# Generated by Django 3.1.4 on 2020-12-20 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_orderitem_item_variations'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image3',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
