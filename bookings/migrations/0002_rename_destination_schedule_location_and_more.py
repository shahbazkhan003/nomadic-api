# Generated by Django 5.2.2 on 2025-06-10 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='destination',
            new_name='location',
        ),
        migrations.AddField(
            model_name='schedule',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='schedule',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
