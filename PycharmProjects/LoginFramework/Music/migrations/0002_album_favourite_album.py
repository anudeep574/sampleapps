# Generated by Django 2.0.6 on 2018-06-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='favourite_album',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
