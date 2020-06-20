from django.db import models

# Create your models here.

class PostModel(models.Model):
    Nama = models.CharField(max_length=128, unique=True)
    Alamat = models.CharField(max_length=128, unique=True)
    Pekerjaan = models.CharField(max_length=128, unique=True)
    No_Telepon = models.CharField(max_length=20, unique=True)
    Email = models.EmailField(max_length=254, help_text="*Email Harus Aktif", unique=True)
    Merasa_Lelah_Berlebihan = models.CharField(max_length=128)
    Badan_Terasa_Sakit = models.CharField(max_length=128)
    Demam_Dengan_Intensitas_Ringan_Hingga_Berat  = models.CharField(max_length=128)
    Badan_Mengggigil = models.CharField(max_length=128)
    Radang_Tenggorokan = models.CharField(max_length=128)
    Sakit_Kepala = models.CharField(max_length=128)
    Hidung_Tersumbat = models.CharField(max_length=128)
    Batuk_Berdahak = models.CharField(max_length=128)
    Batuk_Darah = models.CharField(max_length=128)
    Berkeringat_Pada_Malam_Hari = models.CharField(max_length=128)
    Kehilangan_Nafsu_Makan = models.CharField(max_length=128)
    Berat_Badan_Yang_Turun_Tanpa_Sebab = models.CharField(max_length=128)
    Pembesaran_Kelenjar_Getah_Bening_Di_Leher = models.CharField(max_length=128)
    Batuk = models.CharField(max_length=128)
    Nafas_Berbunyi = models.CharField(max_length=128)
    Sesak_Nafas = models.CharField(max_length=128)
    Dada_Sesak = models.CharField(max_length=128)
    Suara_Sengau = models.CharField(max_length=128)
    Nafas_Tersedu_Sedu = models.CharField(max_length=128)
    Diare = models.CharField(max_length=128)
    Mual = models.CharField(max_length=128)
    Penurunan_Kesadaran = models.CharField(max_length=128)
    Nyeri_Ketika_Batuk  = models.CharField(max_length=128)

    def __str__(self):
        return "{}. {}".format(self.id, self.Email)