# Generated by Django 3.2 on 2023-02-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_productreview_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='non',
            new_name='nom',
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(upload_to='brand', verbose_name='Image'),
        ),
    ]
