# Generated by Django 2.2.3 on 2019-07-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('towncrierapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
