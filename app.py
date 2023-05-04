import os
import openai
import streamlit as st
import speech_recognition as sr
import pyttsx3

openai.api_key = "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"
r = sr.Recognizer()

def verify_news(prompt):
    prompt_text = f"{prompt} : "
    response = openai.Completion.create(
        model="text-davinci-003", prompt=prompt_text, temperature=0, max_tokens=1000
    )
    return response["choices"][0]["text"]

def text_input():
    prompt = st.text_input("HEY THERE! LET ME KNOW WHAT YOU WANT ")
    return prompt

def voice_input():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        st.write("Speak now!")
        audio = r.listen(source)
    text = r.recognize_google(audio).lower()
    return text

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    st.title("VOICE-GPT")

    prompt = ""
    option = st.radio("Choose Input Method", ("Text Input", "Voice Input"))
    if option == "Text Input":
        prompt = text_input()
    else:
        prompt = voice_input()

    if st.button("Go"):
        result = verify_news(prompt)
        st.write(result)
        text_to_speech(result)


if __name__ == "__main__":
    main()
