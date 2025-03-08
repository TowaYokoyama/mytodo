from rest_framework import viewsets
from .models import Task  # Taskモデルをインポート
from .serializers import TaskSerializer  # シリアライザをインポート

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # すべてのタスクを取得
    serializer_class = TaskSerializer  # シリアライザを指定
