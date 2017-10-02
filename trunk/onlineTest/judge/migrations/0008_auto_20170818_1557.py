# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-18 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0007_gaicuoproblem_tiankongproblem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gaicuoproblem',
            name='classname',
        ),
        migrations.RemoveField(
            model_name='gaicuoproblem',
            name='creater',
        ),
        migrations.RemoveField(
            model_name='gaicuoproblem',
            name='knowledgePoint1',
        ),
        migrations.RemoveField(
            model_name='gaicuoproblem',
            name='knowledgePoint2',
        ),
        migrations.RemoveField(
            model_name='tiankongproblem',
            name='classname',
        ),
        migrations.RemoveField(
            model_name='tiankongproblem',
            name='creater',
        ),
        migrations.RemoveField(
            model_name='tiankongproblem',
            name='knowledgePoint1',
        ),
        migrations.RemoveField(
            model_name='tiankongproblem',
            name='knowledgePoint2',
        ),
        migrations.AddField(
            model_name='problem',
            name='problem_type',
            field=models.CharField(default='编程', max_length=10, verbose_name='题目类型'),
        ),
        migrations.AddField(
            model_name='problem',
            name='sample_code',
            field=models.TextField(blank=True, null=True, verbose_name='初始代码'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='题目id'),
        ),
        migrations.DeleteModel(
            name='GaicuoProblem',
        ),
        migrations.DeleteModel(
            name='TiankongProblem',
        ),
    ]