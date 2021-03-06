# Generated by Django 3.0.6 on 2020-06-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyWorkReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, default='', max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('site_name', models.CharField(blank=True, default='', max_length=100)),
                ('representative', models.CharField(blank=True, default='', max_length=100)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('landmark', models.CharField(blank=True, default='', max_length=100)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('contact', models.CharField(blank=True, default='', max_length=100)),
                ('contact2', models.CharField(blank=True, default='', max_length=100)),
                ('service', models.CharField(blank=True, choices=[('Installation', 'Installation'), ('Service/Repair', 'Service/Repair'), ('', 'default')], default='', max_length=25)),
                ('problem', models.CharField(blank=True, default='', max_length=100)),
                ('assign_to', models.CharField(blank=True, default='', max_length=100)),
                ('service_report', models.CharField(blank=True, default='', max_length=100)),
                ('bill_no', models.CharField(blank=True, default='', max_length=100)),
                ('bill_amount', models.CharField(blank=True, default='', max_length=100)),
                ('bill_submit', models.CharField(blank=True, default='', max_length=100)),
                ('amount_received', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
