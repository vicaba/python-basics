import matplotlib.pyplot as plt

if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.bar([1, 2, 3, 4], [1, 4, 9, 5])
    # Parameter 1 is an array containing the points on the x-axis
    # Parameter 2 is an array containing the points on the y-axis
    fig.savefig('myfig.png', dpi=fig.dpi)
    plt.show()
