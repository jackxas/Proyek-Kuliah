import numpy as np

# Fungsi untuk menghitung determinan matriks 2x2
def determinan_2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]

# Fungsi untuk menghitung determinan matriks 3x3
def determinan_3x3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])) - \
           (m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])) + \
           (m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

# Fungsi untuk menghitung adjoint matriks 2x2
def adjoin_2x2(m):
    return np.array([[m[1][1], -m[0][1]], 
                     [-m[1][0], m[0][0]]])

# Fungsi untuk menghitung adjoint matriks 3x3
def adjoin_3x3(m):
    # Matriks kofaktor untuk 3x3
    cofactors = np.array([
        [determinan_2x2(np.delete(np.delete(m, 0, axis=0), 0, axis=1)), 
         -determinan_2x2(np.delete(np.delete(m, 0, axis=0), 1, axis=1)), 
         determinan_2x2(np.delete(np.delete(m, 0, axis=0), 2, axis=1))],
        
        [-determinan_2x2(np.delete(np.delete(m, 1, axis=0), 0, axis=1)), 
         determinan_2x2(np.delete(np.delete(m, 1, axis=0), 1, axis=1)), 
         -determinan_2x2(np.delete(np.delete(m, 1, axis=0), 2, axis=1))],
        
        [determinan_2x2(np.delete(np.delete(m, 2, axis=0), 0, axis=1)), 
         -determinan_2x2(np.delete(np.delete(m, 2, axis=0), 1, axis=1)), 
         determinan_2x2(np.delete(np.delete(m, 2, axis=0), 2, axis=1))]
    ])
    
    # Adjoint adalah transpos dari matriks kofaktor
    return cofactors.T

# Fungsi untuk menghitung invers matriks 2x2
def inverse_2x2(m):
    det = determinan_2x2(m)
    if det == 0:
        return None  # Matriks tidak dapat diinverskan
    adj = adjoin_2x2(m)
    return adj / det

# Fungsi untuk menghitung invers matriks 3x3
def inverse_3x3(m):
    det = determinan_3x3(m)
    if det == 0:
        return None  # Matriks tidak dapat diinverskan
    adj = adjoin_3x3(m)
    return adj / det

# Fungsi untuk memasukkan matriks dari input pengguna
def input_matrix(rows, cols):
    matrix = []
    print(f"Masukkan elemen matriks {rows}x{cols}:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Elemen [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)

# Main Program
def main():
    print("Program untuk menghitung Determinan, Adjoin, dan Invers Matriks.")
    option = int(input("Pilih ukuran matriks (2 untuk matriks 2x2, 3 untuk matriks 3x3): "))
    
    if option == 2:
        matrix = input_matrix(2, 2)
        print("\nMatriks 2x2:")
        print(matrix)
        
        # Determinan 2x2
        det = determinan_2x2(matrix)
        print(f"Determinant: {det}")
        
        # Adjoin 2x2
        adj = adjoin_2x2(matrix)
        print(f"Adjoin Matriks: \n{adj}")
        
        # Invers 2x2
        inv = inverse_2x2(matrix)
        if inv is None:
            print("Matriks tidak dapat diinverskan.")
        else:
            print(f"Invers Matriks: \n{inv}")
    
    elif option == 3:
        matrix = input_matrix(3, 3)
        print("\nMatriks 3x3:")
        print(matrix)
        
        # Determinan 3x3
        det = determinan_3x3(matrix)
        print(f"Determinant: {det}")
        
        # Adjoin 3x3
        adj = adjoin_3x3(matrix)
        print(f"Adjoin Matriks: \n{adj}")
        
        # Invers 3x3
        inv = inverse_3x3(matrix)
        if inv is None:
            print("Matriks tidak dapat diinverskan.")
        else:
            print(f"Invers Matriks: \n{inv}")
    
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()