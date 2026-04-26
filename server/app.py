from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (important if frontend calls API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= API ROUTES =================
# (keep your existing /reset, /step, /health here)

# ================= FRONTEND =================

# Serve static assets
app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets")

# Root → UI
@app.get("/")
def serve_ui():
    return FileResponse("dist/index.html")

# React routing support
@app.get("/{full_path:path}")
def serve_react_app(full_path: str):
    return FileResponse("dist/index.html")