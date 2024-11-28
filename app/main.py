import sys
import os

# Dynamically add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import modules from the src directory
from src.data_preprocessing import load_data, preprocess_batting_data, preprocess_bowling_data
from src.feature_engineering import create_player_metrics
from src.recommendation_system import recommend_players

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    print("Index route accessed")  # Debug statement
    return render_template('index.html')



# Recommendation route
@app.route('/recommend', methods=['POST'])
def recommend():
    print("Recommend route accessed")  # Debug statement
    try:
        # Get user input from the form
        role = request.form['role']
        threshold = float(request.form['threshold'])

        # Load and preprocess data
        batting, bowling, _, _, _ = load_data()
        batting = preprocess_batting_data(batting)
        bowling = preprocess_bowling_data(bowling)

        # Create player metrics
        players = create_player_metrics(batting, bowling)

        # Generate recommendations
        recommendations = recommend_players(players, role, threshold)

        # If no recommendations found, return a simple message
        if recommendations.empty:
            return render_template('index.html', message="No players match the criteria. Please try again.")

        # Render recommendations as an HTML table
        return render_template('recommendations.html', tables=[recommendations.to_html(classes='data')], titles=[''])

    except Exception as e:
        # Handle any errors and display them to the user
        return render_template('index.html', message=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
