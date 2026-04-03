import os
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from TeraboxDL import TeraboxDL

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
COOKIE = os.getenv("TERABOX_COOKIE", "")
# Some Terabox libraries require the 'ndus' cookie specifically
downloader = TeraboxDL(COOKIE)

@app.get("/")
async def read_index():
    # Ensure index.html is in the same directory
    return FileResponse('index.html')

@app.get("/api/extract")
async def extract(url: str):
    if not url:
        return {"status": "error", "message": "No URL provided"}

    # 1. Resolve DiskWala Redirects
    if "diskwala" in url:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            r = requests.get(url, headers=headers, allow_redirects=True, timeout=10)
            url = r.url
        except Exception:
            return {"status": "error", "message": "Failed to resolve DiskWala redirect"}

    # 2. Extract Link
    try:
        info = downloader.get_file_info(url)
        
        # Check if we actually got a link
        download_url = info.get("download_link")
        if not download_url:
            return {
                "status": "error", 
                "message": "Could not generate link. Your TERABOX_COOKIE might be expired or invalid."
            }

        return {
            "status": "success",
            "title": info.get("file_name", "Unknown Video"),
            "size": info.get("file_size", "Unknown Size"),
            "link": download_url
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
