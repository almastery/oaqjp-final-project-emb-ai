"""Flask application for Emotion Detection."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze emotion of the given text and return the result."""
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return "For the given statement, the system response is "\
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "\
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "\
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
