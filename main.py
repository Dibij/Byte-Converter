import yt_dlp
import gzip
import shutil
import os
import sys

# Increase the limit for integer string conversion to handle massive numbers
# Without this, Python 3.11+ raises an error for str(big_number)
sys.set_int_max_str_digits(0) 

def download_video(url, output_path="video.mp4"):
    print(f"Downloading video from {url}...")
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': output_path,
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Video downloaded to {output_path}")
    return output_path

def compress_file(input_path, output_path="video.gz"):
    print(f"Compressing {input_path}...")
    with open(input_path, 'rb') as f_in:
        with gzip.open(output_path, 'wb', compresslevel=9) as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"File compressed to {output_path}")
    return output_path

def read_compressed_as_number(compressed_path):
    print(f"Converting {compressed_path} to an integer...")
    with open(compressed_path, 'rb') as f:
        data = f.read()
    return int.from_bytes(data, 'big')

def main():
    try:
        url = input("Enter YouTube URL: ")
        if not url.strip():
            print("Invalid URL.")
            return
            
        video_file = download_video(url)
        compressed_file = compress_file(video_file)
        big_number = read_compressed_as_number(compressed_file)
        
        # Get the actual size of the compressed file
        file_size = os.path.getsize(compressed_file)
        print(f"\nNumber of bytes in compressed file: {file_size}")
        
        print("Converting the big number to a string to display the first 100 digits... (This may take a while depending on file size)")
        number_str = str(big_number)
        print(f"First 100 digits of the big number: {number_str[:100]}...")
        
        # Clean up
        print("Cleaning up temporary files...")
        os.remove(video_file)
        os.remove(compressed_file)
        print("Done!")
    except Exception as e:
        print(f"An error occurred: {e}")
        # Attempt cleanup on failure
        if os.path.exists("video.mp4"): os.remove("video.mp4")
        if os.path.exists("video.gz"): os.remove("video.gz")

if __name__ == "__main__":
    main()
