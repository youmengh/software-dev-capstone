# Generated by Django 4.1.7 on 2023-04-12 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_object'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentinfo',
            name='card_number',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='paymentinfo',
            name='cvv',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='paymentinfo',
            name='expiration_date',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
