# Generated by Django 3.2.12 on 2022-06-11 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='userimag',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='UserProfileuploads/'),
            preserve_default=False,
        ),
    ]
