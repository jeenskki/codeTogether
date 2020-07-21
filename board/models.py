from django.db import models

# Create your models here.
class questionBoard(models.Model):
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=1000)
  pub_date = models.DateTimeField('date published')
  img = models.ImageField(default=None, null= True, blank= True)
  author_name = models.CharField(max_length=20)

  def __str__(self):
    return self.title / self.pub_date

class answerBoard(models.Model):
  q_id = models.ForeignKey(questionBoard.id, on_delete=models.CASCADE)
  atitle = models.CharField(max_length=100)
  a_content = models.CharField(max_length=1000)
  a_pub_date = models.DateTimeField('date published')
  a_img = models.ImageField(default=None, null=True, blank=True)
  author_name = models.CharField(max_length=20)
    
