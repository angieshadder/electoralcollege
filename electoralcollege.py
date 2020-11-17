import pandas as pd
from random import choice as ch
import matplotlib.pyplot as plt

state_data = pd.read_csv("electoral_data.csv")

choice_list = ["R", "B"]

new_col = []
for row, value in enumerate(state_data.values):
    if value[2] == "P":
        new_col.append(ch(choice_list))
    else:
        new_col.append(value[2])

state_data["Winner"] = new_col

graphable_data = state_data.pivot_table(index="Winner", values="electoral_votes", aggfunc=sum).reset_index()

graphable_data.plot(kind="bar", x="Winner", y="electoral_votes", color=['blue', 'red'])


print(state_data)

plt.show()



