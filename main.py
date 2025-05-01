from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Fake users dictionary (use a secure database in production)
users_db = {
    "user@example.com": {
        "password": "password123",  # Simple password, don't use this in 
real apps
    }
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    # Check if the email exists and if the password matches
    if email not in users_db or users_db[email]["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # If login is successful, you can redirect or send a success message
    print(f"Login successful for {email}")
    return RedirectResponse("/", status_code=302)

