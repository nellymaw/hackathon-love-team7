# Generated by Django 3.2 on 2022-02-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottles', '0004_alter_reply_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='has_unseen_reply',
            field=models.BooleanField(default=False),
        ),
    ]
