# Generated by Django 4.0 on 2022-01-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='During_Date',
            field=models.SmallIntegerField(),
        ),
    ]
