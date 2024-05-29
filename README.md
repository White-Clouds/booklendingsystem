# 图书借阅系统 bookledingsystem

## 简介 Abstract

这是一个简单的基于Django的图书借阅系统，实现了基本的图书借阅管理功能。

**项目用于MySQL结课作业，仅供学习交流使用。**

包括：

1. 用户注册、登录、注销、修改密码、修改邮箱
2. 用户借书、还书、查看借阅记录

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
pycparser~=2.22
PyMySQL~=1.1.1
sqlparse~=0.5.0
tzdata~=2024.1
```

## TODO

### v1.0

- [x] 用户相关基本操作
- [x] 图书相关基本操作

### v1.1

- [ ] 现首页的图书筛选
- [ ] 图书详情页
    - [x] 图书基础信息
    - [ ] 图书封面
    - [ ] 图书简介
- [ ] 书籍分类
    - [ ] 书籍分类筛选

### v1.2

- [ ] 搜索优化
    - [ ] 全站搜索
    - [ ] 部分搜索添加结果页
    - [ ] 搜索结果排序
    

### v2.0 (有时间就做)

- [ ] 项目AJAX化
    - [ ] 用户操作
    - [ ] 图书操作
    - [ ] Toast
    - [ ] 进度条
- [ ] 书籍借阅排行榜
- [ ] 用户借阅排行榜

## 许可证 License

[MIT License](https://github.com/White-Clouds/bookledingsystem/blob/main/LICENSE)