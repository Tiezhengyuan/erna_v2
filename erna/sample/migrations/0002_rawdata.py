# Generated by Django 4.2.5 on 2023-09-29 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=20)),
                ('file_path', models.CharField(max_length=512)),
                ('file_name', models.CharField(max_length=128)),
                ('file_type', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'ordering': ['batch_name', 'file_path'],
            },
        ),
    ]
