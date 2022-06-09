from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import date
from django.core.validators import MaxLengthValidator,MinLengthValidator


# Create your models here.
class Registration_models(models.Model):
    MALE='Male'
    FEMALE='Female'
    GENDER_CHOICE = [(MALE,'Male'), (FEMALE,'Female')]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    blood_Group = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=200, blank=True)
    mobile_No = models.PositiveBigIntegerField()
    email_Id = models.EmailField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, default=MALE)
    
    
    def __str__(self):
        return self.user.username
    

class Order_blood_model(models.Model):
    MALE='Male'
    FEMALE='Female'
    GENDER_CHOICE = [(MALE,'Male'), (FEMALE,'Female')]
    BLOOD_GR= [ ('A+','A+'),
               ('O+','O+'),
               ('B+','B+'),
               ('AB+','AB+'),
               ('A-','A-'),
               ('B-','B-'),
               ('O-','O-'),
               ('AB-','AB-')]
    user_n = models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    receiver_name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=300)
    unit_qty = models.PositiveSmallIntegerField()
    receiver_contact_no = models.CharField(max_length=10)
    receiver_blood_grp = models.CharField(max_length=100, choices=BLOOD_GR,default='A+')
    receiver_gender = models.CharField(max_length=100,choices=GENDER_CHOICE,default=MALE)
    blood_grp = models.CharField(max_length=100, choices=BLOOD_GR,default='A+')
    email_id = models.EmailField(max_length=50)
    current_date = models.DateField(default=date.today,editable=False)
    
    def __str__(self):
        return self.receiver_name



# Create your models here.

class Received_unit_model(models.Model):
    # x = datetime.date.today()
    # y = datetime.date.strftime(x,format="%d-%m-%Y")
    MALE='Male'
    FEMALE='Female'
    GENDER_CHOICE = [(MALE,'Male'), (FEMALE,'Female')]
    BLOOD_GR= [ ('A+','A+'),
               ('O+','O+'),
               ('B+','B+'),
               ('AB+','AB+'),
               ('A-','A-'),
               ('B-','B-'),
               ('O-','O-'),
               ('AB-','AB-')]
    
    name = models.CharField(max_length=100,)
    blood_group = models.CharField(max_length=100, choices=BLOOD_GR,default='A+')
    unit_qty = models.PositiveSmallIntegerField()
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=100,choices=GENDER_CHOICE,default=MALE)
    adhaar_no =models.CharField( max_length=50,validators=[MinLengthValidator(12), MaxLengthValidator(12)])
    current_date = models.DateField(default=date.today,editable=False)

    def __str__(self):
        return self.adhaar_no
    
class Blood_donate_model(models.Model):
    
    name = models.CharField(max_length=100)
    blood_grp = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
