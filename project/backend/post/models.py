from django.db import models


class Post(models.Model):
    post_ID = models.IntegerField()
    title = models.TextField()
    date = models.DateField()
    During_Date = models.SmallIntegerField() # 종료일 = Date + During_Date \ DB 효율성 고fu
    place = models.CharField(max_length=30)
    body = models.TextField(max_length=1000)
    post_file = models.FileField(blank=True)
    post_img = models.ImageField(blank=True)
    on_offline = models.BooleanField()

    def __str__(self):
        return f'[{self.pk}]{self.title}'

class User(models.Model):
    user_ID = models.CharField(max_length=15)
    user_PW = models.CharField(max_length=15)
    phone_num = models.CharField(max_length=11) # 개인 정보
    birth_year = models.PositiveSmallIntegerField() #개인 정보
    user_money = models.PositiveSmallIntegerField()
    warn_num = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=40) #개인 정보
    lab_name = models.CharField(max_length=40, blank=True)
    verify_flag = models.BooleanField(default=False)
    def __str__(self):
        return f'[{self.pk}]{self.title}'


class User_Post_match(models.Model):
    User_num = models.IntegerField()
    Post_num = models.IntegerField()
    def __str__(self):
        return f'[{self.pk}]{self.title}'