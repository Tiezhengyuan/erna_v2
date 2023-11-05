# Generated by Django 4.2.6 on 2023-11-05 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rna_seq', '0009_rename_default_parameters_tool_default_params'),
    ]

    operations = [
        migrations.AlterField(
            model_name='methodtool',
            name='method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tools', to='rna_seq.method'),
        ),
        migrations.AlterField(
            model_name='methodtool',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='methods', to='rna_seq.tool'),
        ),
    ]
