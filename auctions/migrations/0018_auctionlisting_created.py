# Generated by Django 4.1.5 on 2023-02-24 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auctionlisting_category_auctionlisting_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='created',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
