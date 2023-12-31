from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    description = models.TextField(verbose_name = 'Описание')
    image = models.ImageField(upload_to='post/')
    course = models.IntegerField(default=1, verbose_name="Курс")

    def __str__(self):
        return self.title
