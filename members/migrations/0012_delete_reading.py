# Generated by Django 4.1.5 on 2023-02-13 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_remove_book_price_book_link_download'),
    ]

    operations = [
        migrations.DeleteModel(
            name='reading',
        ),
    ]
