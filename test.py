import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = "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"

engine = pyttsx3.init('dummy')

def transcribeAudioToText(fileName):
    recognizer = sr.Recognizer()

    with sr.AudioFile(fileName) as source:
        audio = recognizer.record(source)
    
    try:
        return recognizer.recognize_google(audio)
    except Exception:
        print("Error: ", Exception)

def generateResponse (prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )

    return response["choices"][0]["text"]

def speakText(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print("Say 'Geninus' to start recording your question...")

        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)

            try:
                transcription = recognizer.recognize(audio)

                if transcription:
                    fileName = "input.wav"

                    print("You said: ", transcription)

                    print("Say your question")
            
            except Exception:
                print("An error occurred: ", Exception)

if __name__ == "__main__":
    main()