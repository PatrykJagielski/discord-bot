from django.contrib import admin

from . import models


class AnswearInLine(admin.TabularInline):
    model = models.Answear
    fields = [
        "answear",
        "is_correct",
    ]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "points",
        "difficulty",
    ]
    list_display = [
        "title",
        "updated_at",
    ]
    inlines = [
        AnswearInLine,
    ]


@admin.register(models.Answear)
class AnswearAdmin(admin.ModelAdmin):
    list_display = [
        "answear",
        "is_correct",
        "question",
    ]
