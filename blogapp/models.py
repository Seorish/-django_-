from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200) 
    body = models.TextField()
    # CharField보다 더 큰 범위 text 인 경우
    date = models.DateTimeField(auto_now_add=True)
    # 자동으로 지금 시간을 추가하겠다.



    def __str__(self):
        return self.title