# Generated by Django 3.2 on 2022-07-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='progress',
            field=models.IntegerField(default=0),
        ),
    ]
