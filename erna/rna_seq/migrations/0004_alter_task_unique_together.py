# Generated by Django 4.2.5 on 2023-10-01 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rna_seq', '0003_alter_task_task_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('project', 'task_id')},
        ),
    ]
