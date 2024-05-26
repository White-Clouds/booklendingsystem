from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# 定义了一个名为Book的模型，代表图书
class Book(models.Model):
    # 图书的标题，最大长度为255，必须唯一
    title = models.CharField(max_length=255, unique=True, verbose_name='书名')
    # 图书的作者，最大长度为255
    author = models.CharField(max_length=255, verbose_name='作者')
    # 图书的出版社，最大长度为255
    publisher = models.CharField(max_length=255, verbose_name='出版社')
    # 图书的ISBN号，必须唯一
    isbn = models.BigIntegerField(unique=True, verbose_name='ISBN')
    # 图书的出版年份，可以为空
    published_year = models.BigIntegerField(null=True, blank=True, verbose_name='出版年份')

    def __str__(self):
        # 返回图书的标题作为对象的字符串表示
        return self.title

    class Meta:
        # 定义数据库表名
        db_table = 'books'
        # 定义模型的可读名称
        verbose_name = '书籍'
        # 定义模型的可读名称（复数形式）
        verbose_name_plural = '书籍'
        # 定义模型的约束，这里是设置title字段唯一
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_title')
        ]
        # 是否在管理器中显示此模型
        managed = True


# 定义了一个名为UserManager的模型管理器，用于创建用户和超级用户
class UserManager(BaseUserManager):
    # 创建用户的方法
    def create_user(self, username, email, phone, password=None):
        # 如果没有提供电子邮件，则抛出错误
        if not email:
            raise ValueError('用户必须有电子邮件地址')
        # 创建用户
        user = self.model(username=username, email=self.normalize_email(email), phone=phone)
        # 设置用户密码
        user.set_password(password)
        # 保存用户
        user.save(using=self._db)
        return user

    # 创建超级用户的方法
    def create_superuser(self, username, email, phone, password=None):
        # 创建用户
        user = self.create_user(username, email, phone, password)
        # 设置用户为管理员
        user.is_admin = True
        # 设置用户为员工
        user.is_staff = True
        # 设置用户为超级用户
        user.is_superuser = True
        # 保存用户
        user.save(using=self._db)
        return user


# 定义了一个名为User的模型，代表用户
class User(AbstractBaseUser, PermissionsMixin):
    # 用户名，最大长度为50，必须唯一
    username = models.CharField(max_length=50, unique=True, verbose_name='用户名')
    # 用户的电子邮件，最大长度为255，必须唯一
    email = models.EmailField(max_length=255, unique=True, verbose_name='邮箱')
    # 用户是否活跃，默认为True
    is_active = models.BooleanField(default=True)
    # 用户是否为员工，默认为False
    is_staff = models.BooleanField(default=False)
    # 用户是否为管理员，默认为False
    is_admin = models.BooleanField(default=False)

    # 使用自定义的模型管理器
    objects = UserManager()

    # 定义用户名字段为模型的主要标识字段
    USERNAME_FIELD = 'username'
    # 定义创建用户时必须提供的字段
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        # 返回用户名作为对象的字符串表示
        return self.username

    class Meta:
        # 定义数据库表名
        db_table = 'users'
        # 定义模型的可读名称
        verbose_name = '用户'
        # 定义模型的可读名称（复数形式）
        verbose_name_plural = '用户'
        # 定义模型的约束，这里是设置username字段唯一
        constraints = [
            models.UniqueConstraint(fields=['username'], name='unique_username')
        ]
        # 是否在管理器中显示此模型
        managed = True


# 定义了一个名为Borrow的模型，代表借阅记录
class Borrow(models.Model):
    # 定义了一个名为RETURN_STATUS的列表，包含两个元组，每个元组代表一种归还状态
    RETURN_STATUS = [
        (0, '未归还'),
        (1, '已归还'),
    ]
    # 用户字段，外键关联到User模型，当关联的User对象被删除时，该借阅记录也会被删除
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户ID')
    # 借阅的图书字段，外键关联到Book模型，当关联的Book对象被删除时，该借阅记录也会被删除
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='书籍ID')
    # 借阅日期字段，自动设置为当前日期
    borrow_date = models.DateField(auto_now_add=True, verbose_name='借阅日期')
    # 归还日期字段，可以为空
    return_date = models.DateField(null=True, blank=True, verbose_name='归还日期')
    # 到期日期字段
    due_date = models.DateField(verbose_name='到期日期')
    # 是否已归还字段，0表示未归还，1表示已归还，默认为0
    is_returned = models.IntegerField(choices=RETURN_STATUS, default=0, verbose_name='是否归还')

    def __str__(self):
        # 定义了对象的字符串表示，返回"{用户名} 借阅了 {图书标题}"
        return f"{self.user.username} borrowed {self.book.title if self.book else '此书籍已被删除。'}"

    class Meta:
        # 定义数据库表名
        db_table = 'borrow_records'
        # 定义模型的可读名称
        verbose_name = '借阅记录'
        # 定义模型的可读名称（复数形式）
        verbose_name_plural = '借阅记录'
        # 是否在管理器中显示此模型
        managed = True
