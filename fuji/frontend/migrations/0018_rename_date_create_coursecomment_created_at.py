# Generated by Django 4.0 on 2022-01-26 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0017_alter_coursecomment_date_create'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursecomment',
            old_name='date_create',
            new_name='created_at',
        ),
    ]