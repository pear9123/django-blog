# Generated by Django 2.1.5 on 2019-01-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20190124_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img_profile',
            field=models.ImageField(blank=True, default='user/ben.jpg', upload_to='user'),
        ),
    ]
