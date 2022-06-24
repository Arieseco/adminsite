from django.contrib import admin
from .models import Book,Auther,Publisher

# 管理サイトにModelを登録
admin.site.register(Book)
admin.site.register(Auther)
admin.site.register(Publisher)
