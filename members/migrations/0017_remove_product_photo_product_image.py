# Generated by Django 4.1.6 on 2023-02-13 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0016_remove_product_link_photo_product_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='photos/%y/%m/%d'),
        ),
    ]
