# Generated by Django 2.2.2 on 2019-06-20 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='ID',
            new_name='member_id',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='name',
            new_name='member_name',
        ),
    ]
