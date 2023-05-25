import json
from datetime import datetime,date

with open('plot.json','r') as f:
    fileData= json.load(f)
x= fileData["X"]
y= fileData["Y"]
X_list=[]
Y_list=[]
start = datetime.fromisoformat('2023-01-01')
end = datetime.fromisoformat('2025-01-01')
for i in range(len(x)):
    datetime_obj = datetime.fromisoformat(x[i])  # Convert string to datetime object
    if start < datetime_obj < end:
        X_list.append(datetime_obj.strftime('%H:%M:%S'))
        Y_list.append(y[i])
print("X",X_list,"\n",Y_list)