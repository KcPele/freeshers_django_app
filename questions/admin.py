from django.contrib import admin
from . models import Question, Answer
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    formfield_overrides = {
        models.CharField: {'widget': TinyMCE()},
    }

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)