# Generated by Django 5.0.4 on 2024-05-29 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]