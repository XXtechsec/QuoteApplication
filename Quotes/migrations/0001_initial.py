# Generated by Django 2.1 on 2019-07-03 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceType', models.TextField()),
                ('Type', models.TextField()),
                ('Quality', models.TextField()),
                ('SKU', models.TextField()),
                ('Description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
