# Green Guardian - Plant Disease Detection System

![Project Logo](img%20diis/home_page.jpg)

## 🌱 About the Project
Green Guardian is an AI-powered web application that helps identify plant diseases and provides treatment recommendations. Using a deep learning model trained on 87K images of healthy and diseased plants, it can detect 38 different disease classes with high accuracy.

## ✨ Key Features
- **Disease Recognition**: Upload an image of your plant to get instant disease diagnosis
- **Treatment Recommendations**: Get detailed medicine names and dosage information
- **Comprehensive Database**: Covers 38 common plant diseases
- **User-Friendly Interface**: Simple and intuitive web interface
- **Community Features**: Share experiences and get help from other users

## 🛠️ Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/green-guardian.git
cd green-guardian
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the pre-trained model from [link] and place it in the project root

## 🚀 Usage
1. Run the application:
```bash
streamlit run main.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Use the sidebar to navigate between:
   - **Home**: Project overview
   - **About**: Dataset information
   - **Disease Recognition**: Upload plant images for diagnosis
   - **Availability**: Check medicine availability
   - **Community**: Connect with other users

## 📸 Screenshots
| Home Page | Disease Detection | Treatment Recommendations |
|-----------|-------------------|---------------------------|
| ![Home](img%20diis/home_page.jpg) | ![Detection](img%20diis/tomato_leaf_mold.png) | ![Treatment](img%20diis/medicine_info.png) |

## 📊 Dataset
The model was trained on a dataset containing:
- 70,295 training images
- 17,572 validation images
- 33 test images

Dataset covers 38 classes of healthy and diseased plants including:
- Apple
- Cherry
- Corn
- Grape
- Peach
- Pepper
- Potato
- Strawberry
- Tomato
- And more...

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
- Original dataset from [PlantVillage Dataset](https://github.com/spMohanty/PlantVillage-Dataset)
- TensorFlow and Streamlit communities
