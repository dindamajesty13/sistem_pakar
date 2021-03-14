# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:05:01 2021

@author: MAJESTY
"""

suggestion_to_users = None

symptoms1 = "meriang"
symptoms2 = "sesak napas"

symptoms_data = [{"value1": "sakit kepala", "value2": "suhu tubuh meningkat", "result": "demam"}, {"value1": "meriang", "value2": "sesak napas", "result": "infeksi virus corona"}, {"value1": "detak jantung melemah", "value2": "tekanan darah menurun", "result": "hipotermia"}]
suggestions = [{"demam": "banyak istirahat dan minum obat"}, {"infeksi virus corona": "vaksinasi dan perkuat sistem imun"}, {"hipotermia": "jaga suhu tubuh tetap normal"}]

symptoms_identifier = None
for data_symptoms in symptoms_data:
  if (symptoms1 == data_symptoms["value1"] or symptoms1 == data_symptoms["value2"]) and (symptoms2 == data_symptoms["value1"] or symptoms2 == data_symptoms["value2"]):
    symptoms_identifier = data_symptoms["result"]
    break

if symptoms_identifier:
  print(symptoms_identifier)
else:
  print("result symproms is not found..")
  
for data_suggestions in suggestions:
  for key, value in data_suggestions.items():
    if key == symptoms_identifier:
      suggestion_to_users = data_suggestions[symptoms_identifier]
      break
  
if suggestion_to_users:
  print(f"direkomendasikan untuk {suggestion_to_users}")
else:
  print("result suggestion to user is not found...")
  
  