# Generated by Django 3.1.6 on 2021-03-24 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_metaproduct_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metaproduct',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
