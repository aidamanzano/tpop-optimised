import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def Visualise(cars:list, environment:list[tuple, tuple]) -> None:

    """Visualising cars in the environment, if they are honest they are shown in green, otherwise shown in red"""
    for car in cars:
        if car.honest == True:
            x = car.true_x
            y = car.true_y
        else:
            x = car.fake_x
            y = car.fake_y

        plt.xlim(environment[0][0], environment[0][1])
        plt.ylim(environment[1][0], environment[1][1])
        
        plt.scatter(x, y, marker="o", c = ['r' if car.honest is False else 'g'])     
    plt.grid()
    plt.show()



def simulation_violin_plots(algorithm_type: str, number_of_simulations, csv_path, x_variable:str, y_varible:str):

    os.makedirs(csv_path + 'plots/', exist_ok =True)
    
    df = pd.read_csv(csv_path)
    plt.figure(figsize=(10,5))

    ax = sns.violinplot(x=df[x_variable], y=df[y_varible], data=df)
    
    ax.set_title(algorithm_type + 'Proof of Location Protocol Accuracy, Number of Simulations = ' + str(number_of_simulations))
    ax.set_ylabel(y_varible)
    ax.set_xlabel(x_variable)

    plt.show()
    ax = ax.get_figure()
    ax.savefig(csv_path + 'plots/' + x_variable + 'violin.png')

def subplots(algorithm_type: str, directory_pathfile, number_of_simulations, x_variable:str):
    fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize=(18,12))
    fig.suptitle(algorithm_type + 'Proof of Location Protocol Classifications, Number of Simulations = ' + str(number_of_simulations))
    
    df = pd.read_csv(directory_pathfile+'full_data.csv')
    #create boxplot in each subplot

    sns.boxplot(data=df, x=x_variable, y='Percent True Positives', ax=axes[0,0])
    sns.boxplot(data=df, x=x_variable, y='Percent True Negatives', ax=axes[0,1])
    sns.boxplot(data=df, x=x_variable, y='Percent False Positives', ax=axes[1,0])
    sns.boxplot(data=df, x=x_variable, y='Percent False Negatives', ax=axes[1,1])

    ax = fig.get_figure()
    ax.savefig(directory_pathfile +'full_data.csv' + 'plots/' + 'subplots.png')

def simulation_box_plots(algorithm_type: str, number_of_simulations, csv_path, x_variable:str, y_varible:str):

    os.makedirs(csv_path + 'plots/', exist_ok =True)
    
    df = pd.read_csv(csv_path)

    plt.figure(figsize=(15,10))
    ax = sns.boxplot(x=df[x_variable], y=df[y_varible], data=df)
    
    
    ax.set_title(algorithm_type + 'Proof of Location Protocol Accuracy, Number of Simulations = ' + str(number_of_simulations))
    ax.set_ylabel(y_varible)
    ax.set_xlabel(x_variable)

    plt.show()
    
    ax = ax.get_figure()
    ax.savefig(csv_path + 'plots/' + x_variable + 'boxplot.png')
