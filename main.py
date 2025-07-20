from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import os

app = FastAPI()

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Add session middleware for in-memory notes (non-persistent)
app.add_middleware(SessionMiddleware, secret_key="dev-secret-key")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    notes = request.session.get("notes", [])
    return templates.TemplateResponse("index.html", {"request": request, "notes": notes})

@app.post("/add-note", response_class=HTMLResponse)
def add_note(request: Request, note: str = Form(...)):
    notes = request.session.get("notes", [])
    notes.append(note)
    request.session["notes"] = notes
    # If htmx request, return just the notes list
    if request.headers.get("hx-request"):
        return templates.TemplateResponse("_notes.html", {"request": request, "notes": notes})
    return RedirectResponse("/", status_code=303)