# Generated by Django 5.0.4 on 2024-04-12 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_articles_tag_articles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='articles_tag',
            name='articles',
            field=models.ManyToManyField(through='articles.Articles_scope', to='articles.article'),
        ),
    ]
