# Generated by Django 2.0.4 on 2018-07-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('opening_time', models.DateTimeField()),
                ('closing_time', models.DateTimeField()),
            ],
        ),
    ]
