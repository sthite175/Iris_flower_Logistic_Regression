import pandas as pd
import numpy as np
import pickle
import config

with open(config.model_file_path,"rb") as file:
    model=pickle.load(file)

def predict_species(data):
    sepalL=float(data['sepalL'])
    sepalW=float(data['sepalW'])
    petalL=float(data['petalL'])
    petalW=float(data['petalW'])

    predict_input=np.array([sepalL,sepalW,petalL,petalW])
    predict_output=model.predict([predict_input])
    species=predict_output[0]

    if species==0:
        species="Iris Setosa"
    elif species==1:
        species="Iris Versicolour"
    elif species==2:
        species="Iris Verginica"
    
    return species




