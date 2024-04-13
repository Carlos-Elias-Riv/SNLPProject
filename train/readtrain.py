# we will replace every \t with a comma and save it in a new file

import pandas as pd

train = pd.read_csv("train.csv", sep = "\t", on_bad_lines='warn')


print(train)
