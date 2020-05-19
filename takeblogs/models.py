from django.db import models

class Post(models.Model):
     title = models.CharField(max_length=100)
     published = models.DateTimeField()
     image = models.ImageField(upload_to = 'media/')
     body = models.TextField()
# データベースをあたかも変数かのように扱えるようにする
# 役割をもつclassをmodels.pyに定義

def __str__(self):
    return self.title
# defとは、英語のdefine（定義する）の略
# str()は、数値を文字列に変換する機能で、strは Strings（文字列）の意味
# self.titleで自身のtitleを返す

# Create your models here.