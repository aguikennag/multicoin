# Generated by Django 3.0.5 on 2022-06-25 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20220625_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='kyc', to=settings.AUTH_USER_MODEL),
        ),
    ]
