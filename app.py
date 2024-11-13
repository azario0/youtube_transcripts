import webview
import json
import pyperclip
from langchain_community.document_loaders import YoutubeLoader

class Api:
    def get_transcript(self, video_url):
        try:
            loader = YoutubeLoader.from_youtube_url(video_url)
            documents = loader.load()
            transcript_text = documents[0].page_content
            return transcript_text
        except Exception as e:
            return f"Error retrieving transcript: {str(e)}"

    def fetch_transcript(self, video_url):
        transcript = self.get_transcript(video_url)
        return json.dumps({"transcript": transcript})

    def copy_to_clipboard(self, transcript):
        print(transcript)
        pyperclip.copy(transcript)
        return json.dumps({"message": "Transcript copied to clipboard"})

if __name__ == "__main__":
    api = Api()
    window = webview.create_window("YouTube Transcript Viewer", "web/index.html", js_api=api)
    webview.start()