# Generated by Django 4.2.5 on 2024-09-01 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_sponsor_sponsorship'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsletterSubscription',
            new_name='Subscriber',
        ),
    ]
