# Generated by Django 3.0.2 on 2020-02-03 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0012_auto_20200202_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(),
        ),
    ]
