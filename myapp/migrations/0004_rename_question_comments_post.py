# Generated by Django 4.0 on 2022-06-03 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='Question',
            new_name='post',
        ),
    ]
