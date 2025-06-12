
```markdown
# 🏕️ Nomadic - Travel & Booking App (Django REST API)

Welcome to **Nomadic**, a Django-based REST API for managing travel destinations and user bookings. This project is designed to help users discover beautiful travel locations and make bookings seamlessly.

---

## 🚀 Features

- JWT Authentication (Login, Token Refresh)
- Password Reset via Email
- Register & Login using Email
- Add/View Travel Locations
- Book Trips for Selected Locations
- View Past Bookings

---

## 🏗 Project Structure

```

Nomadic/
├── accounts/       # Custom user model & authentication
├── locations/      # App for managing travel destinations
├── bookings/       # App for user bookings
├── Nomadic/        # Main project settings and URLs
├── manage.py
└── README.md

````

---

## ⚙️ Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/your-username/nomadic.git
cd nomadic
````

2. **Create virtual environment**

```bash
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Run the server**

```bash
python manage.py runserver
```

---

## 🔐 Authentication

This project uses **JWT (JSON Web Token)** authentication.

* `POST /api/login/` — Get access and refresh tokens
* `POST /api/refresh/` — Get a new access token using refresh token
* `POST /api/register/` — Register new users
* `POST /send-reset-password-link/` — Send password reset link
* `POST /reset-password/` — Reset user password

---

## 🌍 Locations API

* `GET /api/locations/` — View all travel locations
* `POST /api/locations/` — Add a new location (admin only)
* `GET /api/locations/<id>/` — View single location details

---

## 🧳 Bookings API

* `GET /api/bookings/` — View user bookings
* `POST /api/bookings/` — Book a trip to a location
* `DELETE /api/bookings/<id>/` — Cancel a booking

---

## 📧 Email Backend (For Password Reset)

Using Django’s **console email backend**:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

You will see password reset links printed in the console.

---

## 📌 Environment Variables (Optional)

Create a `.env` file for secret settings:

```
SECRET_KEY=your_secret_key
DEBUG=True
EMAIL_HOST_USER=shahbazkhan@gmail.com
```

---

## 📄 License

This project is open-source and free to use for learning and development.

---

## ✨ Author

Developed by **Shahbaz Khan**
Feel free to modify and build upon this project for your own travel app ideas!

---

