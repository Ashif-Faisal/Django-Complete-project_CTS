# Generated by Django 4.1.1 on 2022-09-11 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_portal', '0010_infoupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoupdate',
            name='task_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
