from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('', views.landing_pageView, name='landing_page'),
    path('profile/',views.profileView,name='profile'),
    path('leaderboard/',views.leaderboardView,name='leaderboard'),
    path('tasks/',views.TaskListView,name='task_list'),
    path('tasks/create/',views.TaskCreateView,name='task_create'),
    path('tasks/<int:task_id>/taskdetail',views.TaskDetailView,name='task_detail'),
    path('tasks/<int:task_id>/edit/',views.TaskDetailEditView,name='task_edit'),
    path('tasks/<int:task_id>/delete/',views.TaskDeleteView,name='task_delete'),
    path('tasks/<int:task_id>/complete/',views.TaskCompleteView,name='task_complete'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html',next_page='task_list'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='landing_page'),name='logout'),
    # path('logout/',views.custom_logout,name='logout'),

]