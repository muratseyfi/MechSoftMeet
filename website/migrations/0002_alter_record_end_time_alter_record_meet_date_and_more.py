# Generated by Django 5.0.2 on 2024-02-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='end_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='meet_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='start_time',
            field=models.TimeField(auto_now=True),
        ),
    ]