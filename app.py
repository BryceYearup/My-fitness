from flask import Flask, render_template, request

app = Flask(__name__)

# Sample workout suggestions (These can be expanded based on more complex logic or fetched from a database)
workouts = {
    "fat_loss": [
        "High-Intensity Interval Training (HIIT)",
        "Circuit Training",
        "Strength Training with Compound Movements",
        "Jump Rope",
        "Running or Cycling"
    ],
    "muscle_gain": [
        "Weightlifting (Focus on Compound Movements)",
        "Bodyweight Exercises (Push-ups, Squats)",
        "Deadlifts",
        "Bench Press",
        "Pull-ups"
    ],
    "balanced": [
        "Yoga or Pilates",
        "Cardio with Strength Training",
        "Swimming",
        "Running",
        "Cycling"
    ]
}

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/start', methods=['GET', 'POST'])
def index():
    result = ''
    workout_suggestions = []

    if request.method == 'POST':
        try:
            body_fat = float(request.form['bodyFat'])
            calories = int(request.form['calories'])
            workout_plan = request.form['workoutPlan']

            # Start creating the result
            result += f'Your Body Fat: {body_fat}%\n'
            result += f'Your Calorie Intake: {calories} calories\n'
            result += f'Your Current Workout Plan: {workout_plan}\n\n'

            # Determine the fitness plan type based on body fat
            if body_fat < 15:
                result += 'You have a low body fat percentage. Consider focusing on muscle gain.\n'
                workout_suggestions = workouts["muscle_gain"]
            elif body_fat < 25:
                result += 'You have a moderate body fat percentage. Consider focusing on a balanced approach.\n'
                workout_suggestions = workouts["balanced"]
            else:
                result += 'You have a high body fat percentage. Focus on fat loss exercises.\n'
                workout_suggestions = workouts["fat_loss"]

            # Adjust based on calorie intake
            if calories < 2000:
                result += 'Your calorie intake is low. Consider increasing your calorie intake to build muscle or improve performance.\n'
            elif calories < 2500:
                result += 'Your calorie intake is moderate. Maintain this level for balanced results.\n'
            else:
                result += 'Your calorie intake is high. Consider a calorie deficit plan to lose fat.\n'
        except ValueError:
            result = "Please make sure all fields are filled out correctly!"

    return render_template('index.html', result=result, workout_suggestions=workout_suggestions)

if __name__ == "__main__":
    app.run(debug=True)
