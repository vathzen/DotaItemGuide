# Generated by Django 3.1.7 on 2021-03-21 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20210321_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cost',
            field=models.IntegerField(null=True),
        ),
    ]
