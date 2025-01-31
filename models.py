import os
from datetime import datetime
from sqlalchemy import create_engine, Column, String, DateTime, Integer, ForeignKey, Enum, Float
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import enum
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is missing")

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Enums for Departments and Roles
class DepartmentEnum(str, enum.Enum):
    IT = "IT"
    HR = "HR"
    FINANCE = "Finance"
    SALES = "Sales"
    MARKETING = "Marketing"

class RoleEnum(str, enum.Enum):
    ADMIN = "Admin"
    EMPLOYEE = "Employee"

# Employee Model
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    department = Column(Enum(DepartmentEnum), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    salary = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    leaves = relationship("LeaveRequest", back_populates="employee")

# Leave Request Model
class LeaveRequest(Base):
    __tablename__ = "leave_requests"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    reason = Column(String, nullable=False)
    status = Column(String, default="Pending", nullable=False)  # Pending, Approved, Rejected
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    employee = relationship("Employee", back_populates="leaves")

# Create tables
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Error while creating tables: {e}")
