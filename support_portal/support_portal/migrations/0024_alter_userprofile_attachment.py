# Generated by Django 4.1.1 on 2022-09-27 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_portal', '0023_alter_userprofile_attachment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='attachment',
            field=models.FileField(max_length=200, null=True, upload_to='media'),
        ),
    ]
