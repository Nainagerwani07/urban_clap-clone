# Generated by Django 2.1.2 on 2019-07-31 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urban', '0003_customerrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerrequest',
            name='review',
            field=models.CharField(default='', max_length=100),
        ),
    ]
