# Generated by Django 4.1.5 on 2023-02-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_auctionlisting_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='image',
            field=models.CharField(blank=True, max_length=16384),
        ),
    ]
