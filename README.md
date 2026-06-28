# 🍔 Fast Food Ordering Web Application

> A responsive full-stack food ordering platform with cart management and order tracking — built with Django, MySQL, and JavaScript.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?style=flat&logo=django)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=flat&logo=mysql)
![HTML5](https://img.shields.io/badge/HTML5-CSS3-red?style=flat&logo=html5)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=flat&logo=javascript)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat)

---

## 🔗 Live Demo

🌐 **Live Website:**  
https://tomerarvind195-byte.github.io/Webside-for-a-restaurantbase-WebApplication/

> **Note:** This GitHub Pages deployment showcases the frontend only. To access the complete Django application with backend functionality, deploy the project on Render, Railway, or PythonAnywhere.

---

## 📸 Screenshots

| Menu Page | Cart Page | Order Summary |
|-----------|------------|---------------|
| <img src="https://github.com/user-attachments/assets/ee41bb8e-5b7e-4bc7-8eb7-592f7cd3cae6" width="300"> | <img src="https://github.com/user-attachments/assets/32e2edde-75a7-457a-bb32-32daf5c2078b" width="300"> | <img src="https://github.com/user-attachments/assets/de292957-1928-494c-b1a5-257e0e3af51f" width="300"> |

| Confirm Order | About Page | Contact Us |
|---------------|------------|------------|
| <img src="https://github.com/user-attachments/assets/f01c3593-e3de-457e-8ec3-69ad018e6009" width="300"> | <img src="https://github.com/user-attachments/assets/c6645720-24b0-4872-8e55-45d4d17c1035" width="300"> | <img src="https://github.com/user-attachments/assets/2f359af0-f332-462f-a3fc-337345dbf851" width="300"> |

---

## 📋 About The Project

A **mobile-first full-stack food ordering web application** that lets users browse a categorized menu, add items to cart, and place orders — all through a smooth, responsive interface. Built to simulate a real-world food ordering system like Zomato or Swiggy at a smaller scale.

**Key Highlights:**
- 5+ food categories with dynamic menu management
- Complete add-to-cart and order management workflow
- Real-time order tracking via Django backend
- Mobile-first responsive design across all devices
- Django admin panel for easy menu and order management

---

## ✨ Features

- ✅ Browse menu by category (Burgers, Pizza, Drinks, Snacks, etc.)
- ✅ Add to cart with quantity control
- ✅ Order placement and order summary page
- ✅ Real-time inventory and order management via Django admin
- ✅ Fully responsive — mobile, tablet, desktop
- ✅ Fast page loads with optimized static asset management

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.x, Django 4.x |
| Frontend | HTML5, CSS3, JavaScript (ES6) |
| Database | MySQL |
| Version Control | Git & GitHub |
| Deployment | _(Add: Railway / PythonAnywhere)_ |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- MySQL
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/tomerarvind195-byte/food-ordering-app.git
cd food-ordering-app

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup MySQL database
# Create a database named 'food_ordering' in MySQL
# Update DB credentials in settings.py

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Load sample menu data (optional)
python manage.py loaddata menu_data.json

# 7. Create superuser (for admin panel)
python manage.py createsuperuser

# 8. Start the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 📁 Project Structure

```
food-ordering-app/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── food_ordering/           # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── menu/                    # Menu & cart app
│   ├── models.py            # MenuItem, Category, Order models
│   ├── views.py             # Menu, cart, order logic
│   ├── urls.py              # URL routing
│   └── admin.py             # Admin panel config
│
├── templates/               # HTML templates
│   ├── menu.html
│   ├── cart.html
│   └── order_summary.html
│
└── static/                  # CSS, JS, Images
    ├── css/
    ├── js/
    └── images/
```

---

## 🗄️ Database Models

```python
# Key models used in this project

class Category(models.Model):
    name = models.CharField(max_length=100)   # e.g. Burgers, Pizza

class MenuItem(models.Model):
    name        = models.CharField(max_length=200)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    price       = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image       = models.ImageField(upload_to='menu_images/')

class Order(models.Model):
    items      = models.ManyToManyField(MenuItem)
    total      = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status     = models.CharField(max_length=50, default='Pending')
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Arvind Kumar**

- 🌐 [LinkedIn](https://www.linkedin.com/in/arvind-kumar-399a60338)
- 💻 [GitHub](https://github.com/tomerarvind195-byte)
- 📧 tomerarvind195@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> ⭐ Agar yeh project helpful laga toh **star** zaroor karo!
