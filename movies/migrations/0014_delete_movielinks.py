# Generated by Django 3.1.7 on 2021-04-05 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_moviecomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MovieLinks',
        ),
    ]