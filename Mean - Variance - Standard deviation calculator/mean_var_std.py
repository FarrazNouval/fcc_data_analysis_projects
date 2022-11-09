import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  else:
    list_flat = np.array(list)
    list = np.array(list).reshape(3, 3)
    
    list_mean = np.mean(list_flat).tolist()
    list_var = np.var(list_flat)
    list_std = np.std(list_flat)
    list_max = list_flat.max()
    list_min = list_flat.min()
    list_sum = list_flat.sum()

    #axis 0
    mean_0 = np.mean(list, axis=0).tolist()
    var_0 = np.var(list, axis=0).tolist()
    std_0 = np.std(list, axis=0).tolist()
    max_0 = list.max(axis=0).tolist()
    min_0 = list.min(axis=0).tolist()
    sum_0 = list.sum(axis=0).tolist()

    #axis 1
    mean_1 = np.mean(list, axis=1).tolist()
    var_1 = np.var(list, axis=1).tolist()
    std_1 = np.std(list, axis=1).tolist()
    max_1 = list.max(axis=1).tolist()
    min_1 = list.min(axis=1).tolist()
    sum_1 = list.sum(axis=1).tolist()

    calculations = {
      'mean': [mean_0, mean_1, list_mean],
      'variance': [var_0, var_1, list_var],
      'standard deviation': [std_0, std_1, list_std],
      'max': [max_0, max_1, list_max],
      'min': [min_0, min_1, list_min],
      'sum': [sum_0, sum_1, list_sum]
    }

    
    return calculations
