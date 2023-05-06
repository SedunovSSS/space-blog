from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=100)
    text = models.TextField(max_length=500)

    def __str__(self):
        return f'BlogPost - {self.id}'
