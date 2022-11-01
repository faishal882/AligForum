from django.contrib import admin
from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
 list_display = ['name', 'code']
 search_fields = ['name']

class ArticleAdmin(admin.ModelAdmin):
 list_display = ['user', 'category_name', 'timestamp']
 search_fields = ['user__username', 'category__name']

 def category_name(self, obj):
   if obj.category != None:
    return obj.category.name 

 class Meta:
    model = Article

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

