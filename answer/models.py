# from django.db import models
# from django.utils import timezone
# from sign.models import Accounts

# # Create your models here.
# class Answer(models.Model):
#     teacher_id = models.ForeignKey('Accounts', on_delete=models.CASCADE)
#     #유저이름 확인 필요
#     teacher_title = models.CharField(max_length=200)
#     teacher_content = models.TextField()
#     teacher_image = models.ImageField(blank=True,null=True)
#     #이미지가 없어도 올릴 수 있도록 설정.3
#     pub_date = models.DateTimeField(default = timezone.now)

#     def __str__(self):
#         return self.title

        
    
# form 만들기 전