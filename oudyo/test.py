from faster_whisper import WhisperModel

class AudioTranscriber:
    def __init__(self, model_size="tiny"):
        # מודלים: tiny, base, small, medium, large
        self.model = WhisperModel(model_size)

    def transcribe(self, file_path: str) -> str:
        segments, info = self.model.transcribe(file_path)
        text = ""
        for segment in segments:
            text += segment.text + "\n"
        return text.strip()


if __name__ == "__main__":
    transcriber = AudioTranscriber()
    text = transcriber.transcribe("C:/Users/User/Downloads/Telegram Desktop/6. Rap God.mp3")
    print("Transcribed text:")
    print(text)