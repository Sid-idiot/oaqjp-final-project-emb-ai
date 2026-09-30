"""
Flask server for the Emotion Detection application.
"""

from flask import Flask, jsonify, render_template, request

from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the emotion detector interface."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """Analyze text submitted through the web interface."""

    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return "Invalid input! Try again.", 400

    result = emotion_detector(text_to_analyze)

    if result["status_code"] != 200:
        return (
            f"Emotion detection service unavailable "
            f"(status code: {result['status_code']})",
            503
        )

    formatted_response = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({
        "response": formatted_response,
        "anger": result["anger"],
        "disgust": result["disgust"],
        "fear": result["fear"],
        "joy": result["joy"],
        "sadness": result["sadness"],
        "dominant_emotion": result["dominant_emotion"]
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
