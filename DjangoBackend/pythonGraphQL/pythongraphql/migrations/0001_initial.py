# Generated by Django 3.0.7 on 2020-06-19 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('email', models.TextField()),
                ('dateCreated', models.DateTimeField()),
                ('dateOfBirth', models.DateField()),
            ],
        ),
    ]