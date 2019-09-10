# Generated by Django 2.2.4 on 2019-09-09 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('identificador', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('definicion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
