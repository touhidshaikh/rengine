# Generated by Django 3.2.4 on 2021-12-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0006_installedexternaltool_is_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='installedexternaltool',
            name='is_subdomain_gathering',
            field=models.BooleanField(default=False),
        ),
    ]