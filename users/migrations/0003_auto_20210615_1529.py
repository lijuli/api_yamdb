# Generated by Django 3.0.5 on 2021-06-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210615_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='confirmation_code',
            field=models.CharField(default='jrvqjkjgtx', max_length=10, verbose_name='Код подтверждения'),
        ),
    ]
