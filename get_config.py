from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response, JSONResponse, FileResponse
import os 

import json

app = FastAPI()

MEDIA_ROOT = os.path.join(f'{os.path.dirname(os.path.abspath(__file__))}', 'dicom_data')


@app.get("/config_json.json")
async def get_study_metadata():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # json_file_path = os.path.join(current_dir, 'config_json.json')
    json_file_path = os.path.join(current_dir, 'LIDC-IDRI-0001.json')

    print(json_file_path)
    return FileResponse(json_file_path, media_type='application/json')
    
if __name__() == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
