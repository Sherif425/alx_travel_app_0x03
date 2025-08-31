ALX alx_travel_app_0x00
Here's a professional `README.md` file for the project `alx_travel_app_0x01`, covering the context of your current task: API development using Django REST Framework and Swagger.

---

### ✅ `alx_travel_app_0x01/README.md`

```markdown
# alx_travel_app_0x01

A Django REST Framework project that provides an API for managing travel listings and bookings. This version focuses on building API endpoints for the `Listing` and `Booking` models and documenting them using Swagger.

## 🚀 Features

- Full CRUD API for Listings and Bookings
- RESTful API routing via DRF ViewSets and Routers
- Swagger UI documentation at `/swagger/`
- Environment configuration using `.env` files
- Modular app structure following Django best practices

---

## 📁 Project Structure

```

alx\_travel\_app/
├── alx\_travel\_app/
│   ├── **init**.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── listings/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── management/commands/seed.py
├── manage.py
└── .env

````

---

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/alx_travel_app_0x01.git
   cd alx_travel_app_0x01
````

2. **Create a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file:

   ```env
   DEBUG=True
   SECRET_KEY=your_generated_secret_key_here
   DATABASE_NAME=alx_travel
   DATABASE_USER=root
   DATABASE_PASSWORD=password
   DATABASE_HOST=127.0.0.1
   DATABASE_PORT=3306
   ```

5. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Seed the database**

   ```bash
   python manage.py seed
   ```

7. **Run the server**

   ```bash
   python manage.py runserver
   ```

---

## 🔌 API Endpoints

Base URL: `http://localhost:8000/api/`

| Endpoint             | Method | Description          |
| -------------------- | ------ | -------------------- |
| `/api/listings/`     | GET    | List all listings    |
| `/api/listings/`     | POST   | Create a new listing |
| `/api/listings/:id/` | PUT    | Update a listing     |
| `/api/listings/:id/` | DELETE | Delete a listing     |
| `/api/bookings/`     | GET    | List all bookings    |
| `/api/bookings/`     | POST   | Create a new booking |
| `/api/bookings/:id/` | PUT    | Update a booking     |
| `/api/bookings/:id/` | DELETE | Delete a booking     |

---

## 📄 Swagger Documentation

Once the server is running, access Swagger docs at:

```
http://localhost:8000/swagger/
```

---

## ✅ Requirements

* Python 3.8+
* Django 4.x
* Django REST Framework
* drf-yasg (for Swagger)

---

## 🧪 Testing

Use Postman or curl to test endpoints. Example:

```bash
curl http://localhost:8000/api/listings/
```

---

## 📌 Notes

* Ensure the MySQL database is running and accessible.
* The project uses `.env` for secret management. Never commit secrets to version control.

---

## 📚 License

This project is for educational purposes under the ALX SE program.

```

---

Let me know if you want it saved to a file now or customized with your GitHub username or database details.
```
