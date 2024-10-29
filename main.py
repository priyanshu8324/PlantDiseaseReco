import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model(r"C:\Users\Priyanka Bharti\Desktop\jupyter notebook\trained_plant_disease_model.h5")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #return index of max element

#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Recognition"])

#Main Page
if(app_mode=="Home"):
    st.header("Baele Sanjeeivini")
    image_path = r"C:\Users\Priyanka Bharti\Downloads\home_page.jpeg"
    st.image(image_path,use_column_width=True)
    st.markdown("""
**Revolutionizing Plant Care**

Welcome to the Plant Disease Detective 🕵️‍♀️🌱

Your Plant's Personal Doctor

Ever wondered why your plant isn't looking its best? 🌱 Our AI-powered tool can help! Simply upload a photo of your ailing plant, and we'll analyze it to identify potential diseases and offer expert advice.

How it Works:

Snap a Pic: Take a photo of your plant's affected area.
Upload and Analyze: Upload the image to our system. Our AI will analyze it for signs of disease.
Get Expert Advice: Receive tailored recommendations to help your plant recover.
Why Choose Us?

Accurate Diagnosis: Our AI is trained on a vast dataset of plant images, ensuring accurate results.
User-Friendly: No technical expertise required. Simply upload a photo and get instant results.
Quick and Easy: Get quick diagnoses and expert advice to help your plants thrive.
Let's Get Started!
Click on the Disease Recognition page to upload your plant's photo and let's get your plant back to health! 🌿
    """)

