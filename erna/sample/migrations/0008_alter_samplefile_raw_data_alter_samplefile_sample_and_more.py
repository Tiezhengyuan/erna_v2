# Generated by Django 4.2.5 on 2023-10-09 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rna_seq', '0005_alter_task_options'),
        ('sample', '0007_alter_sampleproject_sample_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplefile',
            name='raw_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.rawdata'),
        ),
        migrations.AlterField(
            model_name='samplefile',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.sample'),
        ),
        migrations.AlterField(
            model_name='sampleproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sampleprojects', to='rna_seq.project'),
        ),
        migrations.AlterField(
            model_name='sampleproject',
            name='sample_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sampleprojects', to='sample.samplefile'),
        ),
    ]