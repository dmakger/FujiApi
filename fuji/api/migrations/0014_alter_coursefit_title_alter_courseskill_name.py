# Generated by Django 4.0 on 2022-01-26 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_profile_avatar_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursefit',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='courseskill',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
