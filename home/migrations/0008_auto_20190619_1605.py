# Generated by Django 2.2.2 on 2019-06-19 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190619_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_author',
            new_name='author',
        ),
    ]
