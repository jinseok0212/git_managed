from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser): # AbstractUser를 상속해서 나머지는 기본 테이블에 있음 닉네임이랑 나이는 내가 추가하려고 저거 상속받은거임 
    nickname = models.CharField(max_length=30,blank = True) # 공란 가능 
    age = models.IntegerField(null= True, blank = True)

    def __self__(self):
        return self.username
        
