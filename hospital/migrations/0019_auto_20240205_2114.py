# Generated by Django 3.0.5 on 2024-02-05 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Psychotherapist', 'Psychotherapist'), ('Neuropsychologist', 'Neuropsychologist'), ('Psychologist', 'Psychologist')], default='Psychologist', max_length=50),
        ),
    ]
