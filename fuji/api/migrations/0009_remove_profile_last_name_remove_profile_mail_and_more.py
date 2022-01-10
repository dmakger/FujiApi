# Generated by Django 4.0 on 2022-01-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_profile_about_me_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.ImageField(default='http://localhost:8000/media/logo-person.jpg', upload_to=''),
        ),
    ]