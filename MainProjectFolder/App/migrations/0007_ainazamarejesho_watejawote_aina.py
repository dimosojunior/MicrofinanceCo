# Generated by Django 4.2.6 on 2024-12-21 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_watejawote_ainazamarejesho'),
    ]

    operations = [
        migrations.CreateModel(
            name='AinaZaMarejesho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aina', models.CharField(blank=True, max_length=500, null=True, verbose_name='Aina Ya Mpokeaji')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Aina Za Marejesho',
            },
        ),
        migrations.AddField(
            model_name='watejawote',
            name='Aina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='App.ainazamarejesho', verbose_name='Aina Ya Mpokeaji'),
        ),
    ]
