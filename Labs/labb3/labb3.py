import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


def read_data(unlabelled_data):
    data = pd.read_csv(unlabelled_data)
    data.columns = ['first column', 'second column']
    first_column = data['first column'].values
    second_column = data['second column'].values
    return data, first_column, second_column
    
def plotting_data(first_column, second_column):
    # en linje genom data
    k, m = np.polyfit(first_column, second_column, 1)
    plt.scatter(first_column, second_column, label = 'Data points')
    plt.plot(first_column, k* first_column +m , color = 'blue', label = 'Fitted line')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Data and fitted line')
    plt.show()
    
    # returerar linjens lutning 
    return k, m 



def classify_points(data, first_column, second_column, k, m, output_file):
    label = []
    #loop igenom alla datapunkter och klassificerar dem
    for i in range(len(first_column)):
        if second_column[i] > k * first_column[i] + m:
            label.append(1)
        elif second_column[i] < k * first_column[i] +m:
            label.append(0)
        # om punkten ligger exakt på linjen
        else:
            label.append(None)
        
        
    data ['label'] = label
    # skriv DataFrame till en csv_fil
    data.to_csv(output_file, index = False)
        
    plt.scatter(data['first column'], data['second column'], c = data['label'], cmap ='viridis', label ='Classified Points')
    plt.plot(first_column, k * first_column + m, color='blue', label=f'Fitted Line: y = {k:.2f}x + {m:.2f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Classified Data with Fitted Line')
    plt.show()
        
    above_count = sum(data['label']== 1)
    below_count = sum(data['label']== 0)
    print(f"The number of points above the line: {above_count}.\nThe number of points below the line: {below_count}.")
# anrop funktioner    
data, first_col, second_col = read_data('unlabelled_data.csv')
k,m = plotting_data(first_col,second_col)
classify_points(data, first_col, second_col, k, m,'labelled_data.csv')

        


