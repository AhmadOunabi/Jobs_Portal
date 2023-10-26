from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category_name= models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name


JOB_TYPE_CHOISES=(
    ('Full time','Full time'),
    ('Part time','Part time'),
    ('Remote','Remote'),
    ('Freelance','Freelance'),
)

JOB_EXPERIENCE=(
    ('1-2','1-2'),
    ('2-3','2-3'),
    ('3-6','3-6'),
    ('6+','6+'),
)

class Jobs(models.Model):
    category=models.ForeignKey(Category, related_name='job_category', on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=1000)
    logo=models.ImageField(upload_to='jobs/company_logos')
    type=models.CharField(max_length=50,choices=JOB_TYPE_CHOISES)
    loctaion=models.TextField(max_length=200)
    experience=models.CharField(max_length=20,choices=JOB_EXPERIENCE)
    create_date=models.DateTimeField(default=timezone.now)
    salary_from=models.IntegerField()
    salary_to=models.IntegerField()
    
    def __str__(self):
        return self.title

class UserToken(models.Model):
    user_id=models.CharField(max_length=255)
    token=models.CharField(max_length=2000)
    start_date=models.DateTimeField(auto_now_add=True)
    exp_date=models.DateTimeField()
    def __str__(self):
        return self.user_id

class UserProfile(models.Model):
    user=models.OneToOneField(User,related_name='user_profile', on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    telefon=models.CharField(max_length=50)
    def __str__(self):
        return self.first_name