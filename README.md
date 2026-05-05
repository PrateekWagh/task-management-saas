📌 Project Title
# Task Management SaaS (Backend API)
A backend-based Task Management System built to handle user tasks efficiently through RESTful APIs.

The system allows users to create, update, delete, and track tasks with proper backend logic, authentication support, and secure data handling.



✨ Features

- User registration and authentication system
- Secure password hashing using pwdlib
- Create, update, delete tasks
- Task status management (Pending / Completed)
- RESTful API architecture
- Secure environment variable handling
- Modular backend structure
- Database integration


🛠️ Tech Stack
- Backend: FastAPI
- ORM: SQLAlchemy
- Authentication: pwdlib (password hashing)
- Database: PostgreSQL
- API Testing: Swagger UI / Postman
- Version Control: Git & GitHub

🔐 Authentication System
- Passwords are securely hashed using pwdlib before storing in database
- User authentication ensures protected routes
- Only authenticated users can access task management features

🚀 How to Run Locally
1. Clone the repository
-git clone https://github.com/PrateekWagh/task-management-saas.git

2. Navigate to project folder : cd task-management-saas

3. Create virtual environment : python -m venv venv

4. Activate environment
   
   Windows: venv\Scripts\activate
   
   Mac/Linux: source venv/bin/activate

6. Install dependencies
pip install -r requirements.txt

7. Run FastAPI server
uvicorn main:app --reload

📖 API Documentation

Once the server is running, open:

Swagger UI:
http://127.0.0.1:8000/docs


📈 Future Improvements
- Add frontend dashboard (React)
- Role-based access control (Admin/User)
- Deploy on cloud (Render / AWS)
- Add refresh token system
- Add logging & monitoring system

👨‍💻 Author

Prateek Wagh  
Aspiring Software Engineer | Backend & Cybersecurity Enthusiast

⭐ Support

If you found this project useful, please consider giving it a star ⭐
