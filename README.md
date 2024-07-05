# 图书借阅系统 booklendingsystem

## 简介 Abstract

这是一个简单的基于Django的图书借阅系统，实现了基本的图书借阅管理功能。

**项目用于MySQL结课作业，仅供学习交流使用。**

包括：

1. 用户注册、登录、注销、修改密码、修改邮箱
2. 用户借书、还书、查看借阅记录
3. 书籍分类、排序、筛选、搜索以及查看详情

## 项目依赖 Dependencies

### 架构 Architecture

1. Django 5.0.6
2. Bootstrap 4.6.2
3. jQuery 3.6.0
4. MySQL 8.0.37
5. Python 3.12.3

### Python软件包 Packages

详见`requirements.txt`文件。

```plaintext
asgiref~=3.8.1
cffi~=1.16.0
cryptography~=42.0.7
Django~=5.0.6
django-pagination~=1.0.7
mysqlclient~=2.2.4
pycparser~=2.22
pypinyin~=0.51.0
python-decouple~=3.8
sqlparse~=0.5.0
tzdata~=2024.1
```

### 环境 Environment

在`.env`文件中设置环境变量（需要自行创建）

```plaintext
SECRET_KEY=
DEBUG=True
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=localhost
DATABASE_PORT=3306
LANGUAGE_CODE=zh-hans
TIME_ZONE=Asia/Shanghai
```

## 使用说明 Usage

安装环境并配置完数据库链接后，打开PyCharm的终端，或者自行进入项目的venv环境，运行`python manage.py migrate`
命令迁移数据库，运行`python manage.py createsuperuser`命令创建超级用户。

打开数据库管理工具如Navicat，在你链接的数据库上运行`books.sql`和`categories.sql`文件，初始化数据。

`books.sql`中不包含书籍封面的链接，你可以自行添加。

## TODO

### v1.0

- [x] 用户相关基本操作
- [x] 图书相关基本操作

### v1.1

- [x] 现首页的图书排序筛选
- [x] 书籍分类
    - [x] 书籍分类模型
    - [x] 书籍分类筛选
    - [x] 书籍分类排序

### v1.2

- [x] 优化代码
- [x] 图书详情页
    - [x] 图书基础信息
    - [x] 图书封面
    - [x] 图书简介
- [x] 搜索优化
    - [ ] ~~全站搜索~~
    - [ ] ~~部分搜索添加结果页~~
    - [x] 搜索结果排序

### v2.0+ (有时间就做)

- [ ] 项目AJAX化
    - [ ] 用户操作
    - [ ] 图书操作
    - [ ] Toast
    - [ ] 进度条
- [ ] 更多书籍扩展内容
    - [ ] 书籍评论
    - [ ] 书籍评分
    - [ ] 书籍推荐
    - [ ] 书籍借阅排行榜
- [ ] 更多用户扩展内容
    - [ ] 用户动态
    - [ ] 用户借阅排行榜
    - [ ] 用户积分
    - [ ] 用户等级
    - [ ] 用户勋章
    - [ ] 用户签到
    - [ ] 用户收藏
    - [ ] 用户关注
- [ ] 全站搜索

## 许可证 License

[MIT License](https://github.com/White-Clouds/bookledingsystem/blob/main/LICENSE)