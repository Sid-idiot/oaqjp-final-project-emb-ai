"""
Unit tests for the emotion detection application.
"""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector."""

    def test_joy(self):
        """Test detection of joy."""
        result = emotion_detector(
            "I am extremely happy and excited"
        )
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["status_code"], 200)

    def test_anger(self):
        """Test detection of anger."""
        result = emotion_detector(
            "I am extremely angry"
        )
        self.assertEqual(result["dominant_emotion"], "anger")
        self.assertEqual(result["status_code"], 200)

    def test_sadness(self):
        """Test detection of sadness."""
        result = emotion_detector(
            "I am feeling very sad"
        )
        self.assertEqual(result["dominant_emotion"], "sadness")
        self.assertEqual(result["status_code"], 200)

    def test_fear(self):
        """Test detection of fear."""
        result = emotion_detector(
            "I am scared and nervous"
        )
        self.assertEqual(result["dominant_emotion"], "fear")
        self.assertEqual(result["status_code"], 200)

    def test_disgust(self):
        """Test detection of disgust."""
        result = emotion_detector(
            "That food is disgusting"
        )
        self.assertEqual(result["dominant_emotion"], "disgust")
        self.assertEqual(result["status_code"], 200)

    def test_blank_input(self):
        """Test blank input handling."""
        result = emotion_detector("")
        self.assertEqual(result["status_code"], 400)
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()