# Generated by Django 3.0.5 on 2021-06-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210618_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='confirmation_code',
            field=models.CharField(blank=True, default='xymoocauxy', max_length=10, null=True, verbose_name='Код подтверждения'),
        ),
    ]
