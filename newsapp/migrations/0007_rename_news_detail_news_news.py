# Generated by Django 4.0.1 on 2022-01-08 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0006_alter_news_category_alter_news_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='news_detail',
            new_name='news',
        ),
    ]
