import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open(r"C:\Users\Shivani Simran\Desktop\VS-Python\ML\Car-Price\rand_forest_model.pkl", 'rb')
model = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner):  
   
    prediction = model.predict([[Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner]])
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Car Price Prediction")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Car Price Prediction App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    Year = st.text_input("Year", "Type Here")
    Present_Price = st.text_input("Present_Price", "Type Here")
    Kms_Driven = st.text_input("Kms_Driven", "Type Here")
    Fuel_Type = st.text_input("Fuel_Type", "Type Here")
    Seller_Type = st.text_input("Seller_Type ", "Type Here")
    Transmission = st.text_input("Transmission", "Type Here")
    Owner = st.text_input("Owner", "Type Here")
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner)
    st.success('The Predicted price of the car based on above information is {}'.format(result))
     
if __name__=='__main__':
    main()
