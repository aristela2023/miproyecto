# Generated by Django 4.2 on 2024-05-24 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_post_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='title',
            field=models.CharField(default='Titulo', max_length=200),
            preserve_default=False,
        ),
    ]