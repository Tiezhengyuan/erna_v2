# Generated by Django 4.2.5 on 2023-10-01 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rna_seq', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['project_id', 'owner']},
        ),
    ]