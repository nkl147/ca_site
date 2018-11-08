from django.contrib import admin
from . import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):


    search_fields = ['title']

    list_filter = ['published_date']

    list_display = ['title','published_date']






admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Comment)
