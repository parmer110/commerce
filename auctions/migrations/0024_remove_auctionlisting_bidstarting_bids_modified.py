# Generated by Django 4.1.5 on 2023-02-24 22:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_alter_auctionlisting_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='bidStarting',
        ),
        migrations.AddField(
            model_name='bids',
            name='modified',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 2, 24, 22, 53, 11, 317859, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
