from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Azeez Mutton")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

MENU = [
    {
        "emoji": "🥩",
        "name": "Bone-in Curry Cut",
        "description": "Classic mixed pieces with bone — perfect for rich gravies and biryanis.",
        "weight": "500 g",
        "price": "349",
        "tag": "Best Seller",
    },
    {
        "emoji": "🍖",
        "name": "Boneless Shoulder",
        "description": "Tender, well-marbled shoulder meat. Ideal for kebabs and slow-cook curries.",
        "weight": "500 g",
        "price": "429",
        "tag": "Chef's Pick",
    },
    {
        "emoji": "🫀",
        "name": "Liver & Kidney Pack",
        "description": "Fresh offal — cleaned and ready. Great for quick fry-ups and masala dishes.",
        "weight": "250 g",
        "price": "199",
        "tag": None,
    },
    {
        "emoji": "🦴",
        "name": "Marrow Bones",
        "description": "Nutrient-rich bones sawn to size. Brilliant for paya soup and stock.",
        "weight": "1 kg",
        "price": "249",
        "tag": None,
    },
    {
        "emoji": "🍗",
        "name": "Leg of Mutton (Full)",
        "description": "Whole hind leg — slow-roast showstopper or the centrepiece of any feast.",
        "weight": "1.2–1.5 kg",
        "price": "899",
        "tag": "Weekend Special",
    },
    {
        "emoji": "🧆",
        "name": "Keema (Minced Mutton)",
        "description": "Freshly minced, never frozen. Perfect for kofta, keema pav, and stuffed parathas.",
        "weight": "500 g",
        "price": "399",
        "tag": None,
    },
]

PROCESS = [
    {
        "step": "01",
        "title": "Same-day slaughter",
        "body": "Every animal is slaughtered at our licensed facility on the morning of your order — never frozen.",
    },
    {
        "step": "02",
        "title": "Hand-trimmed & weighed",
        "body": "Master butchers trim each cut to your specification. You pay for meat, not fat.",
    },
    {
        "step": "03",
        "title": "Chilled, not frozen",
        "body": "Packed in food-grade insulated bags with ice gel and delivered within 2 hours of cutting.",
    },
    {
        "step": "04",
        "title": "At your door",
        "body": "Real-time GPS tracking. Delivery in under 60 minutes across the city — or it's free.",
    },
]

TESTIMONIALS = [
    {
        "quote": "The biryani I made with their curry cut was the best I've ever cooked. Genuinely.",
        "author": "Razia Begum",
        "locality": "Frazer Town, Bengaluru",
        "avatar": "R",
    },
    {
        "quote": "No more haggling at the market. Fresh, clean cuts delivered before breakfast. Brilliant.",
        "author": "Mohammed Irfan",
        "locality": "Shivajinagar",
        "avatar": "M",
    },
    {
        "quote": "Ordered the full leg for Eid. It arrived perfectly portioned. The whole family was impressed.",
        "author": "Salma & Family",
        "locality": "Mosque Road",
        "avatar": "S",
    },
]

STATS = [
    {"value": "12+", "label": "Years in business"},
    {"value": "2 hrs", "label": "Farm-to-door time"},
    {"value": "50 k+", "label": "Happy customers"},
    {"value": "100%", "label": "Halal certified"},
]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "menu": MENU,
            "process": PROCESS,
            "testimonials": TESTIMONIALS,
            "stats": STATS,
        },
    )
