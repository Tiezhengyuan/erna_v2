# Generated by Django 4.2.5 on 2023-10-14 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annot', '0005_alter_annotation_options_alter_genome_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genome',
            name='ftp_path',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]