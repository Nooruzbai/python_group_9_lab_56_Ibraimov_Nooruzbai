# Generated by Django 4.0.1 on 2022-01-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.TextField(choices=[('other', 'Other'), ('grocery', 'Grocery'), ('cleaning_supplies', 'Cleaning Supplies'), ('stationary', 'Stationary'), ('butchers', 'Butchers')], default=('other', 'Other'), verbose_name='Category'),
        ),
    ]