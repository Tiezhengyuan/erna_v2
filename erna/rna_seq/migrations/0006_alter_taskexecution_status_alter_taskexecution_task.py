# Generated by Django 4.2.6 on 2023-11-02 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rna_seq', '0005_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskexecution',
            name='status',
            field=models.CharField(choices=[('suspend', 'suspend'), ('ready', 'ready'), ('pause', 'pause'), ('run', 'run'), ('finish', 'finish'), ('fail', 'fail')], default='suspend', max_length=10),
        ),
        migrations.AlterField(
            model_name='taskexecution',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_executions', to='rna_seq.task'),
        ),
    ]
