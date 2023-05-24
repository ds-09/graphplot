from fastapi import FastAPI, File, UploadFile
import json

app=FastAPI(debug=True)

fileData=None

@app.post('/data')
async def upload(f: UploadFile= File()):
    global fileData
    fileData=json.load(f.file)
    return {"message":"File uploaded successfully."}

@app.get('/range/{start}/{end}')

async def xrange(start: int, end: int):
    x= fileData["X"]
    y= fileData["Y"]
    X_list=[]
    Y_list=[]
    for i in range(0, len(x)):
        if (start<x[i]<end):
            X_list.append(x[i])
            Y_list.append(y[i])
        
    return {"X":X_list, "Y":Y_list}



