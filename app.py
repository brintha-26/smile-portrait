from flask import Flask, render_template, request, redirect, url_for, session, flash
import os, json, uuid
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "portrait_secret_key_2025"

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
ORDERS_FILE = "orders.json"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# ── Helpers ──────────────────────────────────────────────
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def load_orders():
    if not os.path.exists(ORDERS_FILE):
        return []
    with open(ORDERS_FILE) as f:
        return json.load(f)

def save_orders(orders):
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=2)

# ── Gallery of already-sketched portraits ────────────────
GALLERY = [
    {"id": 1, "title": "Couple Portrait",     "img": "g1.jpg", "desc": "Romantic pencil sketch for couples"},
    {"id": 2, "title": "male solo Sketch",    "img": "g2.jpg", "desc": "Soft charcoal sketch for newborns"},
    {"id": 3, "title": "Family Portrait",     "img": "g3.jpg", "desc": "Full family pencil art"},
    {"id": 4, "title": "Solo Portrait",       "img": "g4.jpg", "desc": "Individual detailed sketch"},
    {"id": 5, "title": "Pet Portrait",        "img": "g5.jpg", "desc": "Charcoal sketch of your pet"},
    {"id": 6, "title": "Wedding Sketch",      "img": "g6.jpg", "desc": "Special wedding memory art"},
]

FRAME_SIZES = [
    {"size": "A4  (8×11 in)",  "price": 499},
    {"size": "A3  (12×16 in)", "price": 799},
    {"size": "A2  (16×20 in)", "price": 1099},
    {"size": "A1  (20×24 in)", "price": 1499},
]

PRICING = [
    {"type": "Solo Portrait",   "pencil": 499,  "charcoal": 699,  "color": 999},
    {"type": "Couple Portrait", "pencil": 799,  "charcoal": 999,  "color": 1299},
    {"type": "Family Portrait", "pencil": 1099, "charcoal": 1299, "color": 1699},
    {"type": "male solo Sketch", "pencil": 599,  "charcoal": 799,  "color": 1099},
    {"type": "Pet Portrait",    "pencil": 599,  "charcoal": 799,  "color": 1099},
]

# ── Routes ────────────────────────────────────────────────
@app.route("/")
def home():
    return render_template("home.html", gallery=GALLERY[:3])

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", gallery=GALLERY)

@app.route("/pricing")
def pricing():
    return render_template("pricing.html", pricing=PRICING, frames=FRAME_SIZES)

@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "POST":
        name        = request.form.get("name", "").strip()
        email       = request.form.get("email", "").strip()
        phone       = request.form.get("phone", "").strip()
        portrait_type = request.form.get("portrait_type", "")
        art_style   = request.form.get("art_style", "")
        frame_size  = request.form.get("frame_size", "")
        message     = request.form.get("message", "").strip()

        if not all([name, email, phone, portrait_type, art_style, frame_size]):
            flash("Please fill all required fields.", "error")
            return redirect(url_for("order"))

        photo_filename = None
        if "photo" in request.files:
            file = request.files["photo"]
            if file and file.filename and allowed_file(file.filename):
                ext = file.filename.rsplit(".", 1)[1].lower()
                photo_filename = f"{uuid.uuid4().hex}.{ext}"
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], photo_filename))

        order_id = f"PO-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:5].upper()}"
        new_order = {
            "order_id": order_id,
            "name": name, "email": email, "phone": phone,
            "portrait_type": portrait_type, "art_style": art_style,
            "frame_size": frame_size, "message": message,
            "photo": photo_filename,
            "status": "Pending",
            "date": datetime.now().strftime("%d %b %Y, %I:%M %p"),
        }
        orders = load_orders()
        orders.append(new_order)
        save_orders(orders)

        session["last_order_id"] = order_id
        flash(f"Order placed! Your Order ID is {order_id}", "success")
        return redirect(url_for("success"))

    return render_template("order.html",
                           portrait_types=[p["type"] for p in PRICING],
                           frames=FRAME_SIZES)

@app.route("/success")
def success():
    order_id = session.get("last_order_id", "N/A")
    return render_template("success.html", order_id=order_id)

# ── Admin ─────────────────────────────────────────────────
@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    if session.get("admin"):
        return redirect(url_for("admin_dashboard"))
    if request.method == "POST":
        if (request.form.get("username") == ADMIN_USERNAME and
                request.form.get("password") == ADMIN_PASSWORD):
            session["admin"] = True
            return redirect(url_for("admin_dashboard"))
        flash("Invalid credentials.", "error")
    return render_template("admin_login.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    orders = load_orders()
    return render_template("admin_dashboard.html", orders=orders)

@app.route("/admin/update/<order_id>", methods=["POST"])
def update_status(order_id):
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    new_status = request.form.get("status")
    orders = load_orders()
    for o in orders:
        if o["order_id"] == order_id:
            o["status"] = new_status
            break
    save_orders(orders)
    flash("Status updated!", "success")
    return redirect(url_for("admin_dashboard"))

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
