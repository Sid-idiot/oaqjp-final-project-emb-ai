"""
Unit tests for the emotion detection application.
"""

import unittest
from unittest.mock import Mock, patch

from emotion_detection import emotion_detector


def mock_watson_response(emotions):
    """Create a mock Watson NLP response."""
    response = Mock()
    response.status_code = 200
    response.json.return_value = {
        "emotionPredictions": [
            {
                "emotion": emotions
            }
        ]
    }
    return response


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector."""

    @patch("emotion_detection.requests.post")
    def test_joy(self, mock_post):
        """Test detection of joy."""
        mock_post.return_value = mock_watson_response({
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.95,
            "sadness": 0.02
        })

        result = emotion_detector("I am extremely happy and excited")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["status_code"], 200)

    @patch("emotion_detection.requests.post")
    def test_anger(self, mock_post):
        """Test detection of anger."""
        mock_post.return_value = mock_watson_response({
            "anger": 0.95,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.02
        })

        result = emotion_detector("I am extremely angry")

        self.assertEqual(result["dominant_emotion"], "anger")
        self.assertEqual(result["status_code"], 200)

    @patch("emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        """Test detection of sadness."""
        mock_post.return_value = mock_watson_response({
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.02,
            "joy": 0.01,
            "sadness": 0.95
        })

        result = emotion_detector("I am feeling very sad")

        self.assertEqual(result["dominant_emotion"], "sadness")
        self.assertEqual(result["status_code"], 200)

    @patch("emotion_detection.requests.post")
    def test_fear(self, mock_post):
        """Test detection of fear."""
        mock_post.return_value = mock_watson_response({
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.95,
            "joy": 0.01,
            "sadness": 0.02
        })

        result = emotion_detector("I am scared and nervous")

        self.assertEqual(result["dominant_emotion"], "fear")
        self.assertEqual(result["status_code"], 200)

    @patch("emotion_detection.requests.post")
    def test_disgust(self, mock_post):
        """Test detection of disgust."""
        mock_post.return_value = mock_watson_response({
            "anger": 0.01,
            "disgust": 0.95,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.02
        })

        result = emotion_detector("That food is disgusting")

        self.assertEqual(result["dominant_emotion"], "disgust")
        self.assertEqual(result["status_code"], 200)

    def test_blank_input(self):
        """Test blank input handling."""
        result = emotion_detector("")

        self.assertEqual(result["status_code"], 400)
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()