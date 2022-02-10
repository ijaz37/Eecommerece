# Generated by Django 4.0.2 on 2022-02-08 15:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0019_alter_payment_csc_alter_review_ondate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ondate',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 8, 20, 25, 24, 914742), verbose_name=datetime.datetime),
        ),
        migrations.CreateModel(
            name='ShopingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_order', models.BooleanField(default=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('items', models.ManyToManyField(to='main.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
