# Generated by Django 2.2.7 on 2019-11-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='posts/%Y/%m/%d'),
        ),
    ]