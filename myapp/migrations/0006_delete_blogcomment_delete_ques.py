# Generated by Django 4.0 on 2022-06-03 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_comments_blogcomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogComment',
        ),
        migrations.DeleteModel(
            name='Ques',
        ),
    ]
