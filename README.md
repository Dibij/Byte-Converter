# Byte-Converter

Byte-Converter is a Python terminal application that downloads video bytes from a cloud-hosted service (like YouTube), stores them locally after compression, and converts those bytes into a normal mathematical number.

## Features
- Download video bytes from cloud platforms.
- Compress downloaded bytes efficiently on the local device.
- Convert compressed bytes to a massive mathematical representation.

## How It Works
The pipeline consists of three main steps:
1. **Download**: Uses `yt-dlp` to download the best available MP4 video from a given URL.
2. **Compress**: Reads the video file and compresses it using Python's built-in `gzip` (lossless compression).
3. **Convert**: Reads the compressed `.gz` bytes and interprets them as a single big integer using `int.from_bytes()`.

> **Warning**: A 100 MB video translates to roughly 800 million bits. The resulting number is extremely large! Converting this huge mathematical number to a string for display might be slow and memory-intensive depending on your system and the video size.

## Getting Started

### Prerequisites
- Python 3.x
- `ffmpeg` installed on your system (for video merging/handling by yt-dlp)
- Python packages specified in `requirements.txt` (e.g., `yt-dlp`)

### Installation
Clone the repository, navigate into the directory, and install dependencies:
```bash
git clone https://github.com/Dibij/Byte-Converter.git
cd Byte-Converter
pip install -r requirements.txt
```

## Usage
Run the main script:
```bash
python main.py
```
You will be prompted to enter a YouTube URL. The script will download the video, compress it, convert it to a massive number, display the first 100 digits of that number, and then automatically clean up the temporary files.
