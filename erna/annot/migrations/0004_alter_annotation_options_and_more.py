# Generated by Django 4.2.6 on 2023-10-31 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annot', '0003_alter_annotation_genome'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annotation',
            options={'ordering': ('genome', 'file_path')},
        ),
        migrations.RenameField(
            model_name='annotation',
            old_name='file_name',
            new_name='file_path',
        ),
        migrations.AlterUniqueTogether(
            name='annotation',
            unique_together={('genome', 'file_path')},
        ),
    ]
