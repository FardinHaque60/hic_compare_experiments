import numpy as np
import cv2

def add_noise_and_blur(matrix: np.array, noise_level: float, blur_strength: int) -> np.array:
    """
    Add noise and apply blur to a Hi-C matrix.

    Parameters:
        matrix (np.array): Input Hi-C matrix with values between 0 and 0.03.
        noise_level (float): The standard deviation of Gaussian noise.
        blur_strength (int): Kernel size for the blur effect (should be an odd number).

    Returns:
        np.array: The modified matrix with noise and blur.
    """
    # Add Gaussian noise
    noise = np.random.normal(0, noise_level, matrix.shape)
    noisy_matrix = matrix + noise

    # Clip values to keep them within the original range
    # noisy_matrix = np.clip(noisy_matrix, 0, 0.03)

    # Apply Gaussian blur (blur_strength should be odd)
    if blur_strength % 2 == 0:
        blur_strength += 1  # Ensure it's odd
    
    blurred_matrix = cv2.GaussianBlur(noisy_matrix, (blur_strength, blur_strength), 0)

    return blurred_matrix