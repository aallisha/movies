# Generated by Django 3.1.4 on 2021-02-21 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20210218_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieCast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.moviecast'),
        ),
    ]
