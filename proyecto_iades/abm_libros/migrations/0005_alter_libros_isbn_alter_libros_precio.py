# Generated by Django 5.1.3 on 2024-12-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abm_libros', '0004_remove_libros_isbn_libros_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='isbn',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='libros',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
