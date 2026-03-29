# 📚 Portrait Ordering Website — Step-by-Step Guide
### For Brintha S | Flask + HTML + CSS Project

---

## 🗂️ PROJECT STRUCTURE (What you will create)

```
portrait_ordering/
│
├── app.py                  ← Main Flask file (all routes)
├── requirements.txt        ← Libraries needed
├── orders.json             ← Auto-created when orders come in
│
├── templates/              ← All HTML pages
│   ├── base.html           ← Common navbar + footer
│   ├── home.html           ← Home page
│   ├── gallery.html        ← Sketch gallery
│   ├── pricing.html        ← Pricing table
│   ├── order.html          ← Order form with photo upload
│   ├── success.html        ← Order confirmation page
│   ├── admin_login.html    ← Admin login
│   └── admin_dashboard.html← Admin orders view
│
└── static/
    └── uploads/            ← Customer photos saved here
```

---

## ✅ STEP 1 — Install Python & VS Code

1. Download Python from https://python.org → Click "Download Python 3.x"
2. During install → ✅ Check "Add Python to PATH"
3. Download VS Code from https://code.visualstudio.com
4. Install VS Code → open it → install "Python" extension

---

## ✅ STEP 2 — Create Your Project Folder

1. Open your Desktop or Documents
2. Create a new folder: **portrait_ordering**
3. Inside it, create these folders:
   - `templates`
   - `static`
   - Inside `static`, create: `uploads`

---

## ✅ STEP 3 — Install Flask

1. Open VS Code
2. Go to Terminal → New Terminal
3. Type this command and press Enter:

```bash
pip install flask werkzeug
```

Wait for it to finish. You'll see "Successfully installed flask..."

---

## ✅ STEP 4 — Create All Files

Copy each file into your project folder:

| File | Location |
|------|----------|
| app.py | portrait_ordering/ |
| requirements.txt | portrait_ordering/ |
| base.html | portrait_ordering/templates/ |
| home.html | portrait_ordering/templates/ |
| gallery.html | portrait_ordering/templates/ |
| pricing.html | portrait_ordering/templates/ |
| order.html | portrait_ordering/templates/ |
| success.html | portrait_ordering/templates/ |
| admin_login.html | portrait_ordering/templates/ |
| admin_dashboard.html | portrait_ordering/templates/ |

---

## ✅ STEP 5 — Run the Website

1. Open VS Code Terminal
2. Navigate to your project folder:

```bash
cd Desktop/portrait_ordering
```

3. Run the app:

```bash
python app.py
```

4. You will see:
```
* Running on http://127.0.0.1:5000
```

5. Open your browser → go to: **http://127.0.0.1:5000**

🎉 Your website is running!

---

## ✅ STEP 6 — Test All Pages

| Page | URL |
|------|-----|
| Home | http://127.0.0.1:5000/ |
| Gallery | http://127.0.0.1:5000/gallery |
| Pricing | http://127.0.0.1:5000/pricing |
| Order Form | http://127.0.0.1:5000/order |
| Admin Login | http://127.0.0.1:5000/admin |

---

## ✅ STEP 7 — Test the Order Form

1. Go to http://127.0.0.1:5000/order
2. Fill in:
   - Name: Test Customer
   - Phone: 9999999999
   - Email: test@email.com
   - Portrait Type: Solo Portrait
   - Art Style: Pencil Sketch
   - Frame Size: A4
   - Upload any photo from your computer
3. Click "Place My Order"
4. You will see the success page with your Order ID ✅

---

## ✅ STEP 8 — Test Admin Dashboard

1. Go to http://127.0.0.1:5000/admin
2. Login with:
   - Username: **admin**
   - Password: **admin123**
3. You will see all placed orders
4. You can change order status → click Save

---

## 🔧 HOW EACH FILE WORKS

### app.py
- The brain of your website
- Each `@app.route("/page")` controls what shows on that URL
- `load_orders()` reads orders from orders.json
- `save_orders()` writes new orders to orders.json

### base.html
- The common template all pages share
- Has the navbar at top and footer at bottom
- Other pages "extend" this using `{% extends "base.html" %}`

### order.html
- The order form with `enctype="multipart/form-data"` (needed for file upload)
- `<input type="file">` allows photo upload
- JavaScript shows the selected file name

### admin_dashboard.html
- Shows all orders in a table
- Admin can update status: Pending → In Progress → Completed
- Stats bar shows total, pending, in progress, completed counts

---

## 🚨 COMMON ERRORS & FIXES

| Error | Fix |
|-------|-----|
| `ModuleNotFoundError: flask` | Run `pip install flask` again |
| `TemplateNotFound` | Check that your HTML file is inside the `templates/` folder |
| Page not found (404) | Make sure you're on the right URL |
| Photo not uploading | Check that `static/uploads/` folder exists |
| Port already in use | Change port: `app.run(port=5001)` |

---

## 💡 TIPS FOR YOUR RESUME

When explaining this project in interviews, say:

✅ "I built a full-stack portrait ordering website using **Python Flask** for the backend, **HTML and CSS** for the frontend."

✅ "Features include **photo upload**, order management, pricing page, and an **admin dashboard** with status tracking."

✅ "Orders are stored in **JSON**, and the admin can update order status in real time."

---

## 🚀 NEXT STEPS (To make it even better)

- [ ] Add a real database (SQLite) instead of JSON
- [ ] Add WhatsApp notification when order is placed
- [ ] Deploy on Render.com or Railway.app (free hosting)
- [ ] Add payment gateway (Razorpay)

---

*Made with ❤️ for Brintha S — B.Sc IT, NGM College, Pollachi*
