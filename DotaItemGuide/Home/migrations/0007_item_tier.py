# Generated by Django 3.1.7 on 2021-03-21 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_item_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tier',
            field=models.IntegerField(null=True),
        ),
    ]
