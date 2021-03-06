# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-18 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama', models.CharField(max_length=128, unique=True)),
                ('Alamat', models.CharField(max_length=128, unique=True)),
                ('Pekerjaan', models.CharField(max_length=128, unique=True)),
                ('No_Telepon', models.CharField(max_length=20, unique=True)),
                ('Email', models.EmailField(help_text='*Email Harus Aktif', max_length=254, unique=True)),
                ('Keluhan', models.CharField(max_length=128)),
                ('Durasi_Keluhan', models.CharField(max_length=128)),
                ('Merasa_Lelah_Berlebihan', models.CharField(max_length=128)),
                ('Badan_Terasa_Sakit', models.CharField(max_length=128)),
                ('Demam_Dengan_Intensitas_Ringan_Hingga_Berat', models.CharField(max_length=128)),
                ('Badan_Mengggigil', models.CharField(max_length=128)),
                ('Radang_Tenggorokan', models.CharField(max_length=128)),
                ('Sakit_Kepala', models.CharField(max_length=128)),
                ('Batuk_Berdahak', models.CharField(max_length=128)),
                ('Batuk_Darah', models.CharField(max_length=128)),
                ('Berkeringat_Pada_Malam_Hari', models.CharField(max_length=128)),
                ('Kehilangan_Nafsu_Makan', models.CharField(max_length=128)),
                ('Berat_Badan_Yang_Turun_Tanpa_Sebab', models.CharField(max_length=128)),
                ('Pembesaran_Kelenjar_Getah_Bening_Di_Leher', models.CharField(max_length=128)),
                ('Batuk', models.CharField(max_length=128)),
                ('Sesak_Nafas', models.CharField(max_length=128)),
                ('Dada_Sesak', models.CharField(max_length=128)),
                ('Suara_Sengau', models.CharField(max_length=128)),
                ('Diare', models.CharField(max_length=128)),
                ('Mual', models.CharField(max_length=128)),
                ('Nyeri_Ketika_Batuk', models.CharField(max_length=128)),
                ('Tambahan', models.CharField(blank=True, help_text='*Ini tidak wajib di-isi', max_length=128)),
            ],
        ),
    ]
