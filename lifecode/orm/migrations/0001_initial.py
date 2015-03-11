# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('descriptions', models.TextField(default=None, null=True, blank=True)),
                ('counter', models.IntegerField(default=None, null=True, blank=True)),
                ('left', models.IntegerField(default=None, null=True, blank=True)),
                ('right', models.IntegerField(default=None, null=True, blank=True)),
                ('level', models.IntegerField(default=None, null=True, blank=True)),
                ('root', models.IntegerField(default=None, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(default=None, null=True, blank=True)),
                ('parent', models.ForeignKey(related_name=b'children', default=None, blank=True, to='orm.BlogCategory', null=True)),
            ],
            options={
                'db_table': 'blog_category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default=None, max_length=255)),
                ('site', models.CharField(default=None, max_length=255)),
                ('content', models.TextField()),
                ('approved', models.IntegerField()),
                ('ip_address', models.CharField(default=None, max_length=45)),
                ('user_agent', models.CharField(default=None, max_length=45)),
                ('platform', models.CharField(default=None, max_length=45)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(default=None, null=True, blank=True)),
                ('parent', models.ForeignKey(default=None, blank=True, to='orm.BlogComment', null=True)),
            ],
            options={
                'db_table': 'blog_comment',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('slug', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(default=None, null=True, blank=True)),
            ],
            options={
                'db_table': 'blog_post',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPostCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.ForeignKey(to='orm.BlogCategory', db_column=b'category_id')),
                ('post', models.ForeignKey(to='orm.BlogPost', db_column=b'post_id')),
            ],
            options={
                'db_table': 'blog_post_category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPostTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post', models.ForeignKey(to='orm.BlogPost', db_column=b'post_id')),
            ],
            options={
                'db_table': 'blog_post_tag',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('descriptions', models.TextField(default=None, null=True, blank=True)),
                ('counter', models.IntegerField(default=None, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(default=None, null=True, blank=True)),
            ],
            options={
                'db_table': 'blog_tag',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=255)),
                ('displayName', models.CharField(max_length=50)),
                ('active', models.IntegerField()),
                ('role', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('aboutme', models.TextField()),
                ('birthdate', models.DateField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('zipcode', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=45)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to='orm.User')),
            ],
            options={
                'db_table': 'user_profile',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogposttag',
            name='tag',
            field=models.ForeignKey(to='orm.BlogTag', db_column=b'tag_id'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(related_name=b'post', through='orm.BlogPostCategory', to='orm.BlogCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tag',
            field=models.ManyToManyField(related_name=b'post', through='orm.BlogPostTag', to='orm.BlogTag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='user',
            field=models.ForeignKey(related_name=b'user', to='orm.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='post',
            field=models.ForeignKey(related_name=b'comment', to='orm.BlogPost'),
            preserve_default=True,
        ),
    ]
