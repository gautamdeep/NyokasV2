# Generated by Django 3.0.6 on 2020-07-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200702_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
