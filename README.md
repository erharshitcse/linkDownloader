# 🚀 TeraBox & DiskWala Video Downloader

A lightweight, fast web application to extract direct download links from TeraBox and DiskWala. Built with **FastAPI** for the backend and **Tailwind CSS** for a clean, responsive frontend.

## 🌟 Features
* **TeraBox Support:** Extracts direct high-speed download links.
* **DiskWala Support:** Automatically resolves redirects to find the source file.
* **Mobile Friendly:** Fully responsive UI.
* **FastAPI Backend:** High performance and asynchronous processing.

---

## 🛠️ Local Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python main.py
    ```
    Access the site at `http://127.0.0.1:8000`.

---

## 🚀 Deployment (Render + GitHub)

1.  **Push to GitHub:** Upload `main.py`, `index.html`, `requirements.txt`, and `runtime.txt` to your repo.
2.  **Create Web Service on Render:**
    * Connect your GitHub repo.
    * **Build Command:** `pip install -r requirements.txt`
    * **Start Command:** `python main.py`
3.  **Environment Variables (CRITICAL):**
    * Go to **Environment** settings in Render.
    * Add a variable: `TERABOX_COOKIE`
    * Value: Your TeraBox `ndus` cookie (Found in Browser Inspect -> Application -> Cookies).

---

## ⚠️ Important Notes

* **Cookies:** TeraBox links often require a valid user cookie (`ndus`). If downloads fail, update your environment variable with a fresh cookie.
* **Legal:** This tool is for educational purposes. Please respect the Terms of Service of the file-hosting providers.
* **Maintenance:** If the extraction fails, check for updates to the `terabox-downloader` library on GitHub.

---

## 📂 Project Structure
* `main.py` - FastAPI backend logic.
* `index.html` - Single Page Application (SPA) frontend.
* `requirements.txt` - Python dependencies.
* `runtime.txt` - Specifies Python version for deployment.