from django.db import models
import datetime
import re
import bcrypt 

class user_manager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if User.objects.filter(email = postData['email']):
            errors['email'] = "Email already registered, try login"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!")
        try:
            if len(postData['birthday']) == 0:
                errors['birthday'] = "Must enter birthday"
            elif datetime.datetime.strptime(postData['birthday'], '%Y-%m-%d') > datetime.datetime.today():
                errors['birthday'] = "Date cannot be in the future"
            today = datetime.date.today()
            b_day = datetime.datetime.strptime(postData['birthday'], '%Y-%m-%d')
            if (today.year - b_day.year - ((today.month, today.day)<(b_day.month, b_day.day))) < 13:
                errors['birthday'] = "Must be at least 13 years old to register."
        except:
            errors['birthday'] = "Invalid date."
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm']:
            errors['confirm'] = "Passwords do not match"
        return errors
    
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['login_email']):
            errors['login_email'] = ("Invalid email address!")
        user = User.objects.filter(email = postData['login_email'])
        if user:
            logged_user = user[0]
            if not bcrypt.checkpw(postData['login_password'].encode(), logged_user.password.encode()):
                errors['login_password'] = "Password does not match user"
        else: 
            errors['login_email'] = "User does not exist"
        if len(postData['login_password']) < 8:
            errors['login_password'] = "Password must be at least 8 characters"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    birthday = models.DateField()
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = user_manager()

