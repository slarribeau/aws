# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 05:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_short_name', models.CharField(max_length=8)),
                ('trip_headsign', models.CharField(max_length=80)),
                ('departure_time', models.CharField(max_length=8)),
                ('delay', models.SmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.CharField(max_length=8)),
                ('agency_id', models.CharField(max_length=8)),
                ('route_short_name', models.CharField(max_length=8)),
                ('route_long_name', models.CharField(max_length=80)),
                ('route_desc', models.CharField(max_length=8, null=True)),
                ('route_type', models.CharField(max_length=8, null=True)),
                ('route_url', models.CharField(max_length=120, null=True)),
                ('route_color', models.CharField(max_length=8, null=True)),
                ('route_text_color', models.CharField(max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_id', models.IntegerField()),
                ('stop_code', models.CharField(max_length=16)),
                ('stop_name', models.CharField(max_length=80)),
                ('stop_desc', models.CharField(max_length=80)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('stop_zone', models.CharField(max_length=8, null=True)),
                ('stop_url', models.CharField(max_length=8, null=True)),
                ('stop_location_type', models.CharField(max_length=8, null=True)),
                ('parent_station', models.CharField(max_length=8, null=True)),
                ('timezone', models.CharField(max_length=8, null=True)),
                ('wheelchair', models.CharField(max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StopTimes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.CharField(max_length=8)),
                ('departure_time', models.CharField(max_length=8)),
                ('stop_sequence', models.CharField(max_length=8)),
                ('stop_headsign', models.CharField(max_length=80, null=True)),
                ('pickup_type', models.CharField(max_length=8, null=True)),
                ('drop_off_type', models.CharField(max_length=8, null=True)),
                ('shape_dist_traveled', models.CharField(max_length=8, null=True)),
                ('timepoint', models.CharField(max_length=8, null=True)),
                ('stop_id', models.ForeignKey(db_column='stop_id', on_delete=django.db.models.deletion.CASCADE, to='api.Stops')),
            ],
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=24)),
                ('trip_id', models.CharField(max_length=8)),
                ('trip_headsign', models.CharField(max_length=80)),
                ('trip_short_name', models.CharField(max_length=8, null=True)),
                ('direction_id', models.CharField(max_length=8)),
                ('block_id', models.CharField(max_length=8, null=True)),
                ('shape_id', models.CharField(max_length=8)),
                ('wheelchair_accessible', models.CharField(max_length=8)),
                ('bikes_allowed', models.CharField(max_length=8)),
                ('delay', models.SmallIntegerField(null=True)),
                ('route_id', models.ForeignKey(db_column='route_id', on_delete=django.db.models.deletion.CASCADE, to='api.Routes')),
            ],
        ),
        migrations.AddField(
            model_name='stoptimes',
            name='trip_id',
            field=models.ForeignKey(db_column='trip_id', on_delete=django.db.models.deletion.CASCADE, to='api.Trips'),
        ),
    ]
