<<<<<<< HEAD

import streamlit as st
import joblib
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Drilling Cost Estimator", page_icon="🛢", layout="centered")

# Load model and column structure
model = joblib.load('drilling_cost_model.pkl')
model_columns = joblib.load('drilling_columns.pkl')

# Main app title
st.title("🛢 Drilling Cost Estimator")
st.markdown("""
Welcome to the *Drilling Cost Estimation App*.  
This tool uses a trained Machine Learning model to estimate drilling costs based on your provided well parameters.
""")

# Sidebar info
st.sidebar.title("📌 About the App")
st.sidebar.markdown("""
This app predicts drilling cost based on input parameters such as:

- Depth (ft)  
- Hole Size (in)  
- Mud Type  
- Rig Type  
- Formation Type  

Created by *Abdullah Bukhari*  
🎓 1st Year Petroleum Engineering Student  
""")

# Input section
st.header("📝 Enter Drilling Parameters")

col1, col2 = st.columns(2)
with col1:
    depth_ft = st.number_input("Depth (ft)", min_value=1000, max_value=30000, step=100)
    mud_type = st.selectbox('Mud Type', ['Water-Based', 'Oil-Based', 'Synthetic-Based'])

with col2:
    hole_size_in = st.number_input("Hole Size (in)", min_value=5.0, max_value=30.0, step=0.5)
    rig_type = st.selectbox('Rig Type', ['Land Rig', 'Offshore Rig', 'Jack-up Rig'])

formation = st.selectbox('Formation Type', ['Sandstone', 'Limestone', 'Shale'])

# Prediction button
if st.button("💰 Predict Drilling Cost"):
    # Prepare input data
    input_data = pd.DataFrame([{
        'Depth_ft': depth_ft,
        'Hole_Size_In': hole_size_in,
        'Mud_Type': mud_type,
        'Rig_Type': rig_type,
        'Formation_Type': formation
    }])

    # One-hot encode input
    input_encoded = pd.get_dummies(input_data)

    # Add missing columns
    for col in model_columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[model_columns]

    # Make prediction
    prediction = model.predict(input_encoded)[0]

    # Show result
    st.success(f"💲 *Estimated Drilling Cost:* ${prediction:,.2f}")
    st.balloons()

=======
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


>>>>>>> bdd29b59a552d4a90d36d1899e1067fbf33f706d
