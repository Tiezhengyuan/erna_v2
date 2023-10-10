# Generated by Django 4.2.5 on 2023-10-09 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rna_seq', '0005_alter_task_options'),
        ('sample', '0008_alter_samplefile_raw_data_alter_samplefile_sample_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampleproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rna_seq.project'),
        ),
        migrations.AlterField(
            model_name='sampleproject',
            name='sample_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sample_projects', to='sample.samplefile'),
        ),
    ]
