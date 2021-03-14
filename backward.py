# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:09:00 2021

@author: MAJESTY
"""

suggestion_to_users = None

symptoms1 = "meriang"
symptoms2 = "sesak napas"

symptoms_data = [{"value1": "sakit kepala", "value2": "suhu tubuh meningkat", "result": "demam"}, {"value1": "meriang", "value2": "sesak napas", "result": "infeksi_virus_corona"}, {"value1": "detak jantung melemah", "value2": "tekanan darah menurun", "result": "hipotermia"}]
suggestions = [{"demam": "banyak istirahat dan minum obat"}, {"infeksi_virus_corona": "vaksinasi dan perkuat sistem imun"}, {"hipotermia": "jaga suhu tubuh tetap normal"}]

  # C => D
for suggestions_data in suggestions:
  for key, value in suggestions_data.items():
    # A & B => C
    for data_symptoms in symptoms_data:
      if data_symptoms["result"] == key:
        if (symptoms1 == data_symptoms["value1"] or symptoms1 == data_symptoms["value2"]) and (symptoms2 == data_symptoms["value1"] or symptoms2 == data_symptoms["value2"]):
          suggestion_to_users = value

if suggestion_to_users:
  print(f"direkomendasikan untuk {suggestion_to_users}")
else:
  print("result suggestion to user is not found...")