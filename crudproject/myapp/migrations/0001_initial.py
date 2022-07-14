# Generated by Django 3.2 on 2022-07-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.FloatField()),
                ('address', models.TextField()),
            ],
        ),
    ]