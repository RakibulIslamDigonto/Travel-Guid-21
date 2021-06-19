from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.utils.translation import override
from taggit.managers import TaggableManager

# Create your models here.


class Blog(models.Model):
    thumbnail = models.ImageField(upload_to='blog_app/images')
    slug = models.SlugField()
    country = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    tag = TaggableManager()
    short_discription = models.TextField()
    discription = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Blog_app:single_post", kwargs={"slug": self.slug})

    @property
    def comm_count(self):
        return Comment.objects.filter(post=self).count()


class User(models.Model):
    image = models.ImageField(upload_to='blog_app/images')
    name = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=CASCADE, related_name='comment')
    name = models.CharField(max_length=200)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
