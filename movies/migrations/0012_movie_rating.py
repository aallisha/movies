# Generated by Django 3.1.7 on 2021-03-21 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_moviecast_actor_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=2),
        ),
    ]