# Generated by Django 3.2.9 on 2022-02-07 09:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0017_alter_review_ondate'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('stripe_customer_id', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='ondate',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 7, 14, 57, 56, 620052), verbose_name=datetime.datetime),
        ),
    ]
