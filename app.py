from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load your trained model and preprocessor
model = pickle.load(open('artifacts/models.pkl', 'rb'))
preprocessor = pickle.load(open('artifacts/proprocessor.pkl', 'rb'))

@app.route('/', methods=['GET']) 
def home():
    return render_template('home.html')

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    if request.method == 'POST':
        # Get form data
        gender = request.form['gender']
        ethnicity = request.form['ethnicity']
        parental_education = request.form['parental_level_of_education']
        lunch = request.form['lunch']
        test_course = request.form['test_preparation_course']
        reading_score = float(request.form['reading_score'])
        writing_score = float(request.form['writing_score'])

        # Create DataFrame from input
        input_df = pd.DataFrame([{
            'gender': gender,
            'race/ethnicity': ethnicity,
            'parental level of education': parental_education,
            'lunch': lunch,
            'test preparation course': test_course,
            'reading score': reading_score,
            'writing score': writing_score
        }])

        # Transform input and predict
        transformed_input = preprocessor.transform(input_df)
        result = model.predict(transformed_input)[0]

        return render_template('home.html', results=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
