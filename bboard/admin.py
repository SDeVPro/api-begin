from django.contrib import admin
from .models import Bb, Rubric
class RubricAdmin(admin.ModelAdmin):
    list_display = ['name']
# Register your models here.
class BbAdmin(admin.ModelAdmin):
    list_display = ('title','content','price','published')
    list_display_links = ('title','content')
    search_fields = ('title','content')

 
admin.site.register(Rubric, RubricAdmin)
admin.site.register(Bb, BbAdmin)
