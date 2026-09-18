import os
import unittest
import numpy as np
import cv2
from src.srm_filters import get_srm_kernels, extract_srm_features
from src.preprocessing import compute_ela
from src.inference import detect_manipulation

class TestImageForensicsPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.makedirs("tests/temp", exist_ok=True)
        cls.dummy_image_path = "tests/temp/dummy.jpg"
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.rectangle(img, (25, 25), (75, 75), (255, 255, 255), -1)
        cv2.imwrite(cls.dummy_image_path, img)

    def test_srm_kernel_shapes(self):
        kernels = get_srm_kernels()
        self.assertEqual(len(kernels), 3)
        for k in kernels:
            self.assertEqual(k.shape, (5, 5))

    def test_srm_extraction(self):
        srm_features = extract_srm_features(self.dummy_image_path)
        self.assertEqual(srm_features.shape[:2], (100, 100))
        self.assertEqual(srm_features.shape[2], 3)

    def test_ela_computation(self):
        ela = compute_ela(self.dummy_image_path)
        self.assertEqual(ela.shape[:2], (100, 100))

    def test_end_to_end_inference(self):
        mask = detect_manipulation(self.dummy_image_path)
        self.assertEqual(mask.shape, (100, 100))

    @classmethod
    def tearDownClass(cls):
        if os.path.exists("tests/temp/dummy.jpg"):
            os.remove("tests/temp/dummy.jpg")
        if os.path.exists("tests/temp"):
            os.rmdir("tests/temp")
        if os.path.exists("temp_ela_buffer.jpg"):
            os.remove("temp_ela_buffer.jpg")

if __name__ == "__main__":
    unittest.main()