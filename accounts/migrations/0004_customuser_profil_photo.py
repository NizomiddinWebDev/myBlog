# Generated by Django 3.2.7 on 2021-10-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_customuser_profil_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profil_photo',
            field=models.ImageField(blank=True, upload_to='profilPhoto/'),
        ),
    ]
