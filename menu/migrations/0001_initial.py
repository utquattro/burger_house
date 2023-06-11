# Generated by Django 4.2.1 on 2023-06-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('weight', models.IntegerField(blank=True)),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(blank=True)),
                ('photo_url', models.TextField(blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(blank=True, default=True)),
            ],
        ),
    ]
