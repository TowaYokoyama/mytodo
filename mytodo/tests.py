from django.contrib.auth.models import User
from todo.models import Task
from django.test import TestCase

class TaskModelTest(TestCase):
    def test_task_creation(self):
        # ユーザーの作成
        user = User.objects.create_user(username='testuser', password='password123')
        
        # Taskの作成時にユーザーを設定
        task = Task.objects.create(
            title="Test Task", 
            description="This is a test.", 
            user=user  # ユーザーを指定
        )
        
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test.")
        self.assertFalse(task.is_completed)
        self.assertEqual(task.user, user)  # ユーザーが正しく設定されているかを確認

