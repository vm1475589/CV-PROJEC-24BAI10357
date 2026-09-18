cat << 'EOF' > README.md
# image-manipulation-analysis-24BAI10320

A dual-stream computer vision forensic pipeline combining Spatial Rich Model (SRM) filtering and Error Level Analysis (ELA) to detect and localize digital image tampering.

## Project Overview
This project provides a command-line-driven digital forensic tool that exposes subtle image modifications, such as copy-move and splicing forgery, by analyzing high-frequency spatial noise residuals and local JPEG compression inconsistencies.

## Features
- **SRM Noise Extraction:** Applies specialized 5x5 high-pass filters to isolate sensor noise patterns.
- **Error Level Analysis (ELA):** Evaluates re-compression artifacts to highlight manipulated regions.
- **Headless CLI Workflow:** Fully executable via the terminal without requiring GUI windows.
- **Automated Testing Suite:** Includes unit tests verifying pipeline shape and execution consistency.

## Technologies Used
- Python 3.10+
- OpenCV (Headless)
- NumPy
- Pillow (PIL)

## Installation & Setup

Clone the repository and install dependencies locally:

```bash
git clone https://github.com/akhil952/image-manipulation-analysis-24BAI10320.git
cd image-manipulation-analysis-24BAI10320
pip install -r requirements.txt
