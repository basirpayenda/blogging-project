# Generated by Django 2.2.7 on 2019-12-01 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_post_count_visits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='count_visits',
        ),
    ]
