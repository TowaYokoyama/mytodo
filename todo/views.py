from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# タスク一覧
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

# タスク作成
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)  # フォームエラーをコンソールに表示
            return redirect('task_list')  # 登録後、一覧ページにリダイレクト
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})

# タスク編集
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # 編集後、一覧ページにリダイレクト
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_edit.html', {'form': form})

# タスク削除
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # 削除後、一覧ページにリダイレクト
    return render(request, 'todo/task_delete.html', {'task': task})

# todo/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# ユーザー登録処理
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # ユーザーを保存
            login(request, user)  # ログイン後、自動的にユーザーを認証
            return redirect('task_list')  # 登録後、タスク一覧ページにリダイレクト
    else:
        form = UserCreationForm()  # GETリクエストなら空のフォームを渡す

    return render(request, 'todo/signup.html', {'form': form})


from django.contrib.auth.decorators import login_required
# タスク一覧（ログインユーザーのみ）
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # ユーザーごとにタスクを表示
    return render(request, 'todo/task_list.html', {'tasks': tasks})

# タスク作成（ログインユーザーのみ）
@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # ユーザーに紐付けて保存
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})

# タスク編集（ログインユーザーのみ）
@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # ユーザーに紐付いたタスクを取得
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_edit.html', {'form': form})

# タスク削除（ログインユーザーのみ）
@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # ユーザーに紐付いたタスクを取得
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/task_delete.html', {'task': task})

# todo/views.py
from rest_framework import viewsets
from .models import Task  # Taskモデルをインポート
from .serializers import TaskSerializer  # 作成したシリアライザをインポート

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # すべてのタスクを取得
    serializer_class = TaskSerializer  # シリアライザを指定
