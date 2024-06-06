from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.core.paginator import Paginator
from django.db import transaction
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from pypinyin import lazy_pinyin

from .forms import UserForm, CustomUserCreationForm
from .models import Book, Borrow, Category

User = get_user_model()


def home(request):
    query = request.GET.get('q', '')
    sort = request.GET.get('sort', 'id')
    category_filter = request.GET.get('category', '')

    books = Book.objects.all()
    if query:
        books = books.filter(title__icontains=query)
        count = books.count()
        if count:
            messages.success(request, f'找到 {count} 本书籍与"{query}"相关！')
        else:
            messages.warning(request, f'没有找到与"{query}"相关的书籍。')

    if category_filter:
        books = books.filter(category_id=category_filter)
        messages.info(request, f'筛选出 {books.count()} 本"{Category.objects.get(id=category_filter)}"类别的书籍。')

    if sort in ['title', '-title', 'author', '-author', 'category', '-category']:
        reverse = sort.startswith('-')
        if 'category' in sort:
            books = sorted(books, key=lambda book: lazy_pinyin(book.category.name if book.category else '')[0],
                           reverse=reverse)
        else:
            field = sort.lstrip('-')
            books = sorted(books, key=lambda book: lazy_pinyin(getattr(book, field))[0], reverse=reverse)
    else:
        books = books.order_by(sort)

    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    return render(request, 'library/home.html', {
        'page_obj': page_obj,
        'query': query,
        'sort': sort,
        'category_filter': category_filter,
        'categories': categories,
    })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, '登录成功！')
                return redirect(request.META.get('HTTP_REFERER', 'home'))
            else:
                messages.error(request, '用户名或密码错误！')
                return redirect(request.META.get('HTTP_REFERER', 'home'))
        else:
            messages.error(request, '用户名或密码错误！')
            return redirect(request.META.get('HTTP_REFERER', 'home'))
    else:
        form = AuthenticationForm()
    return render(request, 'library/login_form.html', {'form': form})


def login_required_message(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request, *args, **kwargs)
        else:
            messages.info(request, '进行借阅操作前请先登录！')
            return redirect(request.META.get('HTTP_REFERER', 'home'))

    return wrap


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, '注册成功！将为您自动登录。')
            return redirect(request.META.get('HTTP_REFERER', 'home'))
        else:
            messages.error(request, '注册失败，请检查填写的信息是否正确。')
            return redirect(request.META.get('HTTP_REFERER', 'home'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'library/register_form.html', {'form': form})


def book_detail(request, book_id):
    try:
        book = get_object_or_404(Book, pk=book_id)
    except Http404:
        messages.error(request, '书籍不存在或已被删除。')
        return redirect('home')
    return render(request, 'library/book_detail.html', {'book': book})


@login_required_message
def borrow_book(request):
    if request.method == 'POST':
        book_ids = request.POST.getlist('borrow_book')
        days = int(request.POST.get('days', 7))
        days = min(max(days, 1), 30)
        due_date = timezone.now().date() + timedelta(days=days)

        books = Book.objects.filter(id__in=book_ids)
        borrows_to_update = set()
        messages_created = set()

        with transaction.atomic():
            for book in books:
                borrow, created = Borrow.objects.get_or_create(
                    user=request.user,
                    book=book,
                    is_returned=0,
                    defaults={'due_date': due_date}
                )
                if created:
                    if book.id not in messages_created:
                        messages.success(request, f'您已成功借阅《{book.title}》！')
                        messages_created.add(book.id)
                else:
                    if borrow.due_date != due_date:
                        borrow.due_date = due_date
                        borrows_to_update.add(borrow)
                        if book.id not in messages_created:
                            messages.info(request, f'您已更新《{book.title}》的到期时间！')
                            messages_created.add(book.id)
                    else:
                        if book.id not in messages_created:
                            messages.info(request, f'您已经借阅了《{book.title}》，到期时间未改变。')
                            messages_created.add(book.id)

            if borrows_to_update:
                Borrow.objects.bulk_update(borrows_to_update, ['due_date'])

        return redirect('borrow_records')

    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def borrow_records(request):
    user = request.user
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    category_filter = request.GET.get('category', '')
    sort = request.GET.get('sort', 'is_returned')

    borrows = Borrow.objects.filter(user=user).select_related('book', 'book__category')

    if query:
        borrows = borrows.filter(book__title__icontains=query)
        count = borrows.count()
        if count:
            messages.success(request, f'找到 {count} 条借阅记录与"{query}"相关！')
        else:
            messages.warning(request, f'没有找到与"{query}"相关的借阅记录。')

    if status_filter is not None and status_filter != '':
        if status_filter == '0':
            borrows = borrows.filter(is_returned=False)
        elif status_filter == '1':
            borrows = borrows.filter(is_returned=True)
        count = borrows.count()
        messages.info(request, f'共有 {count} 条符合筛选条件的借阅记录。')

    if category_filter:
        borrows = borrows.filter(book__category_id=category_filter)
        messages.info(request,
                      f'筛选出 {borrows.count()} 条"{Category.objects.get(id=category_filter)}"类别的借阅记录。')

    if sort in ['borrow_date', '-borrow_date', 'due_date', '-due_date', 'return_date', '-return_date', 'is_returned',
                '-is_returned']:
        borrows = borrows.order_by(sort)
    elif sort in ['title', '-title']:
        reverse = sort.startswith('-')
        borrows = sorted(borrows, key=lambda item: lazy_pinyin(item.book.title)[0], reverse=reverse)
    elif sort in ['category', '-category']:
        reverse = sort.startswith('-')
        borrows = sorted(
            borrows, key=lambda item:
            lazy_pinyin(item.book.category.name if item.book and item.book.category else '')[0], reverse=reverse)
    else:
        borrows = borrows.order_by('is_returned', 'id')

    paginator = Paginator(borrows, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        borrow_ids = request.POST.getlist('return_books')
        if not borrow_ids:
            messages.warning(request, '未选择任何书籍进行归还。')
            return redirect('borrow_records')

        borrows_to_return = Borrow.objects.filter(id__in=borrow_ids, user=user)
        already_returned = set()
        to_update = set()
        with transaction.atomic():
            for borrow in borrows_to_return:
                if borrow.is_returned:
                    already_returned.add(borrow)
                else:
                    borrow.is_returned = True
                    borrow.return_date = timezone.now()
                    to_update.add(borrow)

            if to_update:
                Borrow.objects.bulk_update(to_update, ['is_returned', 'return_date'])
                for borrow in to_update:
                    messages.success(request, f'成功归还书籍《{borrow.book.title}》')
            for borrow in already_returned:
                messages.warning(request, f'书籍《{borrow.book.title}》已于 {borrow.return_date} 归还')

        return redirect('borrow_records')

    categories = Category.objects.all()

    return render(request, 'library/borrow_records.html', {
        'page_obj': page_obj,
        'query': query,
        'status_filter': status_filter,
        'category_filter': category_filter,
        'sort': sort,
        'categories': categories,
    })


@login_required
def user_detail(request):
    user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, '用户信息更新成功！')
            return redirect('user_detail')
        else:
            messages.error(request, '用户信息更新失败，请检查邮箱地址是否正确。')
    else:
        form = UserForm(instance=user)
    return render(request, 'library/user_detail.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '密码更改成功！返回用户详情页。')
            return redirect('user_detail')
        else:
            messages.error(request, '密码更改失败，请检查表单是否符合要求。')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'library/change_password.html', {'form': form})
