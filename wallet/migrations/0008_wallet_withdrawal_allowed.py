# Generated by Django 3.0.5 on 2022-03-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0007_auto_20220312_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='withdrawal_allowed',
            field=models.BooleanField(default=False),
        ),
    ]