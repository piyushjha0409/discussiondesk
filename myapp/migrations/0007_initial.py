# Generated by Django 4.0.5 on 2022-06-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0006_delete_blogcomment_delete_ques'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=12)),
                ('content', models.TextField()),
            ],
        ),
    ]
