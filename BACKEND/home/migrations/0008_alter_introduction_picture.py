# Generated by Django 4.1.1 on 2022-10-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_homecarousel_introduction_delete_homeservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introduction',
            name='Picture',
            field=models.ImageField(upload_to='imagies/pictures'),
        ),
    ]
