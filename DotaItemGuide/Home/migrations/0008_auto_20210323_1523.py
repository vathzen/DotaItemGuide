# Generated by Django 3.1.7 on 2021-03-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_item_tier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='attrib',
            field=models.CharField(max_length=200),
        ),
    ]
