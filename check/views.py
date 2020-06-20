from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .forms import PostForm
from .models import PostModel
from .medical_check import detect_medical

def index(request):
	posts = PostModel.objects.all()
	context = {
		'page_title':'List Post',
		'posts':posts,
	}


	return render(request,'check/index.html',context)

def create(request):
	post_form = PostForm()
	penyakit = None

	if post_form.is_valid():
		print("udin")
		penyakit = detect_medical(form.data[['Merasa_Lelah_Berlebihan','Badan_Terasa_Sakit','Demam_Dengan_Intensitas_Ringan_Hingga_Berat', 
    		'Badan_Mengggigil','Radang_Tenggorokan','Sakit_Kepala','Hidung_Tersumbat','Batuk_Berdahak','Batuk_Darah','Berkeringat_Pada_Malam_Hari',
    		'Kehilangan_Nafsu_Makan','Berat_Badan_Yang_Turun_Tanpa_Sebab','Pembesaran_Kelenjar_Getah_Bening_Di_Leher','Batuk','Nafas_Berbunyi',
    		'Sesak_Nafas','Dada_Sesak','Suara_Sengau','Nafas_Tersedu_Sedu','Diare','Mual','Penurunan_Kesadaran','Nyeri_Ketika_Batuk']])
	else:
		print("adin")
		penyakit = detect_medical(post_form.data['Nyeri_Ketika_Batuk'])
	context = {
		'page_title':'Create Post',
		'post_form':post_form,
		'penyakit':penyakit
	}

	return render(request, 'check/create.html',context)
"""
	if post_form.is_valid():
		print("najibbbbb")
		penyakit = detect_medical(post_form.data[['Merasa_Lelah_Berlebihan','Badan_Terasa_Sakit','Demam_Dengan_Intensitas_Ringan_Hingga_Berat', 
    		'Badan_Mengggigil','Radang_Tenggorokan','Sakit_Kepala','Hidung_Tersumbat','Batuk_Berdahak','Batuk_Darah','Berkeringat_Pada_Malam_Hari',
    		'Kehilangan_Nafsu_Makan','Berat_Badan_Yang_Turun_Tanpa_Sebab','Pembesaran_Kelenjar_Getah_Bening_Di_Leher','Batuk','Nafas_Berbunyi',
    		'Sesak_Nafas','Dada_Sesak','Suara_Sengau','Nafas_Tersedu_Sedu','Diare','Mual','Penurunan_Kesadaran','Nyeri_Ketika_Batuk']])
    print(penyakit)

	if request.method == "POST":
		PostModel.objects.create(
			Nama	= request.POST['Nama'],
			Alamat 	= request.POST['Alamat'],
			Pekerjaan = request.POST['Pekerjaan'],
			No_Telepon = request.POST['No_Telepon'],
			Email = request.POST['Email'],
			Merasa_Lelah_Berlebihan = request.POST['Merasa_Lelah_Berlebihan'],
			Badan_Terasa_Sakit = request.POST['Badan_Terasa_Sakit'],
			Demam_Dengan_Intensitas_Ringan_Hingga_Berat = request.POST['Demam_Dengan_Intensitas_Ringan_Hingga_Berat'],
			Badan_Mengggigil = request.POST['Badan_Mengggigil'],
			Radang_Tenggorokan = request.POST['Radang_Tenggorokan'],
			Sakit_Kepala = request.POST['Sakit_Kepala'],
			Hidung_Tersumbat = request.POST['Hidung_Tersumbat'],
			Batuk_Berdahak = request.POST['Batuk_Berdahak'],
			Batuk_Darah = request.POST['Batuk_Darah'],
			Berkeringat_Pada_Malam_Hari = request.POST['Berkeringat_Pada_Malam_Hari'],
			Kehilangan_Nafsu_Makan = request.POST['Kehilangan_Nafsu_Makan'],
			Berat_Badan_Yang_Turun_Tanpa_Sebab = request.POST['Berat_Badan_Yang_Turun_Tanpa_Sebab'],
			Pembesaran_Kelenjar_Getah_Bening_Di_Leher = request.POST['Pembesaran_Kelenjar_Getah_Bening_Di_Leher'],
			Batuk = request.POST['Batuk'],
			Nafas_Berbunyi = request.POST['Nafas_Berbunyi'],
			Sesak_Nafas = request.POST['Sesak_Nafas'],
			Dada_Sesak = request.POST['Dada_Sesak'],
			Suara_Sengau = request.POST['Suara_Sengau'],
			Nafas_Tersedu_Sedu = request.POST['Nafas_Tersedu_Sedu'],
			Diare = request.POST['Diare'],
			Mual = request.POST['Mual'],
			Penurunan_Kesadaran = request.POST['Penurunan_Kesadaran'],
			Nyeri_Ketika_Batuk = request.POST['Nyeri_Ketika_Batuk'],
			)

        return HttpResponseRedirect("/check")
"""
	