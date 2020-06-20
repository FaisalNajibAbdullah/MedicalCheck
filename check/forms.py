from django import forms
from captcha.fields import CaptchaField
from .models import PostModel

test_pilih= [
    ('1','Ya'),
    ('0','Tidak')
    ]

class PostForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = PostModel
        widgets = {
        'Nama' : forms.TextInput(attrs={'placeholder': 'Nama Lengkap'}),
        'Alamat' : forms.TextInput(attrs={'placeholder': 'Alamat Lengkap'}),
        'Pekerjaan': forms.TextInput(attrs={'placeholder': 'Pekerjaan'}),
        'No_Telepon' : forms.TextInput(attrs={'placeholder': 'Nomor Telepon Anda'}),
        'Email' : forms.TextInput(attrs={'placeholder': 'Email harus Valid dan Benar e.g email_anda@example.com'}),
        'Merasa_Lelah_Berlebihan' : forms.Select(choices=test_pilih),
        'Badan_Terasa_Sakit' : forms.Select(choices=test_pilih),
        'Demam_Dengan_Intensitas_Ringan_Hingga_Berat' : forms.Select(choices=test_pilih),
        'Badan_Mengggigil' : forms.Select(choices=test_pilih),
        'Radang_Tenggorokan' : forms.Select(choices=test_pilih),
        'Sakit_Kepala' : forms.Select(choices=test_pilih),
        'Hidung_Tersumbat' : forms.Select(choices=test_pilih),
        'Batuk_Berdahak' : forms.Select(choices=test_pilih),
        'Batuk_Darah' : forms.Select(choices=test_pilih),
        'Berkeringat_Pada_Malam_Hari' : forms.Select(choices=test_pilih),
        'Kehilangan_Nafsu_Makan' : forms.Select(choices=test_pilih),
        'Berat_Badan_Yang_Turun_Tanpa_Sebab' : forms.Select(choices=test_pilih),
        'Pembesaran_Kelenjar_Getah_Bening_Di_Leher' : forms.Select(choices=test_pilih),
        'Batuk' : forms.Select(choices=test_pilih),
        'Nafas_Berbunyi' : forms.Select(choices=test_pilih),
        'Sesak_Nafas' : forms.Select(choices=test_pilih),
        'Dada_Sesak' : forms.Select(choices=test_pilih),
        'Suara_Sengau' : forms.Select(choices=test_pilih),
        'Nafas_Tersedu_Sedu' : forms.Select(choices=test_pilih),
        'Diare' : forms.Select(choices=test_pilih),
        'Mual' : forms.Select(choices=test_pilih), 
        'Penurunan_Kesadaran' : forms.Select(choices=test_pilih),
        'Nyeri_Ketika_Batuk' : forms.Select(choices=test_pilih),
        } 
        
        fields = '__all__'
