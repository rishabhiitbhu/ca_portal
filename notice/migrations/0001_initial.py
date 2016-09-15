# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-15 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ca', '0002_remove_caprofile_college_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='MassNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mass_message', models.TextField()),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('ca', models.ManyToManyField(to='ca.CAProfile')),
                ('mark_read', models.ManyToManyField(blank=True, related_name='mark_read', to='ca.CAProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('mark_read', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('ca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ca.CAProfile')),
            ],
        ),
    ]