# Generated by Django 2.1.2 on 2018-11-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceptedProject', '0004_auto_20181128_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptedproject',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='acceptedproject',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]