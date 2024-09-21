# Generated by Django 4.1.3 on 2024-09-21 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField()),
                ('mac_address', models.CharField(max_length=17)),
                ('manufacture_date', models.DateField()),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
