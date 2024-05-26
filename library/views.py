from datetime import timedelta

from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import UserForm
from .models import Book, Borrow


def home(request):
    books = Book.objects.all().order_by('id')
    query = request.GET.get('q')

    if query:
        books = books.filter(title__icontains=query)

    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'library/home.html', {
        'page_obj': page_obj,
        'query': query,
    })


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        Borrow.objects.create(user=request.user, book=book, due_date=request.POST['due_date'])
        return redirect('borrow_records')
    return render(request, 'library/borrow_book.html', {'book': book})


@login_required
def borrow_books(request):
    if request.method == 'POST':
        book_ids = request.POST.getlist('borrow_books')
        days = int(request.POST.get('days', 7))
        days = min(max(days, 1), 30)

        for book_id in book_ids:
            book = get_object_or_404(Book, id=book_id)
            borrow, created = Borrow.objects.get_or_create(
                user=request.user,
                book=book,
                is_returned=0,
                defaults={'due_date': timezone.now().date() + timedelta(days=days)}
            )
            if not created:
                borrow.due_date = timezone.now().date() + timedelta(days=days)
                borrow.save()

        return redirect('borrow_records')
    return redirect('home')


@login_required
def borrow_records(request):
    user = request.user
    query = request.GET.get('q')
    status_filter = request.GET.get('status')

    borrows = Borrow.objects.filter(user=user).order_by('id')

    if query:
        borrows = borrows.filter(book__title__icontains=query)

    if status_filter:
        borrows = borrows.filter(is_returned=status_filter)

    paginator = Paginator(borrows, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        borrow_ids = request.POST.getlist('return_books')
        Borrow.objects.filter(id__in=borrow_ids).update(is_returned=1, return_date=timezone.now())
        return redirect('borrow_records')

    return render(request, 'library/borrow_records.html', {
        'page_obj': page_obj,
        'query': query,
        'status_filter': status_filter,
    })


@login_required
def user_detail(request):
    user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail')
    else:
        form = UserForm(instance=user)
    borrows = Borrow.objects.filter(user=user)
    return render(request, 'library/user_detail.html', {'form': form, 'borrows': borrows})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('user_detail')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'library/change_password.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'library/register.html', {'form': form})
