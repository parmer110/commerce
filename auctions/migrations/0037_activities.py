# Generated by Django 4.1.5 on 2023-03-01 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0036_alter_bids_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bidUpdate', models.DateTimeField(blank=True, null=True)),
                ('closeUpdate', models.DateTimeField(blank=True, null=True)),
                ('commentUpdate', models.DateTimeField(blank=True, null=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='logComment', to='auctions.comment')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logListing', to='auctions.auctionlisting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='logUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]