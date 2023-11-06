# Generated by Django 4.2.6 on 2023-11-06 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rna_seq', '0013_pipeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipeline',
            name='next_step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_steps', to='rna_seq.methodtool'),
        ),
    ]
