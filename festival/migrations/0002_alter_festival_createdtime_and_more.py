# Generated by Django 4.2.2 on 2023-08-12 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festival',
            name='createdtime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='festival',
            name='modifiedtime',
            field=models.DateTimeField(),
        ),
    ]
