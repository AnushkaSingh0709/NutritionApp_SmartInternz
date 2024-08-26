
# Nutrition App Using Gemini Pro: Your Comprehensive Guide to Healthy Eating and Well-being

**Demonstration Video**: [Link to Video]

## Introduction

**Nutrition App Using Gemini Pro** is an innovative mobile application designed to provide personalized dietary recommendations and nutritional advice using the advanced capabilities of the Google Gemini 1.5 Flash model. The app leverages artificial intelligence to analyze user data, dietary preferences, and health goals, delivering tailored meal plans, nutritional insights, and wellness tips. The primary aim of the app is to promote healthier eating habits and improve overall well-being through intelligent and data-driven recommendations.

## Features

- **Personalized Dietary Recommendations**: Tailors meal plans based on individual health goals and dietary preferences.
- **Real-time Nutritional Feedback**: Analyzes meals and provides immediate insights on nutritional balance.
- **Multiscenario Support**: Adapts to various user goals, including weight loss, diabetes management, and muscle building.
- **Seamless Integration with Fitness Trackers**: Syncs with fitness devices to provide a holistic approach to health management.
- **Educational Resources**: Offers tips and resources to educate users on maintaining a balanced diet and healthy lifestyle.

## Scenarios

### Scenario 1: Weight Loss Journey
- **User**: Sarah, 28, a vegetarian aiming to lose 15 pounds.
- **Solution**: Provides a calorie-controlled, nutrient-dense meal plan, integrating data from her fitness tracker for comprehensive guidance.

### Scenario 2: Managing Diabetes
- **User**: John, 45, with Type 2 Diabetes.
- **Solution**: Generates low-carb, high-fiber meal plans, offering real-time feedback and educational resources on managing diabetes through diet.

### Scenario 3: Building Muscle
- **User**: Emily, 30, a strength training enthusiast.
- **Solution**: Creates high-protein meal plans to support muscle growth, integrating workout data to optimize dietary recommendations.

## Project Flow

1. **User Interaction**: Users input their dietary preferences and health goals via the UI.
2. **Data Transmission**: Inputs are transmitted to the backend using the Google API key.
3. **Model Processing**: The input is processed by the Gemini 1.5 Flash pre-trained model via an API call.
4. **Result Generation**: The model processes the input and generates personalized dietary recommendations.
5. **Output Display**: Results are returned to the frontend for display in an intuitive and user-friendly format.

## Requirements Specification

### Steps to Complete the Project

1. **Create a `requirements.txt` file**: List all required libraries.
2. **Install Required Libraries**:
   - Streamlit
   - streamlit_extras
   - google-generativeai
   - python-dotenv
   - PyPDF2
   - Pillow
3. **Generate and Initialize Google API Key**:
   - Generate the API key from the Google API Console.
   - Store the key securely in a `.env` file.
4. **Interfacing with Pre-trained Model**:
   - Load the Gemini 1.5 Flash pre-trained model.
   - Implement functions to generate responses and process images.
5. **Model Deployment**:
   - Integrate with Streamlit for the web framework.
   - Host the application using Streamlit.

## Prior Knowledge Required

To complete this project, you should have a working knowledge of the following topics:

- **Generative AI Concepts**
- **Natural Language Processing (NLP)**
- **Google Gemini 1.5 Flash Model**
- **Streamlit Framework**

## Project Structure

```
NutritionApp/
│
├── images/                 # Stores images used in the UI
├── .env                    # Stores Google API key securely
├── app.py                  # Main application file with model and Streamlit UI code
└── requirements.txt        # List of required libraries
```

## Installation and Setup

1. **Clone the repository**:
   ```
   git clone https://github.com/yourusername/NutritionApp.git
   ```
2. **Navigate to the project directory**:
   ```
   cd NutritionApp
   ```
3. **Install the required libraries**:
   ```
   pip install -r requirements.txt
   ```
4. **Set up the Google API key**:
   - Create a `.env` file in the root directory.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key
     ```
5. **Run the application**:
   ```
   streamlit run app.py
   ```

## Conclusion

**Nutrition App Using Gemini Pro** successfully demonstrates how AI-driven personalized dietary recommendations can enhance user well-being. With its intuitive interface and robust backend, it serves as a comprehensive tool for anyone looking to improve their health through better nutrition.

