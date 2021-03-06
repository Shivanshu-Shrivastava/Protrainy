# Generated by Django 3.1.7 on 2021-02-27 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('dateob', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('github', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
            ],
        ),
    ]
