from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS=[
        ('pending','Pending'),
        ('completed','Completed'),
        ('in_progress','In Progress'),
        
        
    ]
    
    CATEGORY=[
        ('work','Work'),
        ('personal','Personal'),
        ('others','Others'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    due_date = models.DateField()
    due_time = models.TimeField()
    # user_point = models.IntegerField(default=10)
    status = models.CharField(max_length=20,choices=STATUS,default='pending')
    category = models.CharField(max_length=10,choices=CATEGORY)
    is_completed = models.BooleanField(default=False)
    is_late = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_completed_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.title
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=150, unique=True)
    user_points = models.IntegerField(default=10)
    
    def __str__(self):
        return self.user_name