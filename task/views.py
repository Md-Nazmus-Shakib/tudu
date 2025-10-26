from urllib import request
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from . import models
from django.contrib.auth.decorators import login_required
from .import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from datetime import datetime

# Create your views here.
# class CreateTaskView(CreateView):
#     model = models.Task
#     from_class = forms.TaskForm
#     trmplate_name=''
#     success_url =reverse_lazy('')
    
    
# class TaskListView(ListView):
#     model =models.Task
#     template_name=''

@login_required
def TaskListView(request):
    status_filter = request.GET.get('status', 'pending')
    category_filter = request.GET.get('category', 'all')
    user_profile = models.UserProfile.objects.get(user=request.user)
    tasks = models.Task.objects.filter(user=request.user).order_by('is_completed','due_date','due_time')
    
    stat_count={
        'all': tasks.count(),
        'completed': tasks.filter(is_completed=True).count(),
        'pending': tasks.filter(is_completed=False).count(),
        'delayed': tasks.filter(is_late=True).count(),
        'user_points': user_profile.user_points,
    }
    
    if status_filter != 'all':
        tasks = tasks.filter(is_completed=(status_filter == 'completed'))
    if category_filter != 'all':
        tasks = tasks.filter(category=category_filter)
    completed_tasks = tasks.filter(is_completed=True)
    pending_tasks = tasks.filter(is_completed=False)
    delayed_tasks = tasks.filter(is_late=True)
    
    
    return render(request,'task_list.html',{
        'tasks'  : tasks,
        'delayed_tasks' : delayed_tasks,
        'pending_tasks' :   pending_tasks,
        'status_filter' :   status_filter,
        'completed_tasks' : completed_tasks,
        'category_filter' : category_filter,
        'stat_count' : stat_count,
        'user_profile': user_profile,
    })
@login_required
def TaskCreateView(request):
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = forms.TaskForm()
    return render(request,'create_task.html',{'form':form})
@login_required           
def TaskDetailView(request, task_id):
    task = get_object_or_404(models.Task,id=task_id,user=request.user)
    return render(request,'task_detail.html',{'task': task})
@login_required
def TaskDeleteView(request,task_id):
    task = get_object_or_404(models.Task,id=task_id,user=request.user)
    task.delete()
    return redirect('task_list')
@login_required
def TaskCompleteView(request,task_id):
    task = get_object_or_404(models.Task,id=task_id,user=request.user)
    task.is_completed = True
    # task.status = 'completed'
    user_profile = models.UserProfile.objects.get(user=request.user)#userprofile model er object
    task.task_completed_at = timezone.now()
    due_datetime = datetime.combine(task.due_date, task.due_time)
    due_datetime = timezone.make_aware(due_datetime)
    time_difference = task.task_completed_at - due_datetime
    hours_late = time_difference.total_seconds() / 3600  # Convert to hours
    
    # Award points based on lateness
    if hours_late <= 0:
        # Completed BEFORE or ON TIME
        user_profile.user_points += 10
        messages.success(request, f'✅ On time! +10 points')
        
    elif hours_late <= 24:
        # Late but SAME DAY (within 24 hours)
        user_profile.user_points += 5
        messages.success(request, f'✅ Late but completed ! +5 points')
        
    else:
        # VERY LATE (more than 1 day)
        task.is_late = True
        user_profile.user_points -= 5
        
        messages.warning(request, f'⚠️ Very late! -5 points')
    user_profile.save()
    
    task.save()
    # messages.success(request, f'✅ Task "{task.title}" marked as completed!')
    return redirect('task_list',)
@login_required
def TaskDetailEditView(request,task_id):
    user_profile = models.UserProfile.objects.get(user=request.user)
    task = get_object_or_404(models.Task,id=task_id,user=request.user)
    form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    return render(request,'create_task.html',{'form':form,'edit':True, 'user_profile':user_profile})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            models.UserProfile.objects.create(
                user = form.instance,
                user_name = form.instance.username,
                user_points = 10,
            )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')#password1 karon passswrord hashed thake othoba login(request,form.save()) use kora jete pare
            user = authenticate(username=username,password=password)
            
            login(request,user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})
@login_required
def profileView(request):
    user = request.user
    # task = models.Task.objects.filter(user=user)
    profile_detail = models.Task.objects.filter(user=user)
    count_tasks = profile_detail.count()
    pending_tasks = profile_detail.filter(is_completed=False)
    completed_tasks = profile_detail.filter(is_completed=True)
    delayed_tasks = profile_detail.filter(is_late=True)
    user_profile = models.UserProfile.objects.get(user=request.user)

    return render(request,'profile.html',{'profile_detail':profile_detail,'count_tasks':count_tasks,'pending_tasks':pending_tasks,'completed_tasks':completed_tasks,'delayed_tasks':delayed_tasks,'user_profile':user_profile})

@login_required
def leaderboardView(request):
    user_profile = models.UserProfile.objects.get(user=request.user)
    leaderboard_users = models.UserProfile.objects.all().order_by('-user_points')
    return render(request,'leaderboard.html',{'leaderboard_users':leaderboard_users,'user_profile':user_profile})

# def custom_logout(request):
#     logout(request)  # deletes session and cookie
#     request.session.flush()  # ensures all session data is removed
#     return redirect('landing_page')
# @login_required
# def user_pointsView(request):
#     user = request.user
#     tasks = models.Task.objects.filter(user=user, is_completed=True)
    
#     # give 10 points for each completed task
#     tasks.update(user_point=10)
    
#     # calculate total
#     total_points = 0
#     for task in tasks:
#         total_points += task.user_point

#     return render(request, 'profile.html', {'total_points': total_points})

    
    

