import numpy as np
from PIL import Image, ImageChops, ImageEnhance

def compute_ela(image_path: str, quality: int = 90, scale: int = 15) -> np.ndarray:
    """Performs Error Level Analysis (ELA) to detect JPEG re-compression discrepancies."""
    original = Image.open(image_path).convert("RGB")
    temp_path = "temp_ela_buffer.jpg"
    original.save(temp_path, "JPEG", quality=quality)
    
    resaved = Image.open(temp_path)
    diff = ImageChops.difference(original, resaved)
    
    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    scale_factor = scale if max_diff == 0 else 255.0 / max_diff
    ela_image = ImageEnhance.Brightness(diff).enhance(scale_factor)
    
    return np.array(ela_image)