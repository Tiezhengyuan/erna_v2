# Generated by Django 4.2.6 on 2023-11-05 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rna_seq', '0007_alter_project_sequencing_alter_task_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Method',
            fields=[
                ('method_name', models.CharField(max_length=96, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=1028, null=True)),
            ],
            options={
                'ordering': ['method_name'],
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(max_length=32)),
                ('version', models.CharField(max_length=32)),
                ('tool_path', models.CharField(max_length=256)),
                ('exe_path', models.CharField(max_length=256)),
                ('default_parameters', models.CharField(blank=True, max_length=1028, null=True, verbose_name='default parameters of the tool')),
            ],
            options={
                'ordering': ['tool_name', 'version'],
                'unique_together': {('tool_name', 'version')},
            },
        ),
        migrations.CreateModel(
            name='MethodRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_methods', to='rna_seq.method')),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rna_seq.method')),
            ],
            options={
                'ordering': ['method', 'child'],
            },
        ),
        migrations.CreateModel(
            name='MethodTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='methods', to='rna_seq.method')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tools', to='rna_seq.tool')),
            ],
            options={
                'ordering': ['method', 'tool'],
                'unique_together': {('method', 'tool')},
            },
        ),
    ]
