# Generated by Django 2.0.13 on 2019-06-28 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='b',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
