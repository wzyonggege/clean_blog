from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from DjangoUeditor.models import UEditorField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category)
    content = UEditorField(verbose_name='Content',
                           width=600, height=300, toolbars="full",
                           imagePath="blog/ueditor/", filePath="blog/ueditor/",
                           upload_settings={"imageMaxSize": 1204000},
                           default='')

    created_time = models.DateTimeField()
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
