# Generated by Django 3.1.4 on 2021-02-17 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210217_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviecast',
            name='actor_name',
            field=models.CharField(default='Unnamed Actor', max_length=50),
            preserve_default=False,
        ),
    ]
