from django.db import models

# Create your models here.

class Header(models.Model):
    title1 = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)
    title3 = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title1
    
class Why(models.Model):
    icon_select = (
        ('gantel', 'gantel'),
        ('banka', 'banka'),
        ('train', 'train'),
        ('vaqt', 'vaqt'),
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    icon = models.CharField(choices=icon_select, max_length=50)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description[:50]
    

class Team(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/img_team/', default='/static/images/user_avatar.jpg', blank=True, null=True)
    url1 = models.URLField(blank=True, null=True)
    url2 = models.URLField(blank=True, null=True)
    url3 = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name 
    
class Footer(models.Model):
    location = models.URLField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    