# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 15:42
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=150)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MiUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(max_length=600, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(max_length=600)),
                ('descripcion', models.CharField(max_length=150, null=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagramapp.MiUsuario')),
            ],
        ),
        migrations.AddField(
            model_name='likes',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagramapp.MiUsuario'),
        ),
        migrations.AddField(
            model_name='likes',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagramapp.Post'),
        ),
        migrations.AddField(
            model_name='follow',
            name='username_sigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_username_sigo', to='instagramapp.MiUsuario'),
        ),
        migrations.AddField(
            model_name='follow',
            name='username_sigue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_username_sigue', to='instagramapp.MiUsuario'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagramapp.MiUsuario'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagramapp.Post'),
        ),
    ]
