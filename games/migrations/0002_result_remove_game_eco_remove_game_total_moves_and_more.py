# Generated by Django 5.1.4 on 2024-12-14 05:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(max_length=7)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='eco',
        ),
        migrations.RemoveField(
            model_name='game',
            name='total_moves',
        ),
        migrations.AlterField(
            model_name='player',
            name='elo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.result'),
        ),
    ]
