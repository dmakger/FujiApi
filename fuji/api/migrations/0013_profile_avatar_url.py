# Generated by Django 4.0 on 2022-01-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_profile_avatar_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar_url',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
