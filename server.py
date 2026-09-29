"""
Flask web server for the Emotion Detector application.
"""

from flask import Flask, jsonify, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/")
def home():
    """Render the Emotion Detector web interface."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Detect emotion from the supplied text."""
    text = request.args.get("text", "").strip()

    if not text:
        return jsonify({
            "error": "Please enter a valid text.",
            "status_code": 400
        }), 400

    result = emotion_detector(text)

    return jsonify(result)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
