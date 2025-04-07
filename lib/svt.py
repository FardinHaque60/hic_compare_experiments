from scipy.linalg import svd
import numpy as np

def svt(matrix, threshold=0.04):
    U, S, Vt = svd(matrix, full_matrices=False)
    S_thresholded = np.maximum(S - threshold, 0)  # Shrink singular values
    return np.dot(U, np.dot(np.diag(S_thresholded), Vt))