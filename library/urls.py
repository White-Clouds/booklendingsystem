from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('borrow_books/', views.borrow_book, name='borrow_book'),
    path('borrow_records/', views.borrow_records, name='borrow_records'),
    path('user_detail/', views.user_detail, name='user_detail'),
    path('change_password/', views.change_password, name='change_password'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
