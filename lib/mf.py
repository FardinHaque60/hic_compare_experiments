from sklearn.decomposition import TruncatedSVD

def matrix_factorization(matrix, n_components=15):
    svd = TruncatedSVD(n_components=n_components)
    return svd.fit_transform(matrix).dot(svd.components_)