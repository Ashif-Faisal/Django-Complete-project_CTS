# Generated by Django 4.1.1 on 2022-09-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_portal', '0013_alter_userprofile_etd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='urgent_yn',
            field=models.BooleanField(max_length=30, null=True),
        ),
    ]
