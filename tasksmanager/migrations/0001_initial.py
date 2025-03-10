# Generated by Django 4.0.3 on 2022-04-22 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('executor', models.CharField(choices=[('new', 'Новая'), ('queue', 'В очереди'), ('work', 'В работе'), ('dane', 'Выполнено'), ('cancel', 'Отменённая')], default='', max_length=32, verbose_name='Исполнитель')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('queue', 'В очереди'), ('work', 'В работе'), ('dane', 'Выполнено'), ('cancel', 'Отменённая')], default='new', max_length=32, verbose_name='Статус ')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Постановщик')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tasksmanager.task')),
            ],
        ),
    ]
