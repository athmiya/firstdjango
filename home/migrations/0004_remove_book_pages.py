# Generated by Django 2.2.2 on 2019-06-19 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_book_pages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pages',
        ),
    ]