# Generated by Django 2.1.4 on 2020-10-25 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rifas', '0012_auto_20201025_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='rifa',
            name='e_ganhador',
            field=models.BooleanField(default='False'),
            preserve_default=False,
        ),
    ]
