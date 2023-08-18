import matplotlib.pyplot as plt
from dnasequence import DNASequence
from collections import Counter

def readSequencesFromFile(file_name):
    secuencias = []
    with open(file_name, 'r') as file:
        for line in file:
            name, sequence = line.strip().split(',')
            secuencias.append(DNASequence(sequence, name))
    return secuencias

def analyseSequences(sequences):
    dict = {}
    for seq in sequences:
        dict[seq.name] = seq.base_count
    return dict

def showResults(dict):
    total_count = Counter() # https://realpython.com/python-counter/
    for seq in dict.values():
        total_count += seq

    bases = list(total_count.keys())
    count = list(total_count.values())

    fig, ax = plt.subplots()

    ax.grid(axis='y', color='gray', linestyle='dashed', linewidth=0.5)
    ax.bar(bases, count)
    ax.set_xlabel('Bases')
    ax.set_ylabel('Cantidad')
    ax.set_title('Cantidad de cada base en todas las secuencias')
    plt.show()

def main():
    while True:
        file_name = input("Ingrese el nombre del archivo de secuencias de ADN (o 'salir' para terminar): ")
        if file_name.lower() == 'salir':
            break
        try:
            seqs = readSequencesFromFile(file_name)
            dict = analyseSequences(seqs)
            print(dict)
            showResults(dict)
        except Exception as e:
            print(f"Hubo un error al procesar el archivo: {str(e)}")

if __name__ == "__main__":
    main()
