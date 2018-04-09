# Generated by Django 2.0.3 on 2018-04-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('cell', models.CharField(max_length=20, verbose_name='Cell')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('dob', models.DateField(verbose_name='Date Of Birth')),
            ],
        ),
    ]
