
from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    "In the past two weeks, how often have you felt overwhelmed or unable to cope with daily responsibilities?",
    "Have you experienced persistent sadness, emptiness, or hopelessness recently?",
    "How often do you find it difficult to concentrate or make decisions?",
    "Have you had trouble falling or staying asleep, or sleeping too much?",
    "Do you often feel anxious, nervous, or on edge without a clear reason?",
    "How satisfied are you with your current relationships (family, friends, partner)?",
    "Have you noticed a significant change in your appetite or eating habits?",
    "Do you feel interested or motivated to engage in activities you used to enjoy?",
    "Have you had thoughts of self-harm or felt like life isn’t worth living?",
    "Do you feel emotionally supported by those around you?"
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        scores = [int(request.form.get(f"q{i}")) for i in range(len(questions))]
        total_score = sum(scores)
        if total_score <= 4:
            result = "Minimal symptoms"
        elif total_score <= 9:
            result = "Mild concern – pay attention to patterns"
        elif total_score <= 14:
            result = "Moderate risk – consider seeking support"
        elif total_score <= 21:
            result = "High risk – recommend consulting a mental health professional"
        else:
            result = "Severe symptoms – immediate help suggested"
        return render_template("result.html", result=result, score=total_score)
    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
