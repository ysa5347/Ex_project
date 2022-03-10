from django.db import models
from account.models import CustomUser

"""
    하나의 CustomUser와 SubjectTag는 여러개의 Article에 대응할 수 있다.
    하나의 Article은 여러개의 TimeTable에 대응할 수 있다.
    하나의 TimeTable은 여러개의 UserTimeMatchTable에 대응할 수 있다,
"""

class SubjectTag(models.Model):
    subject = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.subject}'

class Article(models.Model):
    writerID = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, related_name='writerID') 
    lab = models.CharField(max_length=40) 
    title = models.TextField()
    postDate = models.DateField(auto_now_add=True)
    modifiedDate = models.DateField(auto_now=True)
    startDay = models.DateField()
    endDay = models.DateField()
    duringTime = models.TimeField(null=True)
    startBirth = models.PositiveSmallIntegerField(blank=True, null=True)
    endBirth = models.PositiveSmallIntegerField(blank=True, null=True)
    gender = models.CharField(blank=True, null=True, max_length=6)
    isOffline = models.BooleanField()
    reward = models.PositiveSmallIntegerField() #단위는 원
    location = models.CharField(max_length=30, blank=True, null=True)
    subject = models.ForeignKey(SubjectTag, max_length=30, blank=True, null=True, on_delete=models.SET_NULL, related_name='sub1st')
    content = models.TextField(max_length = 10000)
    articleFile = models.FileField(blank=True, null=True)
    articleImg = models.ImageField(blank=True, null=True)
    hits = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'[{self.pk}]{self.title}'

class TimeTable(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='timeTable')
    start = models.DateTimeField()
    end = models.DateTimeField()
    numMax = models.SmallIntegerField()
    numPtcp = models.SmallIntegerField()

    def __str__(self):
        return f'{self.pk}'

class UserTimeMatchTable(models.Model):
    ptcpUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ptcpUser')
    Timetable = models.ForeignKey(TimeTable, on_delete=models.CASCADE, related_name='ptcpTable')

    def __str__(self):
        return f'{self.ptcpUser}'