# Request Files

from fastapi import FastAPI, File, UploadFile,Header,Query
app = FastAPI()


# Define File Parameters

@app.post("/files/")
async def create_file(file: bytes = File(description="A file read as bytes")):
    return {"file_size": len(file.name)}

@app.post("/uploadfile/")
async def create_upload_file(file : UploadFile=File(description="A file read as UploadFile")):
    return {"filename": file.filename}