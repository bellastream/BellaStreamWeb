# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'ordering': ['timestamp'],
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='BlogsPost',
            new_name='BlogPost',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='post',
            field=models.ForeignKey(to='blog.BlogPost'),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-timestamp']},
        ),
    ]
