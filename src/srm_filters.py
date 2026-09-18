import cv2
import numpy as np

def get_srm_kernels():
    """Defines 3 Spatial Rich Model (SRM) high-pass noise extraction kernels."""
    # 1st-order edge filter
    q1 = np.array([[0,  0,  0,  0,  0],
                   [0, -1,  2, -1,  0],
                   [0,  2, -4,  2,  0],
                   [0, -1,  2, -1,  0],
                   [0,  0,  0,  0,  0]], dtype=np.float32) / 4.0

    # 2nd-order edge filter
    q2 = np.array([[-1,  2,  -2,  2, -1],
                   [ 2, -6,   8, -6,  2],
                   [-2,  8, -12,  8, -2],
                   [ 2, -6,   8, -6,  2],
                   [-1,  2,  -2,  2, -1]], dtype=np.float32) / 12.0

    # Square 3x3 filter
    q3 = np.array([[0, 0,  0, 0, 0],
                   [0, 0,  0, 0, 0],
                   [0, 1, -2, 1, 0],
                   [0, 0,  0, 0, 0],
                   [0, 0,  0, 0, 0]], dtype=np.float32) / 2.0

    return [q1, q2, q3]

def extract_srm_features(image_path: str) -> np.ndarray:
    """Applies SRM filters on grayscale input to extract high-frequency noise residuals."""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Image not found at {image_path}")

    kernels = get_srm_kernels()
    filtered_channels = [cv2.filter2D(img, -1, k) for k in kernels]
    return cv2.merge(filtered_channels)