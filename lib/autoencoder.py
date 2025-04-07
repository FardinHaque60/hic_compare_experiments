from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler

# Build Autoencoder
def build_autoencoder(input_dim, encoding_dim):
    model = Sequential()
    model.add(Dense(encoding_dim, input_dim=input_dim, activation='relu'))
    model.add(Dense(input_dim, activation='linear'))  # Linear output activation
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def apply_autoencoder(matrix, encode_dim=40):
    model = build_autoencoder(input_dim=len(matrix), encoding_dim=encode_dim)
    # Normalize the matrix
    scaler = MinMaxScaler()
    matrix_scaled = scaler.fit_transform(matrix)
    
    model.fit(matrix_scaled, matrix_scaled, epochs=50, batch_size=32)
    denoised_matrix_scaled = model.predict(matrix_scaled) # denoise
    
    denoised_matrix = scaler.inverse_transform(denoised_matrix_scaled) # rescale
    return denoised_matrix