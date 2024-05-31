# 导入Django的admin模块
from django.contrib import admin
# 导入Django的UserAdmin类
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# 导入当前应用的模型
from .models import User, Book, Borrow, Category

admin.site.site_header = "图书借阅系统"
admin.site.site_title = "图书借阅系统"
admin.site.index_title = "欢迎使用图书借阅系统"


# 定义UserAdmin类，继承自BaseUserAdmin
class UserAdmin(BaseUserAdmin):
    # 定义在admin界面列表中显示的字段
    list_display = ('username', 'email', 'is_admin')
    # 定义在admin界面右侧的过滤器
    list_filter = ('is_admin',)
    # 定义在admin界面编辑页面的字段组
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser')}),
    )
    # 定义在admin界面添加用户页面的字段组
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    # 定义在admin界面的搜索字段
    search_fields = ('username', 'email')
    # 定义在admin界面的排序字段
    ordering = ('username',)
    # 定义在admin界面的多对多字段的水平滚动条
    filter_horizontal = ()


# 定义BookAdmin类，继承自admin.ModelAdmin
class BookAdmin(admin.ModelAdmin):
    # 定义在admin界面列表中显示的字段
    list_display = ('title', 'author', 'publisher', 'category', 'isbn', 'published_year')
    # 定义在admin界面的搜索字段
    search_fields = ('title', 'author', 'isbn')
    # 定义在admin界面右侧的过滤器
    list_filter = ('publisher', 'published_year')
    # 定义在admin界面编辑页面的字段组
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'publisher', 'category', 'isbn', 'published_year')
        }),
    )

    def changelist_view(self, request, extra_context=None):
        # 获取图书的总数
        total_books = Book.objects.count()
        # 将统计数据添加到上下文中
        extra_context = extra_context or {'total_books': total_books}
        # 调用父类的方法，将新的上下文传递给它
        return super().changelist_view(request, extra_context=extra_context)


# 定义BorrowAdmin类，继承自admin.ModelAdmin
class BorrowAdmin(admin.ModelAdmin):
    # 定义在admin界面列表中显示的字段
    list_display = ('user', 'book', 'borrow_date', 'return_date', 'due_date', 'is_returned')
    # 定义在admin界面的搜索字段
    search_fields = ('user__username', 'book__title', 'book__isbn')
    # 定义在admin界面右侧的过滤器
    list_filter = ('borrow_date', 'return_date', 'due_date', 'is_returned')
    # 定义在admin界面编辑页面的字段组
    fieldsets = (
        (None, {
            'fields': ('user', 'book', 'return_date', 'due_date', 'is_returned')
        }),
    )


# 定义CategoryAdmin类，继承自admin.ModelAdmin
class CategoryAdmin(admin.ModelAdmin):
    # 定义在admin界面列表中显示的字段
    list_display = ('code', 'name')
    # 定义在admin界面的搜索字段
    search_fields = ('code', 'name')
    # 定义在admin界面右侧的过滤器
    list_filter = ('code',)


# 在admin界面注册User模型，使用自定义的UserAdmin类
admin.site.register(User, UserAdmin)
# 在admin界面注册Book模型，使用自定义的BookAdmin类
admin.site.register(Book, BookAdmin)
# 在admin界面注册Borrow模型，使用自定义的BorrowAdmin类
admin.site.register(Borrow, BorrowAdmin)
# 在admin界面注册Category模型，使用自定义的CategoryAdmin类
admin.site.register(Category, CategoryAdmin)
