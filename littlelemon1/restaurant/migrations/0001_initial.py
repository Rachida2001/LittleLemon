# Generated by Django 4.2.4 on 2024-01-21 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('No_of_guests', models.IntegerField()),
                ('BookingDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Inventory', models.IntegerField()),
            ],
        ),
    ]
