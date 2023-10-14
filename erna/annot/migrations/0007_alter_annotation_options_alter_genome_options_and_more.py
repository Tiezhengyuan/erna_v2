# Generated by Django 4.2.5 on 2023-10-14 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annot', '0006_alter_genome_ftp_path'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annotation',
            options={'ordering': ['specie', 'assembly_accession', 'seq_type']},
        ),
        migrations.AlterModelOptions(
            name='genome',
            options={'ordering': ['specie', 'assembly_accession']},
        ),
        migrations.RenameField(
            model_name='genome',
            old_name='assembly_version',
            new_name='assembly_accession',
        ),
        migrations.AlterUniqueTogether(
            name='genome',
            unique_together={('specie', 'assembly_accession')},
        ),
    ]