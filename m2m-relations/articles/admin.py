from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Article, Articles_scope, Articles_tag
from django.core.exceptions import ValidationError

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Articles_scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    list_display = ["title", "text", "published_at", "image"]


@admin.register(Articles_tag)
class Articles_tagAdmin(admin.ModelAdmin):
    list_display = ["name"]
