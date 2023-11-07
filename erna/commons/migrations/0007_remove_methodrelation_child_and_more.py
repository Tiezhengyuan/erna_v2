# Generated by Django 4.2.6 on 2023-11-05 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0006_methodtool_methodrelation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='methodrelation',
            name='child',
        ),
        migrations.RemoveField(
            model_name='methodrelation',
            name='method',
        ),
        migrations.RemoveField(
            model_name='methodtool',
            name='method',
        ),
        migrations.RemoveField(
            model_name='methodtool',
            name='tool',
        ),
        migrations.AlterUniqueTogether(
            name='tool',
            unique_together=None,
        ),
        migrations.DeleteModel(
            name='Method',
        ),
        migrations.DeleteModel(
            name='MethodRelation',
        ),
        migrations.DeleteModel(
            name='MethodTool',
        ),
        migrations.DeleteModel(
            name='Tool',
        ),
    ]