import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


def read_data(unlabelled_data):
    data = pd.read_csv(unlabelled_data, names = ['first column', 'second column'])
    first_column = data.iloc[:, 0].values
    second_column = data.iloc[:, 1].values
    return data, first_column, second_column
    
def plotting_data(first_column, second_column):
    # en linje genom data
    k = -1
    m = 0
    X_values = np.linspace(min(first_column), max(first_column), 100)
    y_values = k * X_values + m 
    plt.scatter(first_column, second_column, label = 'Data points')
    plt.plot(X_values, y_values , color = 'blue', label = 'Fitted line')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Data and fitted line')
    plt.show()
    
    # returerar linjens lutning 
    return k , m 



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
    X_values = np.linspace(min(first_column), max(first_column), 100)
    y_values = k * X_values + m 
    plt.plot(X_values, y_values, color='blue', label=f'Fitted Line: y = {k:.2f}x + {m:.2f}')
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

        


