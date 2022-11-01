from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class Category(models.Model):
      name = models.CharField(max_length=220, null=False, blank=False)
      code = models.CharField(max_length=220, null=False, blank=False, unique=True)


class ArticleQuerySet(models.QuerySet):
    def by_username(self, username):
        return self.filter(user__username__iexact=username)
    
    def by_category(self, category):
        return self.filter(category__name__iexact=category)

    


class ArticleManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ArticleQuerySet(self.model, using=self._db)

    

class Article(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
      timestamp = models.DateTimeField(auto_now_add=True)
      headline = models.TextField()
      content = models.TextField()
      
      objects = ArticleManager()



