# Generated by Django 2.1.4 on 2020-10-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_profile_foto_receita'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='foto_receita',
            new_name='foto',
        ),
        migrations.AddField(
            model_name='profile',
            name='aniversario',
            field=models.DateField(default='2020-10-10'),
            preserve_default=False,
        ),
    ]