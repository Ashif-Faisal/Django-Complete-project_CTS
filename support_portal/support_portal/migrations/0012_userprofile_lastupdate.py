# Generated by Django 4.1.1 on 2022-09-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_portal', '0011_infoupdate_task_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='lastupdate',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
