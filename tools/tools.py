from crewai.tools import BaseTool
import random

class MoodClassifierTool(BaseTool):
    name: str = "mood_classifier"
    description: str = "Classifies the user's emotional mood from a text input like 'I'm feeling tired and down'"

    def _run(self, input_text: str) -> str:
        input_text = input_text.lower()
        if "stress" in input_text or "anxious" in input_text:
            return "stressed"
        elif "sad" in input_text or "down" in input_text:
            return "sad"
        elif "happy" in input_text or "excited" in input_text:
            return "happy"
        elif "angry" in input_text:
            return "angry"
        else:
            return "neutral"

class QuoteTool(BaseTool):
    name: str = "quote_tool"
    description: str = "Returns a motivational or positive quote based on the user's mood"

    def _run(self, mood: str) -> str:
        quotes = {
            "stressed": [
                "Take a deep breath. You’re doing better than you think. 💆‍♂️",
                "Storms make trees take deeper roots. 🌳"
            ],
            "sad": [
                "Every day may not be good... but there is something good in every day. 🌤️",
                "Tough times never last, but tough people do. 💪"
            ],
            "happy": [
                "Keep that smile going — you’re glowing! 😄",
                "Happiness is contagious, spread it around! 🌟"
            ],
            "angry": [
                "Breathe in calm, breathe out tension. 🧘‍♂️",
                "Pause. Feel. Respond. Not React. 🔁"
            ],
            "neutral": [
                "You're capable of amazing things. 🌈",
                "Stay present, stay grounded. 🌱"
            ]
        }
        return random.choice(quotes.get(mood, quotes["neutral"]))