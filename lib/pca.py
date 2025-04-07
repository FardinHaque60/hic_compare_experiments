import numpy as np
from sklearn.decomposition import PCA

def collect_windows(matrix, window_size):
    """ Extracts all sliding windows from the matrix for PCA. """
    m, n = matrix.shape
    windows = []

    for i in range(0, m - window_size + 1):
        for j in range(0, n - window_size + 1):
            window = matrix[i:i+window_size, j:j+window_size].flatten()
            windows.append(window)  # Collect all windows

    return np.array(windows)

def reconstruct_from_windows(windows, original_shape, window_size):
    """
    Reassemble a matrix from overlapping windows.
    This averages overlapping regions to smooth out reconstructions.
    """
    reconstructed = np.zeros(original_shape)
    count = np.zeros(original_shape)

    idx = 0
    for i in range(original_shape[0] - window_size + 1):
        for j in range(original_shape[1] - window_size + 1):
            reconstructed[i:i+window_size, j:j+window_size] += windows[idx].reshape((window_size, window_size))
            count[i:i+window_size, j:j+window_size] += 1
            idx += 1

    return reconstructed / np.maximum(count, 1)  # Avoid division by zero

def apply_pca(matrix, window_size=3, n_components=0.95):
    """
    Apply PCA to sliding windows and reconstruct the matrix with the same shape.
    """
    windows = collect_windows(matrix, window_size)  # Get windows (flattened)
    
    pca = PCA(n_components=n_components)
    transformed_windows = pca.fit_transform(windows)  # Reduce dimensionality
    reconstructed_windows = pca.inverse_transform(transformed_windows)  # Reconstruct
    
    # Reshape reconstructed windows back to original form
    reconstructed_matrix = reconstruct_from_windows(reconstructed_windows, matrix.shape, window_size)

    return reconstructed_matrix