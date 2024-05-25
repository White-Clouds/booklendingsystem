from django.contrib import admin
from .models import Book, User, Borrow


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'isbn', 'published_year')
    search_fields = ('title', 'author', 'isbn')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'is_admin')
    search_fields = ('username', 'email')


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date', 'due_date')
    search_fields = ('user__username', 'book__title')
