import openai
import pyttsx3
import speech_recognition as sr

# get openai key from .env
openai.api_key = ""

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
                transcription = recognizer.recognize_google(audio)

                if transcription.lower() == "genious":
                    fileName = "input.wav"

                    print("Say your question")

                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)

                        with open(fileName, "wb") as f:
                            f.write(audio.get_wav_data())
                    
                    text = transcribeAudioToText(fileName)

                    if text:
                        print(f"You said: {text}")

                        response = generateResponse(text)

                        print(f"Chat GPT says: {response}")

                        speakText(response)
            
            except Exception:
                print("An error occurred: ", Exception)

if __name__ == "__main__":
    main()