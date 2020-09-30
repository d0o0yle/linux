from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length= 50)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]
    #객체 중 열글자만 가져오겠다...
