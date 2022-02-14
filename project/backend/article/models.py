
from django.db import models
from account.models import CustomUser

class Article(models.Model):
    writerID = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL) 
    lab = models.CharField(max_length=40) # lab name를 어떻게 처리할 건가요?(예를 들어, 우리가 Lab 이름들을 모두 저장해 놓고, 번호로 지정해줄 것인가요 아니면 자유롭게 지정할 것인가용?)
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
    subject = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField(max_length = 10000)
    articleFile = models.FileField(blank=True, null=True)
    articleImg = models.ImageField(blank=True, null=True)
    hits = models.PositiveIntegerField()
    
    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.writerID}'

class User_Article_match(models.Model):
    pkUser = models.PositiveIntegerField()
    pkPost = models.PositiveIntegerField()
    timeLength = models.PositiveIntegerField()

class Time_table(models.Model):
    expInfo = models.PositiveIntegerField()
    pkUser = models.PositiveIntegerField()
    startTime = models.PositiveSmallIntegerField()# 0 ~ 1440 min
    endTime = models.PositiveSmallIntegerField() # 0 ~ 1440 min
    isCheck = models.BooleanField(default=False) # True: 예약이 차 있다.  
    day = models.DateField()