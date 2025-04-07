import numpy as np
from skimage.metrics import structural_similarity as ssim

def mean_squared_error(matrix_1, matrix_2):
    return np.mean((matrix_1 - matrix_2) ** 2)

def root_mean_squared_error(matrix_1, matrix_2):
    return np.sqrt(mean_squared_error(matrix_1, matrix_2))

def structural_similarity(matrix_1, matrix_2):
    return ssim(matrix_1, matrix_2, data_range=matrix_1.max() - matrix_1.min())

def peak_signal_to_noise_ratio(matrix_1, matrix_2):
    mse = mean_squared_error(matrix_1, matrix_2)
    if mse == 0:
        return float('inf')  # Perfect reconstruction
    max_pixel = np.max(matrix_1)
    return 10 * np.log10((max_pixel ** 2) / mse)

def explained_variance_score(matrix_1, matrix_2):
    variance_original = np.var(matrix_1)
    variance_error = np.var(matrix_1 - matrix_2)
    return 1 - (variance_error / variance_original)

def frobenius_norm_error(matrix_1, matrix_2):
    return np.linalg.norm(matrix_1 - matrix_2, 'fro')