# Generated by Django 4.1.7 on 2023-04-12 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_paymentinfo_card_number_alter_paymentinfo_cvv_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentinfo',
            old_name='cvv',
            new_name='CVV',
        ),
    ]