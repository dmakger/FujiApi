# Generated by Django 4.0 on 2022-01-09 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.module')),
            ],
        ),
    ]
