# Generated by Django 4.1.7 on 2023-04-11 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robot_puanlari', '0005_alter_robot_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='robot',
            options={'ordering': ['-score', 'time']},
        ),
    ]