# Generated by Django 4.0.3 on 2022-04-18 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='user.jpg', upload_to='profile_images/'),
        ),
    ]
