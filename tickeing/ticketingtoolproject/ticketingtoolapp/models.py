from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

priority=(('high','High'),('medium','Medium'),('low','Low'))

status=(('raised','raised'),('accepted','accepted'),('rejected','rejected'),('completed','completed'))

product=(('laptop','Laptop'),('mouse','Mouse'),('headset','Headset'),('keyboard','Keyboard'),('other','Other'))
class ProductModel(models.Model):
    employee_id=models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    employee_name=models.CharField(max_length=100,null=True)
    priority=models.CharField(max_length=100,choices=priority,default='low')
    your_requirement = models.CharField (max_length=100,choices=product,default='Other')
    status = models.CharField(max_length=100, choices=status, default='raised')
    Reason=models.TextField()
    request_raised_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)

application=(('pycharm','Pycharm'),('vscode','VSCode'),('python','Python'),('java','Java'),('mysql','MySql'),
             ('ecllipse','Ecllipse'),('other','Other'))
class ApplicationModel(models.Model):
    employee_id=models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    employee_name=models.CharField(max_length=100,null=True)
    priority=models.CharField(max_length=100,choices=priority,default='low')
    your_requirement = models.CharField(max_length=100, choices=application,default='Other')
    status=models.CharField(max_length=100,choices=status,default='raised')
    Reason=models.TextField()
    request_raised_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)

booking=(('cubical','Cubical'),('training room','Training Room'),('board room','Board Room'),
         ('interview room','Interview Room'),('other','Other'))
class BookingModel(models.Model):
    employee_id=models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    employee_name=models.CharField(max_length=100,null=True)
    priority=models.CharField(max_length=100,choices=priority,default='low')
    your_requirement = models.CharField( max_length=100,choices=booking,default='Other')
    status = models.CharField(max_length=100, choices=status,default='raised')
    Reason=models.TextField()
    request_raised_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)
        
stationary=(('bag','Bag'),('pen','Pen'),('pencil','Pencil'),('paper','Paper'),
            ('stapler','Stapler'),('book','Book'),('other','Other'))
class StationaryModel(models.Model):
    employee_id=models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    employee_name=models.CharField(max_length=100,null=True)
    priority=models.CharField(max_length=100,choices=priority,default='low')
    your_requirement = models.CharField(max_length=100,choices=stationary,default='Other')
    status = models.CharField(max_length=100, choices=status,default='raised')
    Reason=models.TextField()
    request_raised_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)






