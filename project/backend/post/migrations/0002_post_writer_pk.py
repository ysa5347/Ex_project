# Generated by Django 3.2.7 on 2022-01-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='writer_pk',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
