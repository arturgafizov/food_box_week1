# Generated by Django 3.0.7 on 2021-01-15 21:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20210115_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewiew',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rewiew',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]