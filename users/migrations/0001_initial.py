# Generated by Django 3.0.5 on 2021-06-22 18:34

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('bio', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Рассказ о себе')),
                ('role', models.CharField(choices=[('user', 'User'), ('moderator', 'Moderator'), ('admin', 'Admin')], default='user', max_length=15, verbose_name='Роль')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('confirmation_code', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'customuser',
                'verbose_name_plural': 'users',
                'db_table': 'users_customuser',
                'ordering': ('-pk',),
                'abstract': False,
            },
        ),
    ]
