import speech_recognition as sr
import pandas as pd

def speech_to_csv(csv_file):
    r = sr.Recognizer()
    df = pd.DataFrame(columns=['Name'])

    while True:
        with sr.Microphone() as source:
            print("Speak now...")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said:", text)

            # Split the text into words
            words = text.split()

            # Check for the "stop" command
            if text.lower() in ["stop stop", "stop recording", "please stop"]:
                break

            # Combine every two words into a single name
            for i in range(0, len(words), 2):
                name = " ".join(words[i:i+2])
                df = df._append({'Name': name}, ignore_index=True)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)

if __name__ == "__main__":
    csv_file = "words.csv"
    speech_to_csv(csv_file)