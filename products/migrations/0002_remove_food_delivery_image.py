# Generated by Django 3.2.4 on 2021-06-10 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='delivery_image',
        ),
    ]
