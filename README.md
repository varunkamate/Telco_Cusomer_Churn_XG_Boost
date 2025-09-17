📞 Telco Customer Churn Prediction
A Streamlit web application that predicts customer churn for a telecommunications company. The app uses a pre-trained XGBoost model to analyze customer data and provides a real-time prediction based on user-input features.

===============================================================

🚀 Live Demo:==> https://telcocusomerchurnxgboost-f8sh8hyeahyyfggdmu7ff3.streamlit.app/

===============================================================

📌 Project Objective
Build an interactive web application using Streamlit.

Utilize a pre-trained machine learning model (model.pkl) to make predictions.

Allow users to input customer data (e.g., tenure, monthly charges, contract type) through a clean user interface.

Provide a clear churn prediction (Yes/No) and its probability.

===============================================================

🛠️ Tools & Technologies
Python, Pandas, NumPy, Scikit-learn, XGBoost

Frontend: Streamlit for interactive UI

Environment: VS Code

Version Control: Git & GitHub

===============================================================

📂 Project Structure
Telco_Churn_Predictor/
│── app.py                 # Main Streamlit application
│── model.pkl              # Pre-trained XGBoost model
│── Telco_Cusomer_Churn.csv # Original dataset used for training
│── XG_BOOST.ipynb         # Jupyter Notebook with the model training
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation

📊 Methodology
The project leverages the power of machine learning and data visualization to create a functional web app.

Model Training: An XGBoost classifier was trained on the Telco_Cusomer_Churn.csv dataset.

Serialization: The trained model was saved as a binary file (model.pkl) for easy deployment.

Web App Development: The app.py script loads the serialized model, creates a user interface with Streamlit widgets, and uses the model to generate real-time predictions based on user input.

🚀 How to Run Locally
Clone the repository: git clone [https://github.com/your-username/Telco-Churn-Predictor.git](https://github.com/varunkamate/Telco_Cusomer_Churn_XG_Boost?tab=readme-ov-file)

Navigate to the project folder: cd Telco_Churn_Predictor

Create a virtual environment: python -m venv venv

Activate the virtual environment:

Windows: .\venv\Scripts\activate

macOS/Linux: source venv/bin/activate

Install dependencies: pip install -r requirements.txt

Run the Streamlit app: streamlit run app.py
