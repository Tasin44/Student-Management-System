from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

class CustomUser(AbstractUser):#didn't understand why abstractuser use
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=255,unique=True,db_index=True)#didn't get why dbindex here
    is_authorized = models.BooleanField(default=False)
    login_token = models.CharField(max_length=6,blank=True,null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # Three authentication will be there, one for student,one for admin, one for teacher 
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    #set related name(didn't understand)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name=None,
        blank=True
    )
    #didn't understand
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name=None,
        blank=True
    )

    def __str__(self):
        return self.username

class PasswordResetRequest(models.Model):
    user = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
    email = models.EmailField()
    #user will reset the password with the help of token
    token = models.CharField(max_length=32,default=get_random_string(32),editable=False,unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
     # Define token validity period (e.g., 1 hour)
    TOKEN_VALIDITY_PERIOD= timezone.timedelta(hours=1)

    def is_valid(self):
        return timezone.now()<= (self.created_at+self.TOKEN_VALIDITY_PERIOD)
    
    def send_reset_email(self):#must be provide app name in the link
        reset_link = f"http://localhost:8000/authenticationapp/reset-password/{self.token}/"
        
        send_mail(
            'Password Reset Request',
            f'Click the following link to reset your password: {reset_link}',
            settings.DEFAULT_FROM_EMAIL,
            [self.email],
            fail_silently=False,
        )












