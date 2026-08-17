import os
import sys

def convert_mp4_to_bytes(input_path="video.mp4", output_hex_path="video_bytes.txt"):
    """
    Reads an MP4 file and converts it to raw bytes.
    Also prints statistics and saves a hex representation.
    """
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found.")
        return None

    print(f"Reading '{input_path}'...")
    try:
        with open(input_path, 'rb') as f:
            byte_data = f.read()
        
        size_bytes = len(byte_data)
        size_mb = size_bytes / (1024 * 1024)
        print(f"Successfully read {size_bytes} bytes (~{size_mb:.2f} MB).")
        
        # Display sample bytes
        print("\n--- Byte Samples ---")
        print(f"First 50 bytes (hex): {byte_data[:50].hex()}")
        print(f"First 50 bytes (decimal integers): {list(byte_data[:50])}")
        
        # Save hex output
        if output_hex_path:
            print(f"\nWriting hex representation to '{output_hex_path}'...")
            with open(output_hex_path, 'w', encoding='utf-8') as out_f:
                out_f.write(byte_data.hex())
            print(f"Hex representation saved successfully.")
            
        return byte_data

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    video_path = "video.mp4"
    if len(sys.argv) > 1:
        video_path = sys.argv[1]
    
    convert_mp4_to_bytes(video_path)
