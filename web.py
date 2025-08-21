import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

st.set_page_config(page_title="prediction of disease Outbreaks",layout='wide',page_icon='doctor')

diabetes_model = pickle.load(open('saved_models/diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('saved_models/heart_model.sav','rb'))
parkinsons_disease_model = pickle.load(open('saved_models/parkinsons_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Prediction of Disease outbeaks system',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Disease Prediction'],menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
    st.title('DIABETES PREDICTION USING ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('No Of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
    with col2:
        Age = st.text_input('Age Of the Person')

    diab_diagnosis = ''
    if st.button('DiabetesTest Result'):
        user_input = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is Non-Diabetic'
        st.success(diab_diagnosis)

elif selected == 'Heart Disease Prediction':
    st.title("HEART DISEASE PREDICTION USING ML")
    col1,col2,col3 = st.columns(3);

    with col1:
        age = st.text_input("Age of the Person");
    with col2:
        sex = st.text_input("Gender of the Person")
    with col3:
        cp = st.text_input("Enter the Cp")
    with col1:
        trestbps = st.text_input("trestbps")
    with col2:
        chol =  st.text_input("chol")
    with col3:
        fbs = st.text_input("fbs")
    with col1:
        restecg = st.text_input("restecg") 
    with col2:
        thalach = st.text_input("THALACH");
    with col3:
        exang = st.text_input("exang");
    with col1:
        oldpeak = st.text_input("oldpeak");
    with col2:
        slope = st.text_input("slope")
    with col3:
        ca = st.text_input("ca");
    with col1:
        thal = st.text_input("thal");
    heart_diagnosis = ''
    if st.button('HEART TEST RESULT'):
        user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input = [float(x) for x in user_input]
        user_input = np.array(user_input)
        new_input = user_input.reshape(1,-1)
        h_prediction = heart_disease_model.predict(new_input)
        if h_prediction[0]==1:
            heart_diagnosis = 'The person have Heart Disease'
        else:
            heart_diagnosis = 'The person doesn`t have Heart Disease'
        st.success(heart_diagnosis)
elif selected=='Parkinsons Disease Prediction':
    st.title('PARKINSONS DISEASE PREDICTION USING ML')
    #MDVP:Fo(Hz),MDVP:Fhi(Hz),MDVP:Flo(Hz),MDVP:Jitter(%),MDVP:Jitter(Abs),
    #MDVP:RAP,MDVP:PPQ,Jitter:DDP,MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,
    # MDVP:APQ,Shimmer:DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        mdvpFOhz = st.text_input("MDVP:Fo(Hz)")
    with col2:
        mdvpFhihz = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        mdvpFlohz = st.text_input("MDVP:Flo(Hz)")
    with col4:
        mdvpJitterPer = st.text_input("MDVP:Jitter(%)")
    with col1:
        mdvpJitterAbs = st.text_input("MDVP:Jitter(Abs)")
    with col2:
        mdvpRap = st.text_input("MDVP:RAP")
    with col3:
        mdvpPPQ = st.text_input("MDVP:PPQ")
    with col4:
        jitterDDP = st.text_input("Jitter:DDP")
    with col1:
        mdvpShimmer = st.text_input("MDVP:Shimmer")
    with col2:
        mdvpShimmerDb = st.text_input("MDVP:Shimmer(dB)")
    with col3:
        shimmerAPQ3 = st.text_input("Shimmer:APQ3")
    with col4:
        shimmerAPQ5 = st.text_input("Shimmer:APQ5")
    with col1:
        mdvpAPQ = st.text_input("MDVP:APQ")
    with col2:
        shimmerDDA = st.text_input("Shimmer:DDA")
    with col3:
        nhr = st.text_input("NHR")
    with col4:
        hnr = st.text_input("HNR")
    with col1:
        rpde = st.text_input("RPDE")
    with col2:
        dfa = st.text_input("DFA")
    with col3:
        spread1 = st.text_input("Spread1")
    with col4:
        spread2 = st.text_input("spread2")
    with col1:
        d2 = st.text_input("D2")
    with col2:
        ppe = st.text_input("PPE")
    park_diagnosis = ''
    if st.button("TEST RESULT"):
        user_input = [
            mdvpFOhz,mdvpFhihz,mdvpFlohz,mdvpJitterPer,
            mdvpJitterAbs,mdvpRap,mdvpPPQ,jitterDDP,
            mdvpShimmer,mdvpShimmerDb,shimmerAPQ3,
            shimmerAPQ5,mdvpAPQ,shimmerDDA,nhr,hnr,
            rpde,dfa,spread1,spread2,d2,ppe
        ]
        user_input = [float(x) for x in user_input]
        user_input = np.array(user_input)
        new_input = user_input.reshape(1,-1)
        park_prediction = parkinsons_disease_model.predict(new_input)
        if(park_prediction[0]==0):
            park_diagnosis = 'Person Doest`nt have ParkinSon`s disease'
        else:
            park_diagnosis = 'Person have ParkinSon`s disease'
        
        st.success(park_diagnosis);
