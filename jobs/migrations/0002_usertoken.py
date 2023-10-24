# Generated by Django 4.2.6 on 2023-10-24 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=2000)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('exp_date', models.DateTimeField()),
            ],
        ),
    ]