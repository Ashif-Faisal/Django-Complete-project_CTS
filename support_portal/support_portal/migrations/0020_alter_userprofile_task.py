# Generated by Django 4.1.1 on 2022-09-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_portal', '0019_remove_userprofile_checker_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='task',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
