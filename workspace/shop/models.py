from tabnanny import verbose
from django.db import models

# Create your models here.
class Book(models.Model):
  """ 本モデル """

  class Meta:
    db_table = "book"
    verbose_name = verbose_name_plural = "本"
  
  title = models.CharField(verbose_name='タイトル', max_length=255)

  def __str__(self):
      return self.name

class Auther(models.Model):
  """ 著者 """

  class Meta:
    db_table = "auther"
    verbose_name = verbose_name_plural = "著者"
  
  auther = models.CharField(verbose_name="著者", max_length=100)

  def __str__(self):
      return self.name

class Publisher(models.Model):
  """ 出版社 """

  class Meta:
    db_table = "publisher"
    verbose_name = verbose_name_plural = "出版社"
  
  publisher = models.CharField(verbose_name="出版社", max_length=100)

  def __str__(self):
      return self.name
