# Generated by Django 2.1.5 on 2019-01-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20190121_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img_profile',
            field=models.ImageField(blank='user/ben.jpg', upload_to='user'),
        ),
    ]
