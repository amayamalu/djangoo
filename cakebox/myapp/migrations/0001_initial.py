# Generated by Django 4.1.7 on 2023-03-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('flavour', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField()),
                ('shape', models.CharField(max_length=250)),
                ('weight', models.IntegerField()),
                ('layer', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=2550)),
            ],
        ),
    ]
