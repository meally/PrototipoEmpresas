# Generated by Django 3.2 on 2021-05-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importcsv', '0006_alter_producto_recogido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='recogido',
            field=models.IntegerField(default=0),
        ),
    ]