#About Project
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github repo.
                This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing 33 test images is created later for prediction purpose.
                #### Content
                1. train (70295 images)
                2. test (33 images)
                3. validation (17572 images)

                """)

#Prediction Page
elif(app_mode=="Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("User Image")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        st.snow()#effect
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Reading Labels
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))
        disease_info = {
                    0: {
                "cause": "Fungus: Venturia inaequalis",
                "medicine_name": "1. Captan\n2. Myclobutanil (e.g., Immunox)",
                "dosage": "\n1. 2.5 tablespoons per gallon of water, spray every 10 to 14 days.\n2. 1-2 tablespoons per gallon of water, applied as needed.",
                "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\roat.png"
                        },
                1: {
                    "cause": "Fungus: Botryosphaeria obtusa",
                    "medicine_name": "1. Captan\n2. Mancozeb",
                    "dosage": "\n1. 2.5 tablespoons per gallon of water, spray every 10 to 14 days.\n2. 2-3 tablespoons per gallon of water, applied as needed.",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\roat.png"
                },
                2: {
                    "cause": "Fungus: Gymnosporangium juniperi-virginianae",
                    "medicine_name": "Trifloxystrobin",
                    "dosage": "\nApply 3.0 to 7.0 fl oz/acre at the first sign of disease and repeat every 14 days if necessary.",  
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\apple rust.png"
                },
                3: {
                    "cause": "NONE",
                    "medicine_name": "NONE",
                    "dosage": "NONE",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\healthy.png"
                     },
                4: {
                    "cause": "NONE",
                    "medicine_name": "NONE",
                    "dosage": "NONE",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\healthy.png"
                     },
                7: {
                    "cause": "NONE",
                    "medicine_name": "NONE",
                    "dosage": "NONE",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\healthy.png"
                     },
                10: {
                    "cause": "NONE",
                    "medicine_name": "NONE",
                    "dosage": "NONE",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\healthy.png"
                     },
                14: {
                    "cause": "NONE",
                    "medicine_name": "NONE",
                    "dosage": "NONE",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\healthy.png"
                     },
                17: {
                    "cause": "NONE",
                    "medicine_name": "NONE",
                    "dosage": "NONE",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\healthy.png"
                     },
                19: {
                    "cause": "NONE",
                    "medicine_name": "NONE",
                    "dosage": "NONE",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\healthy.png"
                     },
                22: {
                    "cause": "NONE",
                    "medicine_name": "NONE",
                    "dosage": "NONE",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\healthy.png"
                     },
                23: {
                    "cause": "NONE",
                    "medicine_name": "NONE",
                    "dosage": "NONE",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\healthy.png"
                     },
                24: {
                    "cause": "NONE",
                    "medicine_name": "NONE",
                    "dosage": "NONE",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\healthy.png"
                     },
                27: {
                    "cause": "NONE",
                    "medicine_name": "NONE",
                    "dosage": "NONE",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\healthy.png"
                     },
                37: {
                    "cause": "NONE",
                    "medicine_name": "NONE",
                    "dosage": "NONE",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\healthy.png"
                     },
                5: {
                    "cause": "Podosphaera mors-uvae",
                    "medicine_name": "Myclobutanil",
                    "dosage": "Apply 2.0 to 4.0 fl oz/acre depending on the growth stage and infection level.",  # No specific dosage provided
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\cherry powdery.png"
                },
                7: {
                    "cause": "Cercospora zeae-maydis and Cercospora sorghi",
                    "medicine_name": "Pyraclostrobin",
                    "dosage": "Apply 6.0 to 15.5 fl oz/acre depending on the severity of the infection.",  # No specific dosage provided
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\corn.png"
                },
                8: {
                "cause": "Fungus: Puccinia sorghi",
                "medicine_name": "Azoxystrobin",
                "dosage": "Apply 6.0 to 15.5 fl oz/acre depending on the severity of the infection.",
                "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\corn rust.png"
                },
                9: {
                    "cause": "Fungus: Setosphaeria turcica",
                    "medicine_name": "Fungicide containing Azoxystrobin or Pyraclostrobin",
                    "dosage": "2–3g per liter of water (follow label instructions for optimal effectiveness)",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\corn northen.png"
                },
                11: {
                    "cause": "Fungus: Guignardia bidwellii",
                    "medicine_name": "Fungicide containing Myclobutanil or Mancozeb",
                    "dosage": "2–3g per liter of water (refer to label for precise usage instructions)",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\grapes black rot.png"
                },
                12: {
                    "cause": "Fungus: Phaeoacremonium aleophilum and Fomitiporia mediterranea",
                    "medicine_name": "Trunk injection with a fungicide like Thiophanate-methyl",
                    "dosage": "Follow label instructions for trunk injection, as application varies by product",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\grape esca.png"
                },
                13: {
                    "cause": "Fungus: Isariopsis clavispora",
                    "medicine_name": "Mancozeb 75% WP or Copper Hydroxide 77%",
                    "dosage": "Mancozeb 75% WP: 2-2.5 grams per liter of water.\nCopper Hydroxide 77%: 2 grams per liter of water.\n- Apply the fungicide as a foliar spray during early stages of growth\n- repeat as necessary according to label instructions.",
                    "image": r""
                },
                15: {
                    "cause": "Bacteria: Candidatus Liberibacter asiaticus",
                    "medicine_name": "Oxytetracycline and Streptomycin",
                    "dosage": "Oxytetracycline: 1.5 - 2 grams per tree, injected into the trunk, applied at intervals.\nStreptomycin: 1-2 grams per tree, injected similarly or sprayed.",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\orange.png"
                },
                16: {
                    "cause": "Bacteria: Xanthomonas campestris pv. pruni",
                    "medicine_name": "Copper Hydroxide",
                    "dosage": "1-2 grams per liter of water.\n- Apply during the growing season, especially during periods of high humidity and after rain, following the label instructions for frequency and timing.",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\peach bact.png"
                },
                18: {
                    "cause": "Bacteria: Xanthomonas campestris pv. vesicatoria",
                    "medicine_name": "Copper-based fungicides (e.g., Copper Hydroxide or Copper Oxychloride)",
                    "dosage": "- Copper Hydroxide: 1-3 grams per liter of water.\n- Copper Oxychloride: 2-3 grams per liter of water.\n- Apply during the early stages of infection and repeat every 7-14 days as needed, especially after rain.",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\pepper.png"
                },
                20: {
                    "cause": "Fungus: Alternaria solani",
                    "medicine_name": "1. Chlorothalonil\n2. Mancozeb",
                    "dosage": "1. Apply 1-2 lbs per acre every 7-14 days as needed.\n2. Apply 2-3 lbs per acre every 7-14 days as needed.",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\potato early bright.png"
                },
                21: {
                    "cause": "Fungus: Phytophthora infestans",
                    "medicine_name": "1. Metalaxyl\n2. Copper Fungicides",
                    "dosage": "1. Apply 1-2 lbs per acre every 7-14 days as needed.\n2. Apply according to label instructions, typically every 7-10 days.",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\poatato 2.png"
                },
                25: {
                "cause": "Fungus: Podosphaera fusca",
                "medicine_name": "1. Sulfur (Wettable sulfur)\n2. Potassium bicarbonate (e.g., Kaligreen)",
                "dosage": "1. 2-3 tablespoons per gallon of water, spray every 7 to 10 days.\n2. 1-2 tablespoons per gallon of water, applied as needed.",
                "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\squash.png"
                    },
                26: {
                    "cause": "Fungus: Diplocarpon earliana",
                    "medicine_name": "Fungicide containing Myclobutanil",
                    "dosage": "1–2g per liter of water (refer to the label for precise instructions)",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\strawberry.png"
                },
                28: {
                    "cause": "Bacteria: Xanthomonas campestris pv. vesicatoria",
                    "medicine_name": "Copper-based bactericide, e.g., Copper Hydroxide",
                    "dosage": "Follow label instructions, typically 2–3g per liter of water",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\tomato back spot.png"
                },
                29: {
                    "cause": "Fungus: Alternaria solani",
                    "medicine_name": "1. Chlorothalonil\n2. Mancozeb",
                    "dosage": "1. Apply 1-2 lbs per acre every 7-14 days as needed.\n2. Apply 2-3 lbs per acre every 7-14 days as needed.",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\tomato early bright.png"
                },
                30: {
                    "cause": "Fungus: Phytophthora infestans",
                    "medicine_name": "1. Metalaxyl\n2. Copper Fungicides",
                    "dosage": "1. Apply 1-2 lbs per acre every 7-14 days as needed.\n2. Apply according to label instructions, typically every 7-10 days.",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\tomato late bright.png"
                },
                31: {
                    "cause": "Fungus: Cladosporium fulvum",
                    "medicine_name": "Copper-based fungicide, e.g., Copper Oxychloride",
                    "dosage": "Follow product label (typically 2–3g per liter of water)",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\tomato leaf mold.png"
                },


                    32: {
                "cause": "Fungus: Septoria lycopersici",
                "medicine_name": "Copper fungicide spray",
                "dosage": "Apply once every 7-10 days",
                "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\tomato spectorial spot.png"
                    },

                33: {
                    "cause": "Mite: Tetranychus urticae",
                    "medicine_name": "Insecticidal Soap or Neem Oil",
                    "dosage": "Mix 1-2 tablespoons per gallon of water, spray every 7 days until infestation is controlled.",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\Tomato___Spider_mites.png"
                },

                34: {
                    "cause": "Fungus: Corynespora cassiicola",
                    "medicine_name": "Chlorothalonil fungicide",
                    "dosage": "Apply every 7-14 days as per label instructions",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\Tomato___Target_Spot.png"
                },

                35: {
                    "cause": "Virus: Tomato yellow leaf curl virus",
                    "medicine_name": "Imidacloprid spray (preventive for whiteflies)",
                    "dosage": "Apply every 7-10 days as directed",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\Tomato_Yellow_Leaf_Curl_Virus.png"
                },

                36: {
                    "cause": "Virus: Tomato mosaic virus",
                    "medicine_name": "Neem Oil spray (preventive)",
                    "dosage": "Spray weekly as per label instructions",
                    "image": r"C:\Users\Priyanka Bharti\Desktop\img diis\Tomato_mosaic_virus.png"
                }
                
        }

        disease_data = disease_info[result_index]
        st.write("Disease Caused By:", disease_data["cause"])
        st.write("Medicine Name:", disease_data["medicine_name"])
        st.write("Dosage:", disease_data["dosage"])
        st.image(disease_data["image"], width=200)


    if st.button("Availability"):
        stores = [
        {"name": "SRI MANJUNATHA FERTILIZERS, TUMKUR", "address": "2nd Main Rd , Tumakuru", "phone": "1234567890"},
        {"name": "K.R.Vijayakumar Fertiliser & Seeds Dealer", "address": "Gandhi Nagar, Tumakuru", "phone": "9876543210"},
        {"name": "Integrated Pest Control Pvt. Ltd.", "address": "Bengaluru, Karnataka", "phone": "7411032320"}
    ]
        if stores:
         st.table(stores)
        else:
            st.write("No stores found in your location.")
        

       
