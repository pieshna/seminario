# Generated by Django 3.2.7 on 2021-09-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caravanamigrante',
            fields=[
                ('id_persona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=120)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=1)),
                ('edad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'caravanamigrante',
                'verbose_name_plural': 'caravanasmigrantes',
                'db_table': 'caravanamigrante',
                'managed': False,
            },
        ),
    ]
