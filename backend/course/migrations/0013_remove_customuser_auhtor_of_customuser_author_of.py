# Generated by Django 4.1.5 on 2023-03-15 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_customuser_auhtor_of'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='auhtor_of',
        ),
        migrations.AddField(
            model_name='customuser',
            name='author_of',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_of', to='course.course'),
        ),
    ]