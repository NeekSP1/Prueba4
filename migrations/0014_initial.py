# Generated by Django 4.0.4 on 2022-06-23 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0013_delete_comprar_delete_contacto_delete_producto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comprar',
            fields=[
                ('Boleta', models.IntegerField(primary_key=True, serialize=False, verbose_name='Boleta')),
                ('Producto', models.CharField(max_length=20, verbose_name='Producto')),
                ('Cantidad', models.CharField(max_length=20, verbose_name='Cantidad')),
                ('Tipotarjeta', models.CharField(max_length=100, verbose_name='Tipotarjeta')),
                ('Numerotarjeta', models.CharField(max_length=100, verbose_name='Numerotarjeta')),
                ('Fecha_expira', models.CharField(max_length=100, verbose_name='Fecha_expira')),
                ('Cvv', models.CharField(max_length=100, verbose_name='CVV')),
                ('Direccion', models.CharField(max_length=100, verbose_name='Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('Nombre', models.CharField(max_length=10, verbose_name='Nombre')),
                ('Rut', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Rut')),
                ('Apellido', models.CharField(max_length=10, verbose_name='Apellido')),
                ('Email', models.CharField(max_length=20, verbose_name='E-mail')),
                ('Asunto', models.CharField(max_length=9, verbose_name='Asunto')),
                ('Asunto2', models.CharField(max_length=20, verbose_name='Asunto2')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('Stock', models.CharField(max_length=20, verbose_name='Stock')),
                ('Precio', models.CharField(max_length=20, verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='Registroo',
            fields=[
                ('Nombre', models.CharField(max_length=6, verbose_name='Nombre')),
                ('Rut', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Rut')),
                ('Edad', models.CharField(max_length=2, verbose_name='Edad')),
                ('Email', models.CharField(max_length=20, verbose_name='E-mail')),
                ('Telefono', models.CharField(max_length=9, verbose_name='Telefono')),
                ('Contrase??a', models.CharField(max_length=20, verbose_name='Contrase??a')),
            ],
        ),
    ]
