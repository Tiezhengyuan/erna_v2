# Generated by Django 4.2.1 on 2023-08-15 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=56)),
                ('file_name', models.CharField(max_length=128)),
                ('metadata', models.CharField(max_length=1256)),
            ],
            options={
                'ordering': ['specie', 'version'],
            },
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specie_name', models.CharField(max_length=256, unique=True)),
                ('abbreviation', models.CharField(blank=True, max_length=10, null=True)),
                ('scientific_name', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'ordering': ['specie_name'],
            },
        ),
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('genome_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='annot.genome')),
                ('file_format', models.CharField(choices=[('FQ', 'FASTQ'), ('FA', 'FASTA'), ('GBK', 'GBK'), ('BAT', 'BAT'), ('SAM', 'SAM'), ('BAM', 'BAM'), ('O', 'other')], max_length=10)),
                ('seq_type', models.CharField(choices=[('R', 'RNA'), ('D', 'DNA'), ('P', 'protein'), ('O', 'other')], max_length=10)),
            ],
            bases=('annot.genome',),
        ),
        migrations.AddField(
            model_name='genome',
            name='specie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annot.specie'),
        ),
    ]
