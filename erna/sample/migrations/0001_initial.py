# Generated by Django 4.2.1 on 2023-08-16 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rna_seq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=50)),
                ('sample_name', models.CharField(max_length=100)),
                ('metadata', models.CharField(blank=True, max_length=3000, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('batch_name', 'sample_name'),
            },
        ),
        migrations.CreateModel(
            name='SampleFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=1256)),
                ('file_format', models.CharField(blank=True, max_length=24)),
                ('file_type', models.CharField(blank=True, max_length=24)),
                ('batch_no', models.CharField(blank=True, max_length=128, null=True)),
                ('exist', models.BooleanField(default=False)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.sample')),
            ],
            options={
                'ordering': ('sample', 'file_name'),
            },
        ),
        migrations.CreateModel(
            name='SampleProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rna_seq.project')),
                ('sample_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.samplefile')),
            ],
            options={
                'ordering': ['project', 'sample_file'],
            },
        ),
    ]