# Generated by Django 4.2.6 on 2023-10-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataUpdated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('year', models.TextField()),
                ('abstract', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
    ]
