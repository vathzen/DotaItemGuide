# Generated by Django 3.1.7 on 2021-03-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20210323_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='attrib',
            field=models.JSONField(),
        ),
    ]
