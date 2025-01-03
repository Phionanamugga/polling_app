from django.contrib import admin

from .models import Choice, Question


admin.site.register(Question, QuestionAdmin)
# ...
admin.site.register(Choice)

class ChoiceInline(admin.TabularInline): ...


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)