import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from TeraboxDL import TeraboxDL
import requests

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Use Environment Variable for security on Render
COOKIE = os.getenv("TERABOX_COOKIE", "your_default_ndus_here")
downloader = TeraboxDL(COOKIE)

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get("/api/extract")
async def extract(url: str):
    # Handle DiskWala redirects to TeraBox
    if "diskwala" in url:
        try:
            r = requests.get(url, allow_redirects=True, timeout=10)
            url = r.url
        except:
            raise HTTPException(status_code=400, detail="Could not resolve DiskWala link")

    try:
        info = downloader.get_file_info(url)
        return {
            "status": "success",
            "title": info.get("file_name"),
            "size": info.get("file_size"),
            "link": info.get("download_link")
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
