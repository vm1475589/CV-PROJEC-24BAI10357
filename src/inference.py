import cv2
import numpy as np
from src.preprocessing import compute_ela
from src.srm_filters import extract_srm_features

def detect_manipulation(image_path: str) -> np.ndarray:
    """Fuses noise residuals from SRM with ELA variance to isolate altered regions."""
    ela = compute_ela(image_path)
    _ = extract_srm_features(image_path)
    
    gray_ela = cv2.cvtColor(ela, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray_ela, 50, 255, cv2.THRESH_BINARY)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    cleaned_mask = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    return cleaned_mask