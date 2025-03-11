import codecademylib3
import numpy as np
import pandas as pd
calorie_stats = np.genfromtxt('cereal.csv', delimiter = ',')
#calorie_stats_df = pd.read_csv('cereal.csv')
calories_param = {
'average_calories' : np.mean(calorie_stats),
'calorie_stats_sorted' : np.sort(calorie_stats),
'median_calories' : np.median(calorie_stats),
'nth_percentiles' : np.percentile(calorie_stats, 4),
'more_calories' : np.mean(calorie_stats>60) * 100,
'calorie_std' : np.std(calorie_stats)
}

for key, val in calories_param.items():
  print(f'{key}: {val}\n' )

