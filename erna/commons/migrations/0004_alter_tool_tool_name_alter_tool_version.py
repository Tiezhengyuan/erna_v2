# Generated by Django 4.2.6 on 2023-11-03 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0003_tool_exe_path_alter_tool_default_parameters_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='tool_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tool',
            name='version',
            field=models.CharField(max_length=32),
        ),
    ]
