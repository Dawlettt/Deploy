from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from ckeditor.fields import RichTextField

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    body = RichTextField()
    photo = models.ImageField(upload_to="images/", blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("article_detail", args=[str(self.pk)])
