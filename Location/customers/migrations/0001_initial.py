# Generated by Django 3.0 on 2022-05-17 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenoms', models.CharField(max_length=100)),
                ('sexe', models.CharField(max_length=15)),
                ('profession', models.CharField(max_length=150)),
                ('credible', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('couleur', models.CharField(max_length=50)),
                ('annee', models.IntegerField()),
                ('porte', models.IntegerField()),
                ('climatiser', models.CharField(max_length=5)),
                ('energie', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Client')),
                ('voiture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Voiture')),
            ],
        ),
    ]