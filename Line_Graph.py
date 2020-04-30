'''
This program displays a line graph for sales over 10 years.
Autor: April Carchedi
'''
import matplotlib.pyplot as plt

def main():
    # Lists for X and Y coordinates.
    x_coords = [2009, 2010, 2011, 2012, 2013, 2014,
             2015, 2016, 2017, 2018]
    y_coords = [175000, 250000, 525000, 239000, 1000000,
             1000500, 500000, 740000, 5625000,
             100000000]
    # Create line graph.
    plt.plot(x_coords, y_coords)
    
    # Create title and lables.

    plt.title('Sales Line Graph')
    plt.xlabel('10 Years')
    plt.ylabel('Sales amount in $')

    # Create grid.
    plt.grid(True)

    # Display the line graph.
    plt.show()

# Call main function.
main()
