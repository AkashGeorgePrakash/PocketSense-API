# PocketSense API - Expense Tracker for College Students

PocketSense helps college students track and split their daily expenses with friends. It simplifies managing shared costs for everything from dining hall meals to textbooks, local travel, and weekend outings.

## 📌 Features
- **User Authentication** - Secure login and registration.
- **Expense Groups** - Create groups to manage shared expenses.
- **Transaction Tracking** - Keep records of expenses and balances.
- **Settlement System** - Calculate who owes whom and settle debts.

## 🛠 Tech Stack
- **Backend:** Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT Tokens
- **Deployment:** Heroku/AWS

## 🚀 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/PocketSense-API.git
   ```

2. Navigate to the project folder:
   ```bash
   cd PocketSense-API
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🗄 Database Setup & Migrations
1. Apply migrations:
   ```bash
   python manage.py migrate
   ```
2. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
3. Run the development server:
   ```bash
   python manage.py runserver
   ```

## 🔗 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/register/` | Register a new user |
| `POST` | `/login/` | User login |
| `GET`  | `/expenses/` | List all expenses |
| `POST` | `/expenses/add/` | Add a new expense |
| `POST` | `/settle/` | Settle balances between users |

## 🚀 Future Enhancements
- ✅ Mobile app integration
- ✅ Real-time notifications
- ✅ AI-based spending insights

## 📬 Contact & Contributions
Contributions are welcome!
If you have any questions, feel free to reach out:

📧 **Email:** akashgeorgeprakash@gmail.com  
🔗 **GitHub:** [AkashGeorgePrakash](https://github.com/AkashGeorgePrakash)
