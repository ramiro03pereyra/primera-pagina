# Generated by Django 5.2.4 on 2025-07-08 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('productos', models.ManyToManyField(to='productos.producto')),
            ],
        ),
    ]
