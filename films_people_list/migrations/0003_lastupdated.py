# Generated by Django 3.0.7 on 2020-08-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films_people_list', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastUpdated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
