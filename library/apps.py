from django.apps import AppConfig


# LibraryConfig 类
# Django 应用配置类，用于设置应用的一些属性
class LibraryConfig(AppConfig):
    # 设置应用中模型的默认自动字段类型
    default_auto_field = 'django.db.models.BigAutoField'

    # 设置应用的名称
    name = 'library'
