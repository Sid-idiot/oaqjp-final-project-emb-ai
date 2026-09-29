"""
Emotion Detection module.

Provides an emotion_detector function that analyzes text
and returns emotion scores and the dominant emotion.
"""


def emotion_detector(text):
    """
    Analyze text and return emotion scores.

    Args:
        text (str): Input sentence.

    Returns:
        dict: Emotion scores and dominant emotion.
    """
    if text is None or not isinstance(text, str) or not text.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "status_code": 400,
        }

    text = text.lower()

    emotions = {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.0,
        "sadness": 0.0,
    }

    emotion_keywords = {
        "anger": [
            "angry", "anger", "furious", "mad",
            "hate", "annoyed", "rage", "irritated"
        ],
        "disgust": [
            "disgust", "disgusting", "gross",
            "awful", "nasty", "revolting"
        ],
        "fear": [
            "afraid", "fear", "scared", "terrified",
            "worried", "nervous", "panic"
        ],
        "joy": [
            "happy", "joy", "excellent", "great",
            "amazing", "wonderful", "love", "excited",
            "good", "fantastic"
        ],
        "sadness": [
            "sad", "unhappy", "depressed", "cry",
            "lonely", "upset", "heartbroken"
        ],
    }

    matches = {}

    for emotion, keywords in emotion_keywords.items():
        matches[emotion] = sum(
            word in text for word in keywords
        )

    total_matches = sum(matches.values())

    if total_matches == 0:
        for emotion in emotions:
            emotions[emotion] = 0.20
    else:
        for emotion in emotions:
            emotions[emotion] = round(
                matches[emotion] / total_matches,
                2
            )

    dominant_emotion = max(
        emotions,
        key=emotions.get
    )

    emotions["dominant_emotion"] = dominant_emotion
    emotions["status_code"] = 200

    return emotions
