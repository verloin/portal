# Generated by Django 4.0.3 on 2022-04-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
