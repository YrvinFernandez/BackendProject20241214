# Generated by Django 5.1.4 on 2024-12-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productosmodel',
            name='imagen',
            field=models.ImageField(upload_to='imagen'),
        ),
    ]
