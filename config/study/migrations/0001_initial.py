# Generated by Django 3.2.15 on 2022-09-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('school', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=20)),
            ],
        ),
    ]