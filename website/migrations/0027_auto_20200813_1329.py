# Generated by Django 3.0.5 on 2020-08-13 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20200810_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='date_created',
            new_name='dateCreated',
        ),
    ]
