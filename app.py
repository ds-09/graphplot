from fastapi import FastAPI, File, UploadFile
import json
from datetime import datetime,date

app=FastAPI(debug=True)
with open('plot.json','r') as f:
    fileData= json.load(f)

@app.get('/range/{start}/{end}')

async def xrange(start: date, end: date):
    x= fileData["X"]
    y= fileData["Y"]
    X_list=[]
    Y_list=[]
    for i in range(len(x)):
        datetime_obj = datetime.strptime(x[i], "%Y-%m-%dT%H:%M:%S").date()  # Convert string to date object
        date_obj = datetime_obj.date()
        if start < date_obj < end:
            X_list.append(x[i])
            Y_list.append(y[i])
           
    return {"X":X_list, "Y":Y_list}



