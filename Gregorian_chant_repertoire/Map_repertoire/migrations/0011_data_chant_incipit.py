# Generated by Django 5.0 on 2024-02-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map_repertoire', '0010_rename_provenance_name_sources_provenance'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_chant',
            name='incipit',
            field=models.CharField(max_length=500, null=True, verbose_name='incipit'),
        ),
    ]
