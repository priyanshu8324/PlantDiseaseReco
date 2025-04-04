import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Store locations with coordinates, details, and phone numbers
locations = {
    "SRI MANJUNATHA FERTILIZERS": (13.3364, 77.1051, "2nd Main Rd, Tumakuru", "1234567890"),
    "K.R.Vijayakumar Fertiliser & Seeds Dealer": (13.3344, 77.1068, "Gandhi Nagar, Tumakuru", "9876543210"),
    "Sri Guru Raghavendra Fertilisers": (13.3386, 77.1070, "M G Road, Tumakuru", "9988776655"),
    "Annapurna Agro Agencies": (13.3421, 77.1028, "B H Road, Tumakuru", "8877665544"),
    "Raitha Mitra Agro Centre": (13.3491, 77.1121, "Siddaganga Extension, Tumakuru", "7766554433")
}

# Function to create a Folium map
def create_map(locations):
    # Calculate map center based on average coordinates
    lats = [lat for lat, _, _, _ in locations.values()]
    lons = [lon for _, lon, _, _ in locations.values()]
    map_center = (sum(lats) / len(lats), sum(lons) / len(lons))

    folium_map = folium.Map(location=map_center, zoom_start=13)  # Increased zoom for better view

    # Add markers for each store
    for store_name, (lat, lon, address, phone) in locations.items():
        folium.Marker(
            location=(lat, lon),
            popup=f"<strong>{store_name}</strong><br>{address}<br>Phone: {phone}",
            icon=folium.Icon(color='blue')
        ).add_to(folium_map)

    return folium_map

# Streamlit application
st.title("Store Availability in Tumakuru")
st.markdown("Explore available stores in Tumakuru on the map and view detailed information below.")

# Display the map
folium_map = create_map(locations)
st_folium(folium_map, width=800, height=500)  # Adjusted map size

# Create a DataFrame for the store details
store_details = pd.DataFrame.from_dict(locations, orient='index', columns=['lat', 'lon', 'address', 'phone'])
store_details.reset_index(inplace=True)
store_details.columns = ['Store Name', 'Latitude', 'Longitude', 'Address', 'Phone']

# Display the store details in a more informative table
st.subheader("Store Details")
st.markdown("Click on the store name to view it on the map.")

for index, row in store_details.iterrows():
    st.write(f"**{row['Store Name']}**")
    st.write(f"Address: {row['Address']}")
    st.write(f"Phone: {row['Phone']}")
    st.write(f"Latitude: {row['Latitude']}, Longitude: {row['Longitude']}")
    st.markdown("---")  # Add a separator between stores

# Additional content for the Availability page can go here
st.markdown("---")
st.markdown("This application provides a visual representation of store locations in Tumakuru. Click on the markers for store information.")