import os
from django.core.cache import cache
import pickle

#def detect_medical(string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string,string):
def detect_medical(Nyeri_Ketika_Batuk):

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

	prediction = model.predict([Nyeri_Ketika_Batuk])
	return penyakits[prediction[0]]

