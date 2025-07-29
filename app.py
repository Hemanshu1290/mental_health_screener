
from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    "Little interest or pleasure in doing things?",
    "Feeling down, depressed, or hopeless?",
    "Feeling nervous, anxious, or on edge?",
    "Trouble relaxing or staying calm?",
    "Trouble falling asleep or staying asleep, or sleeping too much?",
    "Feeling tired or having little energy?",
    "Poor appetite or overeating?",
    "Difficulty concentrating on things (e.g., reading, working)?",
    "Feeling bad about yourself — or that you are a failure or let others down?"
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
