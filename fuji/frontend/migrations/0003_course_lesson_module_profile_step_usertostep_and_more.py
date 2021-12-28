# Generated by Django 4.0 on 2021-12-23 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('frontend', '0002_remove_lesson_module_id_remove_module_course_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('duration_in_minutes', models.IntegerField()),
                ('rating', models.FloatField(default=0)),
                ('members_amount', models.IntegerField(default=0)),
                ('has_certificate', models.BooleanField()),
                ('max_progress_points', models.IntegerField()),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.author')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.course')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('avatar_url', models.ImageField(upload_to='')),
                ('mail', models.EmailField(max_length=50)),
                ('about_me_text', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='UserToStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.step')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserToModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.module')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserToLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.lesson')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserToCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress_points', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.profile')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='module_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.module'),
        ),
    ]