# Generated by Django 4.1.1 on 2022-09-08 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_portal', '0009_alter_userprofile_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='infoUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latest_update', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]