# Generated by Django 4.2.6 on 2023-10-25 04:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ts', models.DateTimeField(db_index=True)),
                ('receiving_station', models.CharField(db_index=True)),
                ('calling_station', models.CharField(db_index=True)),
                ('frequency', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mode', models.CharField(db_index=True)),
                ('snr_db', models.IntegerField()),
                ('wpm', models.IntegerField()),
                ('msg', models.CharField()),
                ('rbn_ts', models.DateTimeField(db_index=True)),
            ],
        ),
    ]
