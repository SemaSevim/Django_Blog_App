# Generated by Django 4.0.6 on 2022-08-08 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anketler', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soru',
            old_name='ayim_tarihi',
            new_name='yayim_tarihi',
        ),
    ]
