from t_pop.collections.adapters.location_guard import TwoDLocationGuardAdapter
from t_pop.collections.components.containers import Containers
from t_pop.processes.agent_generator import car_generator
from t_pop.processes.results import results
from t_pop.algorithms.tpop import TPoP, Tree

import pandas as pd
import os


def simulator_setup(environment_size:list[tuple, tuple], number_of_cars:int, p_c:float, p_h:float):

    #location cache creation
    location_adapter = TwoDLocationGuardAdapter(environment_size)

    cars = car_generator(p_c, p_h, environment_size, number_of_cars)


    #initialise the empty container dictionaries, these will have the position as key and the car object as the value
    true_car_container_dict = {}
    fake_car_container_dict = {}

    #Assign the cars
    for i in range(number_of_cars):
        
        #putting the car into the location cache
        location_adapter.add_car(cars[i])
        #moving the car within the environment (location cache)
        #location_adapter.move_car(cars[i], time=1)

        #putting into the container dictionary the position as a key and the car class instance as the value
        true_car_container_dict.update( {cars[i].true_position_index : cars[i]} )

        #same for the dishonest cars, but using their fake position.
        if cars[i].honest is False:
            fake_car_container_dict.update( {cars[i].fake_position_index : cars[i]} )


    containers = Containers(true_car_container_dict, fake_car_container_dict)
    return cars, location_adapter, containers

def parser(simulation_number, probability_of_honest, probability_of_coerced, density, threshold, accuracy, True_Positive, True_Negative, False_Positive, False_Negative):
    if True_Positive + False_Negative:
        percent_true_positives = (True_Positive / (True_Positive + False_Negative)) * 100
    else:
        percent_true_positives = 0
    if True_Negative +  False_Positive:
        percent_true_negatives = (True_Negative / (True_Negative +  False_Positive)) * 100
    else:
        percent_true_negatives = 0
    percent_false_positives = 100 - percent_true_positives
    percent_false_negatives = 100 - percent_true_negatives

    row_list = [simulation_number, probability_of_honest, probability_of_coerced, density, threshold, accuracy,
    True_Positive, True_Negative, False_Positive, False_Negative, percent_true_positives, percent_true_negatives, 
    percent_false_positives, percent_false_negatives]

    return row_list

def simulator_caller(number_of_simulations:int, number_of_cars:int, prob_coerced:float, prob_honest:float, depth:int,
                    car_list: list, containers, location_adapter,
                    number_of_witnesses_per_depth:list, density:float, threshold:float, environment_size:list[tuple, tuple]):
    
    data = []
    for simulation_id in range(number_of_simulations):
        car_list, location_adapter, containers = simulator_setup(environment_size, number_of_cars, prob_coerced, prob_honest)
        for car in car_list:
            tree = Tree(car, depth, number_of_witnesses_per_depth, location_adapter, containers)
            TPoP(tree, threshold, number_of_witnesses_per_depth, location_adapter, containers)
        True_Positive, True_Negative, False_Positive, False_Negative, Accuracy = results(car_list)
        row = parser(simulation_id, prob_honest, prob_coerced, density, threshold, Accuracy, True_Positive, True_Negative, False_Positive, False_Negative)
        data.append(row)

    simulation_df = pd.DataFrame(data, 
    columns=['Simulation number', 'Probability of honest cars', 'Probability of coerced cars', 'Density', 
    'Threshold','Accuracy', 'True Positives', 'True Negatives', 'False Positives', 'False Negatives', 
    'Percent True Positives', 'Percent True Negatives', 'Percent False Positives','Percent False Negatives'])
    return simulation_df

def save_simulation(simulation_df, path, simulation_id):
    simulation_path = path + str(simulation_id) + '.txt'
    simulation_df.to_csv(simulation_path)

    return simulation_path

def make_directory(target_path):
    cwd = os.getcwd()
    path = cwd + target_path
    os.makedirs(path, exist_ok =True)
    return path

def full_csv(directory_path_string):
    """Given a directory pathfile with .txt files of simulation data, 
    loops through each one, reads them and creates one .csv file with 
    all the simulation data"""
    
    directory = os.fsencode(directory_path_string)
    dfs = []

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        
        if filename.endswith('.txt'):
            simulation_path = directory_path_string + filename
            data = pd.read_csv(simulation_path)
            dfs.append(data)

    return pd.concat(dfs)


