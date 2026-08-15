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

## Estimating Size and Number Scale
Video sizes are largely determined by **Bitrate × Duration**, not just resolution. Here is a rough guide for standard YouTube videos (using codecs like H.264/VP9) per minute of video, and the resulting mathematical number length:

| Quality | Rough Bitrate | Approx. Size per Minute | Decimal Digits of the Huge Number |
|---|---|---|---|
| **144p** | ~100 Kbps | ~0.75 MB / min | ~1.8 Million digits |
| **360p** | ~400 Kbps | ~3.0 MB / min | ~7.2 Million digits |
| **720p (HD)** | ~2.5 Mbps | ~18.7 MB / min | ~45.0 Million digits |
| **1080p (FHD)**| ~5.0 Mbps | ~37.5 MB / min | ~90.3 Million digits |
| **4K (UHD)** | ~20 Mbps | ~150.0 MB / min | ~361.0 Million digits |

**Why so many digits?**  
Every byte has 8 bits (256 possible values). In a base-10 number system, each byte requires roughly ~2.408 decimal digits. Therefore, a 1 MB file (1,048,576 bytes) translates to an integer that is approximately **2.52 million digits long**!

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
