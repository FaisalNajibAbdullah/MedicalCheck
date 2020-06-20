import os
from django.core.cache import cache
import pickle

#def detect_medical(string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string):
def detect_medical(Merasa_Lelah_Berlebihan,Badan_Terasa_Sakit,Demam_Dengan_Intensitas_Ringan_Hingga_Berat,Badan_Mengggigil,
	Radang_Tenggorokan,Sakit_Kepala,Hidung_Tersumbat,Batuk_Berdahak,Batuk_Darah,Berkeringat_Pada_Malam_Hari,Kehilangan_Nafsu_Makan,
	Berat_Badan_Yang_Turun_Tanpa_Sebab,Pembesaran_Kelenjar_Getah_Bening_Di_Leher,Batuk,Nafas_Berbunyi,Sesak_Nafas,Dada_Sesak,
	Suara_Sengau,Nafas_Tersedu_Sedu,Diare,Mual,Penurunan_Kesadaran,Nyeri_Ketika_Batuk):

	penyakits = [
		'Flu',
		'TBC',
		'Asma',
		'Bronkitis'
	]

	model_cache_key = 'model_cache'
	model_rel_path = "check/MedicalCheck_Model/model_cache/model.pkl"

	model = cache.get(model_cache_key)

	if model is None:
		model_path = os.path.realpath(model_rel_path)
		model = pickle.load(model_path)
		#save di memori django
		cache.set(model_cache_key, model, None)

	prediction = model.predict([Merasa_Lelah_Berlebihan,Badan_Terasa_Sakit,Demam_Dengan_Intensitas_Ringan_Hingga_Berat,Badan_Mengggigil,
	Radang_Tenggorokan,Sakit_Kepala,Hidung_Tersumbat,Batuk_Berdahak,Batuk_Darah,Berkeringat_Pada_Malam_Hari,Kehilangan_Nafsu_Makan,
	Berat_Badan_Yang_Turun_Tanpa_Sebab,Pembesaran_Kelenjar_Getah_Bening_Di_Leher,Batuk,Nafas_Berbunyi,Sesak_Nafas,Dada_Sesak,
	Suara_Sengau,Nafas_Tersedu_Sedu,Diare,Mual,Penurunan_Kesadaran,Nyeri_Ketika_Batuk])
	return penyakits[prediction[0]]

