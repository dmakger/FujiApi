# Generated by Django 4.0 on 2022-01-10 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_remove_usertocourse_course_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('avatar_url', models.URLField()),
                ('mail', models.EmailField(max_length=50)),
                ('about_me_text', models.TextField()),
            ],
        ),
    ]
