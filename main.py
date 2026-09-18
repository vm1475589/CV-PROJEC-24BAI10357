import argparse
import os
import cv2
from src.inference import detect_manipulation

def main():
    parser = argparse.ArgumentParser(description="Image Manipulation & Forgery Detection CLI")
    parser.add_argument("--input", type=str, required=True, help="Path to input image")
    parser.add_argument("--output_dir", type=str, default="results", help="Directory for output files")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    
    print(f"[INFO] Inspecting {args.input}...")
    mask = detect_manipulation(args.input)
    
    output_path = os.path.join(args.output_dir, "detected_tamper_mask.png")
    cv2.imwrite(output_path, mask)
    print(f"[SUCCESS] Tampering mask saved to: {output_path}")

if __name__ == "__main__":
    main()