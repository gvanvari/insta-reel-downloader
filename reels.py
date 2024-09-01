import sys
from instascrape import Reel

def download_reel(url):
    try:
        
        """
        1. login instagram web
        2. open dev tools
        3. go to applications tab
        4. click on storage
        5. copy sessionid
        """
        session_id = ""
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
            "cookie":f'sessionid={session_id};'
            }

        # Create a Reel object
        reel = Reel(url)
        
        # Scrape the reel data
        reel.scrape(headers=headers)
        
        # # Generate a filename based on the reel's shortcode
        filename = "downloads.mp4"
        print(filename)
        
        # # Download the video
        reel.download(filename)
        
        # print(f"Reel downloaded successfully as {filename}")
    except Exception as e:
        print(f"Error downloading reel: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python reel.py <reel_url>")
    else:
        reel_url = sys.argv[1]
        download_reel(str(reel_url))