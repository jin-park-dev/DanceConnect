# Generated by Django 2.0 on 2017-12-27 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20171227_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
            preserve_default=False,
        ),
    ]
