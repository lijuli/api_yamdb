# Generated by Django 3.0.5 on 2021-06-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210616_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='confirmation_code',
            field=models.CharField(blank=True, default='szforrudxd', max_length=10, null=True, verbose_name='Код подтверждения'),
        ),
    ]
