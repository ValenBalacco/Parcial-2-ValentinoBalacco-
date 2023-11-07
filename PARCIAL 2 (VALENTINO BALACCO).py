# Función para verificar si una secuencia es mutante
def is_mutant(sequence):
    count = 1  # Contador de letras empieza en 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            count += 1  # Incrementa el contador si la letra es igual a la anterior
        else:
            count = 1  # Reinicia el contador si no son iguales
        if count >= 4:
            return True  # Si hay una secuencia de 4 letras iguales es gen mutante
    return False

# Función para construir la matriz de ADN
def build_adn_matrix():
    matrix = []
    for n in range(6):
        row = input("Ingrese una fila de ADN (6 letras A, T, C, o G): ").upper()
        if len(row) == 6:
            valid = True
            for base in row:
                if base not in 'ATCG':
                    valid = False
                    break
            if valid:
                matrix.append(row)
            else:
                print("La fila ingresada es inválida. Solo se permite letras A, T, C o G.")
                return None
        else:
            print("La fila ingresada es inválida. Solo se permite exactamente 6 letras.")
            return None
    return matrix

# Funcion para verificar si la matriz contiene genes mutantes
def have_mutant_gens(matrix):
    distinct_sequences = []# Contador de secuencias distintas
    for i in range(6):
        for j in range(6):
            # Verificar horizontal
            if j + 3 < 6:
                sequence = matrix[i][j:j+4]
                if is_mutant(sequence):
                    distinct_sequences.append(sequence)
            # Verificar vertical
            if i + 3 < 6:
                sequence = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j]
                if is_mutant(sequence):
                    distinct_sequences.append(sequence)
            # Verificar diagonal
            if i + 3 < 6 and j + 3 < 6:
                sequence = matrix[i][j] + matrix[i+1][j+1] + matrix[i+2][j+2] + matrix[i+3][j+3]
                if is_mutant(sequence):
                    distinct_sequences.append(sequence)
            # Verificar diagonal opuesta
            if i + 3 < 6 and j - 3 >= 0:
                sequence = matrix[i][j] + matrix[i+1][j-1] + matrix[i+2][j-2] + matrix[i+3][j-3]
                if is_mutant(sequence):
                    distinct_sequences.append(sequence)
                    
    return len(distinct_sequences) > 1 # Es mutante si tiene almenos  dos secuencias distintas de 4 letras
    
# Main 
if __name__ == "__main__":
    while True:
        print("Menú:") #Inicia el Menú
        print("1. Ingresar matriz de ADN")
        print("2. Salir")
        choice = input("Elija una opción: ")
       
        if choice == "1":
            adn_matrix = build_adn_matrix()
            
          # Caso mutante
#            adn_matrix = ['ATGCGA','CAGTGC','TTATGT','AGAAGG','CCCCTA','TCACTG']
          
          # Caso no mutante
#            adn_matrix = ['ATATAT','CGGTCG','TCGGCT','TTCCGG','AAGCGC','AATTAT']
             
            print(adn_matrix)

            if adn_matrix:
                if have_mutant_gens(adn_matrix):
                    print("El ADN es de un mutante!")
                else:
                    print("El ADN no es de un mutante!")
        elif choice == "2":
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")