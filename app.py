import streamlit as st

st.markdown(
    """
   <style>
   body {
       background-color: rgb(85, 157, 97);
       color: linear-gradient(135deg, rgb(42, 61, 66), rgb(22, 45, 65));
   }
   .stApp {
       background-color: linear-gradient(135deg, rgb(40, 60, 66), rgb(22, 45, 65));
       padding: 30px;
       border-radius: 15px;
       box-shadow: 0 4px 6px rgba(65, 50, 89, 0.3);
   }
   h1 {
       text-align: center;
       font-size: 36px;
       color: linear-gradient(135deg, rgb(35, 34, 90), rgb(58, 13, 51));
   }
   .stbutton>button {
       background-color: linear-gradient(45deg, rgb(23, 61, 94), rgb(55, 35, 106));
       color: linear-gradient(135deg, rgb(110, 39, 96), rgb(46, 88, 124));
       font-size: 18px;
       padding: 10px 20px;
       border-radius: 10px;
       box-shadow: 0 4px 6px rgba(70, 48, 103, 0.4);
       transition: 0.3s;
   }
   .stbutton>button:hover {
       background-color: linear-gradient(45deg, rgb(17, 97, 137), rgb(31, 18, 88));
       transform: scale(1.05);
       color: linear-gradient(135deg, rgb(31, 27, 82), rgb(22, 45, 65));
   }
   .result-box {
       font-size: 24px;
       font-weight: bold;
       text-align: center;
       background: rgba(24, 35, 71, 0.1);
       padding: 25px;
       border-radius: 10px;
       margin-top: 20px;
       box-shadow: 0px 5px 15px rgba(71, 15, 15, 0.3);
   }
   .footer {
       text-align: center;
       margin-top: 50px;
       font-size: 14px;
       color: linear-gradient(135deg, rgb(51, 129, 150), rgb(54, 122, 181));
   }
   </style>
   """,
    unsafe_allow_html=True
)

# Title and description:
st.markdown("<h1>UNIT CONVERTER</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions with added error handling

def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
    }
    if from_unit not in length_units or to_unit not in length_units:
        return "Invalid units"
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilograms': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    if from_unit not in weight_units or to_unit not in weight_units:
        return "Invalid units"
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    return "Invalid units"

# Button for conversion
if st.button(" Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)

    if isinstance(result, str) and result == "Invalid units":
        st.error("Invalid units selected. Please try again.")
    else:
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Created by Bushra Memon</div>", unsafe_allow_html=True)