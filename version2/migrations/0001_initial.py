# Generated by Django 4.1.4 on 2022-12-29 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=250)),
                ('Logo', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'services',
            },
        ),
        migrations.CreateModel(
            name='Payment_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.FloatField(default=0.0)),
                ('PaymentDate', models.DateField(auto_now_add=True)),
                ('ExpirationDate', models.DateField(auto_now_add=True)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='version2.services')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userss', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expired_payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Penalty_fee_amount', models.FloatField(default=0.0)),
                ('Payment_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='version2.payment_user')),
            ],
        ),
    ]
