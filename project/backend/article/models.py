
from django.db import models
from account.models import CustomUser

class Tag(models.Model):
    subject = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.subject}'

class Article(models.Model):
    writerID = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL) 
    lab = models.CharField(max_length=40) 
    title = models.TextField()
    postDate = models.DateField(auto_now_add=True)
    modifiedDate = models.DateField(auto_now=True)
    startDay = models.DateField()
    endDay = models.DateField()
    startBirth = models.PositiveSmallIntegerField(blank=True, null=True)
    endBirth = models.PositiveSmallIntegerField(blank=True, null=True)
    gender = models.CharField(blank=True, null=True, max_length=6)
    isOffline = models.BooleanField()
    reward = models.PositiveSmallIntegerField() #단위는 원
    location = models.CharField(max_length=30, blank=True, null=True)
    subject = models.ForeignKey(Tag, max_length=30, blank=True, null=True, on_delete=models.SET_NULL)
    content = models.TextField(max_length = 10000)
    articleFile = models.FileField(blank=True, null=True)
    articleImg = models.ImageField(blank=True, null=True)
    hits = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.writerID}'



class Time_table(models.Model):
    pk = models.PositiveIntegerField(primary_key=True)
    article = models.ForeignKey(Article)
    start = models.DateTimeField()
    end = models.DateTimeField()
    ptcpUser = models.ForeignKey(CustomUser)