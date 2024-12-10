# Generated by Django 4.2.6 on 2024-12-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_malipoyafainicopies_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JumbeZaWateja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JinaKamiliLaMteja', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina La Mteja')),
                ('SimuYaMteja', models.IntegerField(blank=True, null=True, verbose_name='Simu Ya Mteja')),
                ('EmailYaMteja', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email Ya Mteja')),
                ('Message', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Ujumbe')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Jumbe Za Wateja',
            },
        ),
    ]
