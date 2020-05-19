from django.db import models

class Post(models.Model):
     title = models.CharField(max_length=100)
     published = models.DateTimeField()
     image = models.ImageField(upload_to = 'media/')
     body = models.TextField()
# データベースをあたかも変数かのように扱えるようにする
# 役割をもつclassをmodels.pyに定義

# Create your models here.