# Generated by Django 4.1.5 on 2023-03-16 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0021_alter_lesson_lesson_blocks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='lessons',
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='course.course'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_blocks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson_blocks', to='course.lessonblock'),
        ),
        migrations.AlterField(
            model_name='lessonblock',
            name='block_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.images'),
        ),
    ]
