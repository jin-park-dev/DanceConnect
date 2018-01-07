# Generated by Django 2.0.1 on 2018-01-05 09:28

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20180105_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=profiles.models.OverwriteStorage(), upload_to='profile_list'),
        ),
    ]
