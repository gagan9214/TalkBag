# Generated by Django 5.0.6 on 2024-07-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0003_alter_talk_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
    ]
