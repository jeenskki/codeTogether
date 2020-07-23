from datetime import datetime as dt
from django.db import models
from sign.models import Accounts
# Create your models here.
class Board(models.Model):
  content_id = models.AutoField('content_id', primary_key=True)
  account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  content = models.TextField(max_length=2000)
  img = models.ImageField(upload_to='./ans_img/% Y/% m/% d/', blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)
  mod_date = models.DateTimeField(auto_now=True)
  content_type = models.IntegerField(default=0)
  reply_chk = models.IntegerField(default=0)
  # request_to_teacher = models.IntegerField()

  class Meta:
    db_table = 'board'

  def __str__(self):
    return self.title + ' / ' + self.pub_date.strftime('%Y-%m-%d')

