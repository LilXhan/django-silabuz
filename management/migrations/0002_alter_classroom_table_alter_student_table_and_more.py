# Generated by Django 4.1.4 on 2022-12-07 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='classroom',
            table='classrooms',
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
        migrations.AlterModelTable(
            name='teacher',
            table='teachers',
        ),
    ]