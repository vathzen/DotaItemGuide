# Generated by Django 3.1.7 on 2021-03-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20210321_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.CharField(max_length=10, null=True),
        ),
    ]