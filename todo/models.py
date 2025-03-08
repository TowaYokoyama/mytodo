from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ユーザーと紐づける
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)  # 追加
    due_date = models.DateField(null=True, blank=True, default=timezone.now)  # 追加
    priority = models.IntegerField(default=1)  # 追加
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
def clean(self):
        # 締切日が今日より前の日付だったらエラー
        if self.due_date < timezone.now().date():
            raise ValidationError('締切日は今日以降の日付にしてください。')

def __str__(self):
        return self.title  # 管理画面などで表示される名前
    