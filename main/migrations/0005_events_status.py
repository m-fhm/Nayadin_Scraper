# Generated by Django 3.2.3 on 2021-05-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
