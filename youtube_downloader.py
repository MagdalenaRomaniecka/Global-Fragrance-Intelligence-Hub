import yt_dlp

class YouTubeDownloader:
    def __init__(self, output_template: str = "YouTube_Podcast.%(ext)s"):
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
                'preferredquality': '192',
            }],
            'outtmpl': output_template,
            'quiet': False
        }

    def download_audio(self, url: str) -> bool:
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([url])
            return True
        except Exception as e:
            print(f"Download error: {e}")
            return False

if __name__ == "__main__":
    downloader = YouTubeDownloader()
    video_url = "https://www.youtube.com/watch?v=DyLiHTcQn4I"
    downloader.download_audio(video_url)