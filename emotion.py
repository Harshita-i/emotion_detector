# import streamlit as st
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# from transformers import pipeline
# import torch
# import emoji

# # Load model and tokenizer
# @st.cache_resource
# def load_emotion_model():
#     model_name = "nateraw/bert-base-uncased-emotion"
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
#     model = AutoModelForSequenceClassification.from_pretrained(model_name)
#     return pipeline("text-classification", model=model, tokenizer=tokenizer)

# # Emotion to emoji mapping
# EMOJI_MAP = {
#     "sadness": "😢",
#     "joy": "😄",
#     "love": "❤️",
#     "anger": "😠",
#     "fear": "😱",
#     "surprise": "😲"
# }

# # Load pipeline
# emotion_classifier = load_emotion_model()

# # Streamlit UI
# st.title("🧠 Emotion Detector from Text")
# st.write("Type a sentence and get the emotion you're expressing!")

# user_input = st.text_area("Enter your text here:")

# if user_input:
#     result = emotion_classifier(user_input)[0]
#     emotion = result['label']
#     score = result['score']
#     emoji_icon = EMOJI_MAP.get(emotion, "❓")

#     st.markdown(f"### Emotion: **{emotion.capitalize()}** {emoji_icon}")
#     st.markdown(f"**Confidence:** {score:.2%}")



# import streamlit as st
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# from transformers import pipeline

# # Load model and tokenizer
# @st.cache_resource
# def load_emotion_model():
#     model_name = "nateraw/bert-base-uncased-emotion"
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
#     model = AutoModelForSequenceClassification.from_pretrained(model_name)
#     return pipeline("text-classification", model=model, tokenizer=tokenizer)

# # Emotion to emoji mapping
# EMOJI_MAP = {
#     "sadness": "😢",
#     "joy": "😄",
#     "love": "❤️",
#     "anger": "😠",
#     "fear": "😱",
#     "surprise": "😲"
# }

# # Load pipeline
# emotion_classifier = load_emotion_model()

# # Streamlit UI
# st.title("Emotion Detector from Text")
# st.write("Type a sentence and get the emotion you're expressing!")

# user_input = st.text_area("Enter your text here:")

# if user_input:
#     result = emotion_classifier(user_input)[0]
#     emotion = result['label']
#     score = result['score']
#     emoji_icon = EMOJI_MAP.get(emotion, "❓")

#     st.markdown(f"### Emotion: **{emotion.capitalize()}** {emoji_icon}")
#     st.markdown(f"**Confidence:** {score:.2%}")



import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
import random

# Load model and tokenizer
@st.cache_resource
def load_emotion_model():
    model_name = "nateraw/bert-base-uncased-emotion"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return pipeline("text-classification", model=model, tokenizer=tokenizer)

# Emotion to emoji mapping
EMOJI_MAP = {
    "sadness": "😢",
    "joy": "😄",
    "love": "❤️",
    "anger": "😠",
    "fear": "😱",
    "surprise": "😲"
}

# Emotion-based recommendations
RECOMMENDATIONS = {
    "sadness": [
        "Here's a joke: Why don’t scientists trust atoms? Because they make up everything! 😂",
        "Listen to [Happy by Pharrell Williams](https://www.youtube.com/watch?v=ZbZSe6N_BXs)",
        "Cheer up! Try [this joke site](https://www.rd.com/jokes/)"
    ],
    "joy": [
        "Go dance it out! 💃🕺",
        "Call a friend and share the joy!",
        "Make a gratitude list – joy doubles when shared."
    ],
    "love": [
        "Write a heartfelt note to someone. ❤️",
        "Watch a romantic movie you love.",
        "Send a compliment to someone randomly today!"
    ],
    "anger": [
        "Take 10 deep breaths and go for a walk.",
        "Try journaling how you feel.",
        "Punch a pillow (safely 😅), then laugh it out!"
    ],
    "fear": [
        "Ground yourself: 5 things you can see, 4 you can touch...",
        "Listen to calming sounds: [Calm Radio](https://www.calm.com/)",
        "You’ve survived 100% of your worst days — you got this!"
    ],
    "surprise": [
        "Surprised? Embrace the unknown today!",
        "Tell someone what surprised you today – share the moment.",
        "Write a short story based on your surprise!"
    ]
}

# Load classifier
emotion_classifier = load_emotion_model()

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Streamlit UI
st.title("🧠Emotion Detector with Recommendations")
st.write("Type your thoughts below. Track your emotions and get fun suggestions!")

user_input = st.text_input("Enter a message:")

if st.button("Analyze"):
    if user_input.strip() != "":
        result = emotion_classifier(user_input)[0]
        emotion = result['label']
        score = result['score']
        emoji_icon = EMOJI_MAP.get(emotion, "❓")
        suggestion = random.choice(RECOMMENDATIONS.get(emotion, ["Just breathe and relax."]))

        # Save to chat history
        st.session_state.history.append({
            "text": user_input,
            "emotion": emotion,
            "emoji": emoji_icon,
            "confidence": f"{score:.2%}",
            "suggestion": suggestion
        })

# Clear chat history button
if st.button("🗑️ Clear Chat History"):
    st.session_state.history = []
    st.success("Chat history cleared!")


# Show history
if st.session_state.history:
    st.markdown("---")
    st.subheader("🗂️ Chat History")
    for entry in reversed(st.session_state.history):
        st.markdown(f"**You:** {entry['text']}")
        st.markdown(f"**Detected Emotion:** {entry['emotion'].capitalize()} {entry['emoji']}")
        st.markdown(f"**Confidence:** {entry['confidence']}")
        st.markdown(f"**💡 Suggestion:** {entry['suggestion']}")
        st.markdown("---")
