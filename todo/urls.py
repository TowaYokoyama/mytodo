from django.urls import path, include
from .views import task_list, task_create, task_edit, task_delete, signup
from todo.api_views import TaskViewSet  # api_viewsからインポート
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # tasksというURLにビューを登録


urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('edit/<int:task_id>/', task_edit, name='task_edit'),  # 編集用URL
    path('delete/<int:task_id>/', task_delete, name='task_delete'),  # 削除用URL
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),  # ユーザー登録ページ
    path('api/', include(router.urls)),  # APIエンドポイントを設定
]
