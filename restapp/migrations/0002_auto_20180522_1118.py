# Generated by Django 2.0.5 on 2018-05-22 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
