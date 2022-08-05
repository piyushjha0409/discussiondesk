from django.contrib import admin
from questions.models import Ques, BlogComment
# Register your models here.

admin.site.register((Ques, BlogComment))