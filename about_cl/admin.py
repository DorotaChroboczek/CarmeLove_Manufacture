from django.contrib import admin


from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title_main', 'preface_main',
                    'title_midmost', 'preface_midmost', 'text')
