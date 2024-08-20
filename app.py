import streamlit as st
from src.pipeline.prediction_pipeline import Features, Prediction

online_order_list = ["Yes", "No"]
book_table_list = ["Yes", "No"]
location_list = ['Banashankari', 'Other', 'Jayanagar', 'JP Nagar','Bannerghatta Road', 'BTM', 'Electronic City', 'Sarjapur Road',
                 'Koramangala', 'HSR', 'Bellandur', 'Marathahalli', 'Whitefield','Indiranagar', 'MG Road', 'Brigade Road', 'Ulsoor']
restaurant_type_list = ['Buffet', 'Cafes', 'Delivery', 'Desserts', 'Dine-out',
                        'Drinks & nightlife', 'Pubs and bars']
cuisines_type_list = ['North Indian', 'Chinese', 'Cafe', 'South Indian', 'Other',
                      'Bakery', 'Biryani', 'Street Food', 'Fast Food', 'Ice Cream',
                      'Desserts', 'Continental', 'Beverages', 'Andhra', 'Kerala']
restaurant_serving_type = ['Casual Dining', 'Cafe', 'Quick Bites', 'Delivery', 'Other','Dessert Parlor', 'Bakery', 'Pub', 'Takeaway', 'Beverage Shop',
                           'Sweet Shop', 'Bar', 'Food Court']
city_list = ['Banashankari', 'Bannerghatta Road', 'Basavanagudi', 'Bellandur','Brigade Road', 'Brookefield', 'BTM', 'Church Street',
             'Electronic City', 'Frazer Town', 'HSR', 'Indiranagar','Jayanagar', 'JP Nagar', 'Kalyan Nagar', 'Kammanahalli','Koramangala', 'Lavelle Road', 'Malleshwaram', 'Marathahalli',
             'MG Road', 'New BEL Road', 'Old Airport Road', 'Rajajinagar','Residency Road', 'Sarjapur Road', 'Whitefield']

online_order = st.selectbox("please enter if it is an online order", online_order_list)
book_table = st.selectbox("please enter if table was book", book_table_list)
votes = st.number_input("please enter number of votes", value=0)
location = st.selectbox("please select the location", location_list)
cost_for_two = st.number_input("please enter the cost for two people", value=0)
type = st.selectbox("please enter the restaurant type", restaurant_type_list)
city = st.selectbox("please enter the city", city_list)
restaurant_type = st.selectbox("please enter restaurant serving type", restaurant_serving_type)
cuisines = st.selectbox("please enter the cuisine type", cuisines_type_list)
number_of_cuisines_offered = st.number_input("please enter the number of cuisines that are offered", value=0)

st.button("predict")

if __name__ == "__main__":
    f = Features(online_order,book_table,votes,location,cost_for_two,type,city,restaurant_type,cuisines,number_of_cuisines_offered)
    features_as_df = f.to_dataframe()
    p = Prediction()
    output = p.initiate_prediction(features_as_df)
    op=round(output[0],2)
    st.subheader(op)
