# Generated by Django 3.0.6 on 2020-06-30 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_order',
            name='vendor',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.DO_NOTHING, to='product.Vendor'),
        ),
    ]
