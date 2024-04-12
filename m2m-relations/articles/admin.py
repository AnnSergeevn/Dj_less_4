from django.contrib import admin

from django.forms import BaseInlineFormSet
from .models import Article, Articles_scope, Articles_tag
from django.core.exceptions import ValidationError


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            ind = []
            if form.cleaned_data['is_main'] == True:
                ind.append(1)

            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            if len(ind) > 1:
                raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Articles_scope
    extra = 0
    formset = RelationshipInlineFormset
    show_change_link = True


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "text", "published_at", "image"]
    search_fields = ["title", "text"]
    inlines = [RelationshipInline,]



@admin.register(Articles_tag)
class Articles_tagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [RelationshipInline,]


