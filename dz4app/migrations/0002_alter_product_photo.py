# Generated by Django 5.0.3 on 2024-03-21 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dz4app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
