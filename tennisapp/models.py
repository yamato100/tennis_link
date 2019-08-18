from django.db import models

# Create your models here.

class TennisModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    time = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=100, null=True)

    # 要素のうち正の数の数を数えて、それを長さとする
#adminページへアクセス時にエラーが出る
#        cnt = 0
#        for i in self:
#            if i > 0:
#                cnt += 1
#        return cnt