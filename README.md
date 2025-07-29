# 🧠 Mental Health Screener

A simple and effective web application built using **Python Flask** that allows users to assess their mental health through a questionnaire and receive a visual + textual result based on their responses.

---

## 💡 About the Project

This project was built as part of a hackathon to address the increasing need for **early mental health screening**. It is **not a diagnostic tool**, but rather a first-step awareness screener to help users understand their mental well-being.

---

## ✨ Features

- ✅ 9-question depression screening (based on PHQ-9 model)
- ✅ Score-based assessment (Mild, Moderate, Severe)
- ✅ Bar/doughnut chart visualization using Chart.js
- ✅ Clean, responsive UI with calming color tones
- ✅ Simple backend using Python + Flask
- ✅ Fully open-source and customizable

---

## 🖥️ Live Demo

If you're running locally:  
🔗 Open your browser and go to → `http://127.0.0.1:5000`

---

## 📸 Screenshots

> **Main Questionnaire Page**
![questionnaire](screenshots/questionnaire.png)

> **Result with Visualization**
![result](screenshots/result_chart.png)

*(Add these screenshots in a `screenshots/` folder in your repo)*

---

## 🛠️ Tech Stack

| Frontend       | Backend       | Libraries Used    |
|----------------|----------------|--------------------|
| HTML, CSS, JS  | Python (Flask) | Chart.js, Jinja2   |

---

## 🚀 Getting Started

To run this project on your local machine:

### 1. Clone the Repo

```bash
git clone https://github.com/Hemanshu1290/mental_health_screener.git
cd mental_health_screener
```

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:
```bash
pip install flask
```

### 4. Run the Flask App

```bash
python app.py
```

### 5. Open in Browser

Navigate to `http://127.0.0.1:5000` in your browser.

---

## 🧪 How It Works

- The user answers 9 questions on a scale of 0–3.
- The backend calculates the total score.
- Based on the score, a result message is shown:
  - `0–4` → Minimal Depression 🟢
  - `5–9` → Mild Depression 🟡
  - `10–14` → Moderate Depression 🟠
  - `15+` → Severe Depression 🔴
- A chart displays the score for quick visual feedback.

---

## 📂 Project Structure

```
mental_health_screener/
│
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── index.html
│   └── result.html
├── app.py
├── README.md
└── requirements.txt
```

---

## 👨‍⚖️ For Judges / Hackathon Evaluators

This project demonstrates:
- Awareness on mental health
- Full-stack functionality with visualization
- Clean and usable design
- Extensibility for AI, NLP, or voice support (future scope)

✅ All code is well-structured and easy to follow.  
✅ No external databases or services are required.  
✅ Runs fully offline (except for Chart.js CDN).

---

## 🧠 Future Scope

- Add anxiety & stress screening
- Save anonymous results to CSV
- Connect to therapist database (via API)
- Add AI-based sentiment analysis

---

## 🤝 Contributors

- **Hemanshu Sharma** – [@Hemanshu1290](https://github.com/Hemanshu1290)

---

## ⚠️ Disclaimer

This tool is **for educational purposes only**. It is not intended to replace professional medical advice or treatment.

---

## 📃 License

MIT License. Free to use and modify with attribution.
