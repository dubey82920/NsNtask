# Generated by Django 4.1.3 on 2023-02-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NsN', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='work_type',
            field=models.CharField(choices=[('YT', 'Youtube'), ('IG', 'Instagram'), ('OT', 'Other')], max_length=10),
        ),
    ]