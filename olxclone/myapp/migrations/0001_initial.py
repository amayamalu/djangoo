# Generated by Django 4.1.7 on 2023-03-15 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
                ('owner_type', models.CharField(max_length=250)),
                ('fuel_type', models.CharField(max_length=250)),
                ('kms', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField()),
                ('number', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=2550)),
            ],
        ),
    ]
