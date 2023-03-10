# Generated by Django 3.2 on 2023-03-05 07:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_order_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Code')),
                ('value', models.FloatField(verbose_name='Valeur')),
                ('from_date', models.DateField(default=django.utils.timezone.now, verbose_name='Valide Du')),
                ('to_date', models.DateField(default=django.utils.timezone.now, verbose_name='Expiration ')),
                ('quantity', models.IntegerField(verbose_name='Quantité')),
                ('image', models.ImageField(upload_to='coupon/', verbose_name='Image')),
            ],
        ),
    ]
