# Generated by Django 4.0.1 on 2022-01-08 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_url', models.CharField(blank=True, max_length=150, null=True)),
                ('category', models.CharField(blank=True, max_length=150, null=True)),
                ('headline', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.CharField(blank=True, max_length=150, null=True)),
                ('images', models.CharField(blank=True, max_length=500, null=True)),
                ('news', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
