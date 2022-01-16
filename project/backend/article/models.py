from django.db import models


class Article(models.Model):
    #postID = models.PositiveIntegerField(null=True) # pk로 대체 가능
    writerID = models.PositiveIntegerField(null=True) #로그인 하고, 자동으로 어떻게 받죠
    lab = models.CharField(max_length=40) # lab name를 어떻게 처리할 건가요?(예를 들어, 우리가 Lab 이름들을 모두 저장해 놓고, 번호로 지정해줄 것인가요 아니면 자유롭게 지정할 것인가용?)
    title = models.TextField()
    postDate = models.DateField()
    startDay = models.DateField()
    endDay = models.DateField()
    age = models.PositiveSmallIntegerField(blank=True, null=True) #나이 하나만 받는게 아니라, 나이대를 받아야 하지 않나요
    gender = models.CharField(blank=True, null=True, max_length=6)
    isOffline = models.BooleanField()
    reward = models.PositiveSmallIntegerField() #단위는 원
    location = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField()
    articleFile = models.FileField(blank=True, null=True)
    articleImg = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return f'[{self.pk}]{self.title}'

class User(models.Model):
    userID = models.CharField(max_length=15)
    userPW = models.CharField(max_length=15)
    phone = models.CharField(max_length=11) # 개인 정보
    email = models.CharField(max_length=100)
    birth = models.PositiveSmallIntegerField() #개인 정보
    penalty = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=40) #개인 정보
    lab = models.CharField(max_length=40, blank=True)
    isExp = models.BooleanField(default=False)
    isPermit = models.BooleanField(default=False)

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