# Generated by Django 3.2.2 on 2021-05-12 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_cldr_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docu',
            options={'managed': False, 'verbose_name_plural': 'DOCU'},
        ),
        migrations.AlterModelOptions(
            name='pd',
            options={'managed': False, 'verbose_name_plural': 'PD'},
        ),
        migrations.AlterModelOptions(
            name='pins',
            options={'managed': False, 'verbose_name_plural': 'PINS'},
        ),
        migrations.AlterModelOptions(
            name='run',
            options={'managed': False, 'verbose_name_plural': 'RUN'},
        ),
        migrations.AlterModelOptions(
            name='zm',
            options={'managed': False, 'verbose_name_plural': 'ZM'},
        ),
        migrations.AlterModelOptions(
            name='zuo',
            options={'managed': False, 'verbose_name_plural': 'ZUO'},
        ),
    ]
