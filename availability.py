import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# --- Data Loading and Processing ---
@st.cache_data
def load_store_data():
    locations = {
        "Select": [],
           "Tumakuru": [
            {"NAME": "SRI MANJUNATHA FERTILIZERS", "PHONE": "1234567890", "LAT": 13.3364, "LON": 77.1051, "ADDRESS": "2nd Main Rd, Tumakuru"},
            {"NAME": "K.R.Vijayakumar Fertiliser & Seeds Dealer", "PHONE": "9876543210", "LAT": 13.3344, "LON": 77.1068, "ADDRESS": "Gandhi Nagar, Tumakuru"},
            {"NAME": "Sri Guru Raghavendra Fertilisers", "PHONE": "9988776655", "LAT": 13.3386, "LON": 77.1070, "ADDRESS": "M G Road, Tumakuru"},
            {"NAME": "Annapurna Agro Agencies", "PHONE": "8877665544", "LAT": 13.3421, "LON": 77.1028, "ADDRESS": "B H Road, Tumakuru"},
            {"NAME": "Raitha Mitra Agro Centre", "PHONE": "7766554433", "LAT": 13.348913570146168, "LON": 77.12963872246092, "ADDRESS": "Siddaganga Extension, Tumakuru"},
        ],
        
        "Bengaluru": [
            {"NAME": "Integrated Pest Control Pvt. Ltd.", "ADDRESS": "Bengaluru, Karnataka", "PHONE": "7411032320", "LAT": 12.9716, "LON": 77.5946},
            {"NAME": "Urban Farms Store", "ADDRESS": "MG Road, Bengaluru", "PHONE": "9876512345", "LAT": 12.9762, "LON": 77.6033},
            {"NAME": "Green Thumb Nursery", "ADDRESS": "Near MG Road Metro, Bengaluru", "PHONE": "8765432109", "LAT": 12.9795, "LON": 77.6019},
            {"NAME": "Jayanagar Agro Supplies", "ADDRESS": "4th Block, Jayanagar, Bengaluru", "PHONE": "7654321098", "LAT": 12.9267, "LON": 77.5827},
            {"NAME": "Plant Paradise", "ADDRESS": "Jayanagar Shopping Complex, Bengaluru", "PHONE": "6543210987", "LAT": 12.9288, "LON": 77.5845},
            {"NAME": "Indira Nursery", "ADDRESS": "100 Feet Road, Indiranagar, Bengaluru", "PHONE": "5432109876", "LAT": 12.9719, "LON": 77.6413},
            {"NAME": "Eco Solutions", "ADDRESS": "CMH Road, Indiranagar, Bengaluru", "PHONE": "4321098765", "LAT": 12.9754, "LON": 77.6341},
            {"NAME": "Malleswaram Seeds", "ADDRESS": "8th Cross, Malleswaram, Bengaluru", "PHONE": "3210987654", "LAT": 13.0058, "LON": 77.5608},
            {"NAME": "Green Life Store", "ADDRESS": "Sampige Road, Malleswaram, Bengaluru", "PHONE": "2109876543", "LAT": 13.0097, "LON": 77.5664}
        ]
    }
    return locations

# --- Map Creation Function ---
def create_map(stores):
    if not stores:
        return None

    lats = [store['LAT'] for store in stores if 'LAT' in store and isinstance(store['LAT'], (int, float))]
    lons = [store['LON'] for store in stores if 'LON' in store and isinstance(store['LON'], (int, float))]

    if not lats or not lons:
        return folium.Map(location=[12.9716, 77.5946], zoom_start=11) # Default Bangalore center

    map_center = (sum(lats) / len(lats), sum(lons) / len(lons))
    folium_map = folium.Map(location=map_center, zoom_start=12)

    for store in stores:
        if 'LAT' in store and isinstance(store['LAT'], (int, float)) and 'LON' in store and isinstance(store['LON'], (int, float)):
            folium.Marker(
                location=(store['LAT'], store['LON']),
                popup=f"<strong>{store['NAME']}</strong><br>{store['ADDRESS']}<br>Phone: {store['PHONE']}",
                icon=folium.Icon(color='blue')
            ).add_to(folium_map)
    return folium_map

# --- Availability Page ---
def availability_page():
    st.header("Fertilizer Store Availability")
    locations = load_store_data()
    location_names = list(locations.keys())
    selected_location = st.selectbox("Select Location", location_names)

    if selected_location and selected_location != "Select":
        stores = locations[selected_location]
        if stores:
            st.subheader(f"Fertilizer Stores in {selected_location}")
            df = pd.DataFrame(stores)
            df_display = df[['NAME', 'ADDRESS', 'PHONE']]
            df_display.index = df_display.index + 1
            st.table(df_display)

            st.subheader(f"Map of Stores in {selected_location}")
            folium_map = create_map(stores)
            if folium_map:
                st_folium(folium_map, width=800, height=500)
            else:
                st.warning("Could not display map due to missing coordinate data.")
        else:
            st.info(f"No store details available for {selected_location}.")
    elif selected_location == "Select":
        st.info("Please select a location to view the available fertilizer stores.")

# --- Main Execution ---
if __name__ == "__main__":
    availability_page()