from django.db import models

#회원정보 DB

class User(models.Model):
    username = models.CharField(max_length=64)
    user_id = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    birth = models.IntegerField(max_length=6)
    user_type = models.BooleanField(default=True) #Ture가 학생
    
    class Meta:
        db_table = 'user'


    # def __str__(self):
    #     return self.name + str(self.age)