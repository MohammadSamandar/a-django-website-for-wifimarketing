# Generated by Django 4.1.3 on 2023-04-16 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('Businesses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCustomer',
            fields=[
                ('siteuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('otp', models.PositiveIntegerField(blank=True, null=True)),
                ('otp_create_time', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='Businesses.business')),
            ],
            options={
                'verbose_name': 'مشتری کسب و کار',
                'verbose_name_plural': 'مشتریان کسب و کارها',
            },
            bases=('users.siteuser',),
        ),
    ]
