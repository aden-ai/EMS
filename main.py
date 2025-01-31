from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import SessionLocal, Employee, LeaveRequest, DepartmentEnum, RoleEnum
from pydantic import BaseModel
from typing import List, Optional
import datetime

# FastAPI app setup
app = FastAPI()

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models for input validation
class EmployeeBase(BaseModel):
    name: str
    email: str
    department: DepartmentEnum
    role: RoleEnum
    salary: float

class LeaveRequestBase(BaseModel):
    employee_id: int
    start_date: datetime.datetime
    end_date: datetime.datetime
    reason: str

@app.get("/")
def read_root():
    return {"msg": "Welcome to the Employee Management System"}

# CRUD for Employee
@app.post("/employees/", response_model=EmployeeBase)
def create_employee(employee: EmployeeBase, db: Session = Depends(get_db)):
    db_employee = Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        role=employee.role,
        salary=employee.salary
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.get("/employees/", response_model=List[EmployeeBase])
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@app.get("/employees/{employee_id}", response_model=EmployeeBase)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.put("/employees/{employee_id}", response_model=EmployeeBase)
def update_employee(employee_id: int, employee: EmployeeBase, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db_employee.name = employee.name
    db_employee.email = employee.email
    db_employee.department = employee.department
    db_employee.role = employee.role
    db_employee.salary = employee.salary
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.delete("/employees/{employee_id}", status_code=204)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(db_employee)
    db.commit()
    return {"msg": "Employee deleted successfully"}

# CRUD for LeaveRequest
@app.post("/leaves/", response_model=LeaveRequestBase)
def create_leave_request(leave_request: LeaveRequestBase, db: Session = Depends(get_db)):
    db_leave_request = LeaveRequest(
        employee_id=leave_request.employee_id,
        start_date=leave_request.start_date,
        end_date=leave_request.end_date,
        reason=leave_request.reason
    )
    db.add(db_leave_request)
    db.commit()
    db.refresh(db_leave_request)
    return db_leave_request

@app.get("/leaves/{employee_id}", response_model=List[LeaveRequestBase])
def get_leave_requests(employee_id: int, db: Session = Depends(get_db)):
    return db.query(LeaveRequest).filter(LeaveRequest.employee_id == employee_id).all()

@app.put("/leaves/{leave_id}", response_model=LeaveRequestBase)
def update_leave_request(leave_id: int, leave_request: LeaveRequestBase, db: Session = Depends(get_db)):
    db_leave_request = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()
    if db_leave_request is None:
        raise HTTPException(status_code=404, detail="Leave Request not found")
    db_leave_request.start_date = leave_request.start_date
    db_leave_request.end_date = leave_request.end_date
    db_leave_request.reason = leave_request.reason
    db.commit()
    db.refresh(db_leave_request)
    return db_leave_request

@app.delete("/leaves/{leave_id}", status_code=204)
def delete_leave_request(leave_id: int, db: Session = Depends(get_db)):
    db_leave_request = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()
    if db_leave_request is None:
        raise HTTPException(status_code=404, detail="Leave Request not found")
    db.delete(db_leave_request)
    db.commit()
    return {"msg": "Leave Request deleted successfully"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000)