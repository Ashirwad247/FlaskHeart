
# Heart Disease Prediction System

This project is a Flask-based web application that predicts the likelihood of heart disease using machine learning. It uses a pre-trained machine learning model to analyze input data and provide a prediction.

---

## Features
- **User-friendly Interface**: Simplified for ease of use by medical practitioners and users.
- **Machine Learning Model**: Pre-trained using advanced algorithms.
- **Modular Design**: The app is built with Flask, ensuring flexibility and scalability.

---

## Prerequisites
Ensure you have the following installed:
- Python 3.7 or higher
- `pip` (Python package manager)
- Virtual Environment (`venv`)

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd heart_disease
   ```

2. **Set Up a Virtual Environment**
   Navigate to the `env` directory:
   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**
   - **Windows**: 
     ```bash
     env\Scripts\activate.bat
     ```
   - **Linux/Mac**: 
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   Start the Flask development server:
   ```bash
   python app.py
   ```
   The app will be accessible at `http://127.0.0.1:5000`.

---

## Directory Structure

```
heart_disease/
│
├── app.py                     # Main application file
├── env/                       # Virtual environment directory
├── requirements.txt           # Python dependencies
├── saved_trained_model.pkl    # Pre-trained ML model
├── static/                    # Static assets (CSS, JS, images)
└── templates/                 # HTML templates for the Flask app
```

---

## Dependencies

The project uses the following Python packages:
- Flask
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn

All dependencies are listed in `requirements.txt`.

---

## Machine Learning Model

The ML model used (`saved_trained_model.pkl`) was trained on a heart disease dataset using algorithms like XGBoost and Random Forest. The model achieves high accuracy for predictions and is optimized for real-world use.

---

## Usage

1. Launch the app using the setup instructions above.
2. Navigate to the web interface.
3. Input the required parameters such as age, cholesterol levels, etc.
4. Submit the form to receive predictions.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Acknowledgments

Special thanks to all contributors and open-source libraries used in this project.
