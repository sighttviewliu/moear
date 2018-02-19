# Generated by Django 2.0.2 on 2018-02-19 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spiders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(db_index=True, primary_key=True, serialize=False)),
                ('author', models.CharField(blank=True, default='', max_length=255, verbose_name='作者')),
                ('origin_url', models.CharField(max_length=255, unique=True, verbose_name='原文地址')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='发布时间')),
                ('content', models.TextField(verbose_name='文章正文')),
                ('title', models.CharField(max_length=3000, verbose_name='文章标题')),
                ('excerpt', models.CharField(blank=True, max_length=5000, null=True, verbose_name='文章摘要')),
                ('status', models.CharField(choices=[('publish', '发布'), ('private', '私有')], db_index=True, default='publish', max_length=20, verbose_name='文章状态')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('spider', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spiders.Spider', verbose_name='爬虫信息')),
            ],
            options={
                'verbose_name_plural': '文章数据',
                'verbose_name': '文章数据',
            },
        ),
        migrations.CreateModel(
            name='PostMeta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True, verbose_name='键名')),
                ('value', models.TextField(blank=True, default=None, null=True, verbose_name='键值')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post', verbose_name='文章数据')),
            ],
            options={
                'verbose_name_plural': '文章元数据',
                'verbose_name': '文章元数据',
            },
        ),
        migrations.CreateModel(
            name='ReadRecord',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('star', models.SmallIntegerField(choices=[(0, '-'), (1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default=0, verbose_name='评级')),
                ('comment', models.TextField(blank=True, default=None, null=True, verbose_name='读后感')),
                ('post', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Post', verbose_name='文章数据')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name_plural': '阅读记录',
                'verbose_name': '阅读记录',
            },
        ),
        migrations.AlterUniqueTogether(
            name='readrecord',
            unique_together={('post', 'user')},
        ),
    ]
