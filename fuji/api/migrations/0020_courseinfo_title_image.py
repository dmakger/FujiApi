# Generated by Django 4.0 on 2022-01-28 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_remove_course_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinfo',
            name='title_image',
            field=models.ImageField(default='8.jpg', upload_to=''),
        ),
    ]