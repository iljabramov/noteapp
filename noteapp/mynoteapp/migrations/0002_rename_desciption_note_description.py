# Generated by Django 4.0.3 on 2022-03-20 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mynoteapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='desciption',
            new_name='description',
        ),
    ]