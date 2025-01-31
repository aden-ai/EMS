# Employee Management System (EMS) API

## 📌 Project Overview

The **Employee Management System (EMS) API** is a FastAPI-based backend service that manages employee records and leave requests. It provides CRUD operations for employees and leave requests while ensuring structured data storage with SQLAlchemy and PostgreSQL.

## 🚀 Deployment

- **Hosted API:** [https://emsapi.onrender.com](https://emsapi.onrender.com)
- **Live API Docs:** [https://emsapi.onrender.com/docs](https://emsapi.onrender.com/docs)

## 🚀 Features

- **Employee Management:** Add, update, retrieve, and delete employee records.
- **Leave Management:** Employees can apply for leave, and admins can approve/reject requests.
- **Role-Based Access Control (RBAC):** Admins have higher privileges to manage employees and leave requests.
- **Database Integration:** Uses PostgreSQL with SQLAlchemy ORM.
- **Authentication & Security:** Secure endpoints using JWT-based authentication (Planned feature).
- **RESTful API:** Well-structured API with OpenAPI documentation.

## 🏗️ Tech Stack

- **Backend:** FastAPI, SQLAlchemy
- **Database:** PostgreSQL
- **Authentication:** OAuth2 + JWT (Planned)
- **Deployment:** Render
- **Documentation:** Auto-generated Swagger UI



## 🌐 API Endpoints

| Method   | Endpoint                | Description                   |
| -------- | ----------------------- | ----------------------------- |
| `POST`   | `/employees/`           | Create a new employee         |
| `GET`    | `/employees/`           | Get all employees             |
| `GET`    | `/employees/{id}`       | Get employee by ID            |
| `PUT`    | `/employees/{id}`       | Update employee details       |
| `DELETE` | `/employees/{id}`       | Delete an employee            |
| `POST`   | `/leaves/`              | Apply for leave               |
| `GET`    | `/leaves/{employee_id}` | Get employee's leave requests |
| `PUT`    | `/leaves/{leave_id}`    | Update leave request          |
| `DELETE` | `/leaves/{leave_id}`    | Delete leave request          |

<br>

## 📜 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/aden-ai/EMS.git
cd EMS
```

### 3️⃣ Set Up Environment Variables

Create a `.env` file with:

```
DATABASE_URL=postgresql://username:password@localhost/dbname
```

### 4️⃣ Run the Application

```bash
uvicorn main:app --reload
```

### 5️⃣ Access API Documentation

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🤝 Contributing

Want to contribute? Feel free to fork this repo, create a new branch, and submit a pull request!

## 📜 License

This project is licensed under the MIT License.



