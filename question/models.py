from django.db import models
from __future__ import unicode_literals
from .fields import ThumbnailImageField

# Create your models here.
class Board(models.Model):
  board_id = models.AutoField('board_id', primary_key=True)
  title = models.CharField('title', max_length=100)  
  content = models.TextField('content')
  regDate = models.DateTimeField('regDate', auto_now_add=True)
  updDate = models.DateTimeField('updDate', auto_now=True)

  def __str__(self):
    return self.title + "/" + self.regDate

class AttFile(models.Model):
  attfile_id = models.AutoField(primary_key=True)
  board = models.ForeignKey(Board)
  image = ThumbnailImageField(upload_to='board/image/%y/%m', default=None, null=True, blank=True)
  regDate = models.DateTimeField('date register', auto_now_add= True)

