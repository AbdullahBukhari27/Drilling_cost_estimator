import streamlit as st
import joblib
import os
import pandas as pd 

#load training model
model = joblib.load('drilling_cost_model.pkl')
model_columns = joblib.load('drilling_columns.pkl')

#title of app
st.title('Drilling Cost Eistimator')
st.write('enter drilling parameters to estimate drilling cost')

#user input
depth_ft = st.number_input('Depth(ft)', min_value = 0)
hole_size_in = st.number_input('Hole Size(In)' , min_value = 0.0)
mud_type = st.selectbox('Mud Type',['Water-Based' , 'Oil-Based' , 'Synthetic-Based'])
rig_type = st.selectbox('Rig Type' , ['Land Rig' , 'Offshore Rig' , 'Jack-up Rig'])
formation = st.selectbox('Formation Type',['Sandstone' , 'Limestone' , 'Shale'])


#encoded this app

 

#when button is clicked
if st.button('Predict Cost'):
    input_data = pd.DataFrame([{'Depth_ft': depth_ft,'Hole_Size_In': hole_size_in,'Mud_Type': mud_type,'Rig_Type': rig_type,'Formation_Type': formation}])

    

    #One-hot encode
    input_encoded = pd.get_dummies(input_data)

    #Match training columns
    for col in model_columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[model_columns]

    #Predict
    prediction = model.predict(input_encoded)[0]
    st.success(f"Estimated Drilling Cost: ${prediction:,.2f}")


