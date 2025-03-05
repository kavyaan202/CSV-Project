# CSV Processing with Django, Celery, and Redis

## 📌 Project Overview
This Django-based project allows users to **upload CSV files**, process them asynchronously using **Celery & Redis**, and display real-time **sum, average, and count calculations**. Additionally, users can filter results dynamically using a **search feature**.

---

## 🚀 Features
✅ Upload CSV files via a web interface  
✅ Process CSV data asynchronously with Celery  
✅ Perform calculations (Sum, Average, Count) dynamically  
✅ Implement a search feature to filter data by product name  
✅ Display processed results dynamically on the frontend  
✅ Handle errors for invalid or missing data  

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/kavyaan202/CSV-Project.git
cd CSV-Project
```

### **2️⃣ Create a Virtual Environment & Activate It**
```sh
python -m venv env
```
#### **On Windows**:
```sh
env\Scripts\activate
```
#### **On macOS/Linux**:
```sh
source env/bin/activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Setup Django Project**
```sh
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Start Redis Server** (Required for Celery)
#### **On Windows (via WSL or Redis for Windows)**
```sh
redis-server
```
#### **On macOS/Linux**:
```sh
sudo systemctl start redis
```

### **6️⃣ Start Celery Worker**
```sh
celery -A csv_project worker --loglevel=info
```

### **7️⃣ Run Django Server**
```sh
python manage.py runserver
```

---

## 📂 Project Structure
```
csv_project/
│── csv_project/             # Django Project Directory
│   │── __init__.py
│   │── settings.py
│   │── urls.py
│   │── celery.py            # Celery Configuration
│
│── csv_app/                 # Django App Directory
│   │── models.py            # Database Models
│   │── views.py             # Views & Business Logic
│   │── tasks.py             # Celery Tasks
│   │── templates/           # HTML Templates
│   │── static/              # Static Files (CSS, JS)
│
│── media/                   # Uploaded Files
│── migrations/              # Django Migrations
│── env/                     # Virtual Environment (Not for GitHub)
│── manage.py                # Django Management Script
│── requirements.txt         # Dependencies List
│── README.md                # Project Documentation
```

---

## 🎯 How It Works
1️⃣ **Upload a CSV file** via the web interface.  
2️⃣ **Celery processes the file asynchronously** and calculates sum, average, and count for numeric columns.  
3️⃣ **Search functionality** dynamically filters data by product name.  
4️⃣ The processed results are **displayed dynamically** without page refresh.  

---

## 💡 Troubleshooting
### **1. 'django-admin' is not recognized**
- Ensure you're inside the virtual environment:
  ```sh
  env\Scripts\activate   # Windows
  source env/bin/activate  # macOS/Linux
  ```

### **2. Celery Not Recognized**
- Run Celery using Python:
  ```sh
  python -m celery -A csv_project worker --loglevel=info
  ```

### **3. Redis Connection Issues**
- Ensure Redis is running:
  ```sh
  redis-cli ping  # Should return 'PONG'
  ```

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your proposed changes.

---

## 📧 Contact
For queries, email at **kavyanagaraj1111@gmail.com** or create an issue on GitHub.

🚀 Happy Coding!

