from django.db import models

#회원정보 DB

class User(models.Model):
    username = models.CharField(max_length=64, verbose_name = '사용자명')
    user_id = models.CharField(max_length=64, verbose_name = '사용자명')
    user_pw = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birth = models.DateField()
    user_type = models.IntegerField()
    
 
    def __str__(self):
        return self.username + str(self.birth)