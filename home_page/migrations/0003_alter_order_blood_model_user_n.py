# Generated by Django 4.0.1 on 2022-06-03 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_page', '0002_remove_order_blood_model_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_blood_model',
            name='user_n',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
