from django.db import models


class Post(models.Model): # 내맘대로 짜봤음/
    post_ID = models.PositiveIntegerField() # pk로 대체 가능
    writer_pk = models.PositiveIntegerField()
    lab_name = models.CharField(max_length=40) # lab name를 어떻게 처리할 것인가.(예를 들어, 우리가 Lab 이름들을 모두 저장해 놓고, 번호로 지정해줄 것인가 아니면 자유롭게 지정할 것인가)
    title = models.TextField()
    post_date = models.DateField()
    exp_start = models.DateField()
    exp_end = models.SmallIntegerField() # 종료일 = Date + During_Date
    sub_age = models.PositiveSmallIntegerField()
    sub_gender = models.BooleanField() # 남 0 여 1
    on_offline = models.BooleanField()
    reward = models.PositiveSmallIntegerField() #단위는 원
    location = models.CharField(max_length=30)
    body = models.TextField(max_length=1000)
    post_file = models.FileField(blank=True)
    post_img = models.ImageField(blank=True)
    

    def __str__(self):
        return f'[{self.pk}]{self.title}'

class User(models.Model):
    user_ID = models.CharField(max_length=15)
    user_PW = models.CharField(max_length=15)
    phone_num = models.CharField(max_length=11) # 개인 정보
    birth_year = models.PositiveSmallIntegerField() #개인 정보
    
    penalty = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=40) #개인 정보
    lab_name = models.CharField(max_length=40, blank=True)
    exp_submit = models.BooleanField(default=False) # 왜 booleanfield 사용하지 않는가?
    permit = models.BooleanField(default=0) # 왜 booleanfield 사용하지 않는가?
    

class User_Post_match(models.Model):
    user_pk = models.PositiveIntegerField()
    post_pk = models.PositiveIntegerField()
    time_length = models.PositiveIntegerField()

class Time_table(models.Model):
    exp_info = models.PositiveIntegerField()
    user_pk = models.PositiveIntegerField()
    start = models.PositiveSmallIntegerField()# 0 ~ 1440 min
    end = models.PositiveSmallIntegerField() # 0 ~ 1440 min
    boolean = models.PositiveSmallIntegerField()  # 왜 booleanfield 사용하지 않는가?
    day = models.CharField(max_length=8) # 왜 Datefield 사용하지 않는가?