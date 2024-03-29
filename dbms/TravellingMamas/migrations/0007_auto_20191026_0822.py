# Generated by Django 2.2 on 2019-10-26 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravellingMamas', '0006_auto_20191026_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='reviews',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='room_type',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='room_type',
            name='room_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='accomadation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tour',
            name='fare',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tour',
            name='reviews',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='number_of_guests',
            field=models.CharField(max_length=100),
        ),
    ]
