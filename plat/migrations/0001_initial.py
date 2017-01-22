# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-22 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignmentId', models.CharField(max_length=50)),
                ('workerId', models.CharField(max_length=50)),
                ('hitId', models.CharField(max_length=50)),
                ('arriveTime', models.DateTimeField(null=True)),
                ('finishTime', models.DateTimeField(null=True)),
                ('accept', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='HitGroupInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hitGroupId', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('questionsPerHit', models.IntegerField()),
                ('cNum', models.IntegerField()),
                ('taskType', models.CharField(choices=[('SC', 'SingleLabel'), ('MC', 'Multilabel'), ('CL', 'collect'), ('FL', 'FILL'), ('DIY', 'your own task')], default='CIC', max_length=3)),
                ('taskFile', models.CharField(max_length=50)),
                ('taskUI', models.CharField(max_length=50)),
                ('hitRemains', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HitInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hitGroupId', models.CharField(max_length=50)),
                ('hitId', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hitGroupId', models.CharField(max_length=50)),
                ('workerId', models.CharField(max_length=50)),
                ('taskId', models.CharField(max_length=50)),
                ('hitId', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('taskId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('taskDescription', models.CharField(max_length=250)),
                ('taskLabels', models.CharField(max_length=250)),
                ('hitGroupId', models.CharField(max_length=50)),
                ('answered', models.IntegerField(default=0)),
                ('result', models.CharField(max_length=50)),
                ('distribution', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workerId', models.CharField(max_length=50)),
                ('quality', models.FloatField(default=0.7)),
            ],
        ),
    ]