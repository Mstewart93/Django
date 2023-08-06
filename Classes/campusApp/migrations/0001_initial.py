# Generated by Django 4.2.4 on 2023-08-06 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, default='', max_length=60)),
                ('State', models.CharField(blank=True, default='', max_length=2)),
                ('Campus_ID', models.IntegerField(blank=True, default='')),
            ],
        ),
    ]