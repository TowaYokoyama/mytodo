from django.contrib import admin

# Register your models here.
from .models import Task  # Taskモデルをインポート

admin.site.register(Task)  # Taskを管理画面に登録
