# Generated by Django 2.2.17 on 2021-03-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vrp', '0003_vrpproblem_data_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vrpproblem',
            name='data_path',
        ),
        migrations.RemoveField(
            model_name='vrpproblem',
            name='description',
        ),
        migrations.AddField(
            model_name='routingplan',
            name='vehicle_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
