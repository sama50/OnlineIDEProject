# Generated by Django 3.2.12 on 2022-06-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userprofile_userimag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userimag',
            field=models.ImageField(blank=True, null=True, upload_to='UserProfileuploads/'),
        ),
    ]
