## Insert Statements

### Pharmacy
```sql
INSERT INTO Pharmacy VALUES (1, 'HealthPlus Pharmacy', '123 Main St', '3135551000');
INSERT INTO Pharmacy VALUES (2, 'CareWell Pharmacy', '456 Oak Ave', '3135552000');
INSERT INTO Pharmacy VALUES (3, 'MediTrust Pharmacy', '789 Pine Rd', '3135553000');
```

### DrugManufacturer
```sql
INSERT INTO DrugManufacturer VALUES (1, 'Pfizer', '100 Pharma St', 'New York', 'NY');
INSERT INTO DrugManufacturer VALUES (2, 'Moderna', '200 Bio Ave', 'Cambridge', 'MA');
INSERT INTO DrugManufacturer VALUES (3, 'Johnson & Johnson', '300 Health Blvd', 'New Brunswick', 'NJ');
```

### Employee
```sql
INSERT INTO Employee VALUES (1, 1, 'Alice Smith', '12 Elm St', 'Dearborn', 'MI', '1985-04-12', 'Pharmacist', 'Morning');
INSERT INTO Employee VALUES (2, 1, 'Bob Johnson', '34 Maple St', 'Dearborn', 'MI', '1990-07-19', 'Technician', 'Evening');
INSERT INTO Employee VALUES (3, 2, 'Carol White', '56 Oak St', 'Detroit', 'MI', '1982-11-03', 'Pharmacist', 'Morning');
INSERT INTO Employee VALUES (4, 2, 'David Brown', '78 Pine St', 'Detroit', 'MI', '1995-02-25', 'Technician', 'Night');
INSERT INTO Employee VALUES (5, 3, 'Emma Davis', '90 Cedar St', 'Ann Arbor', 'MI', '1988-09-14', 'Pharmacist', 'Evening');
```

### Pharmacist
```sql
INSERT INTO Pharmacist VALUES (1, 'PharmD');
INSERT INTO Pharmacist VALUES (3, 'PharmD');
INSERT INTO Pharmacist VALUES (5, 'PharmD');
```

### PharmacyTechnician
```sql
INSERT INTO PharmacyTechnician VALUES (2, 'Certified Technician');
INSERT INTO PharmacyTechnician VALUES (4, 'Registered Technician');
```

### Patient
```sql
INSERT INTO Patient VALUES (1, 'John Doe', 'M', 'BlueCross', '11 First St', 'Dearborn', 'MI', 1);
INSERT INTO Patient VALUES (2, 'Jane Roe', 'F', 'Aetna', '22 Second St', 'Detroit', 'MI', 3);
INSERT INTO Patient VALUES (3, 'Mike Lee', 'M', 'Cigna', '33 Third St', 'Ann Arbor', 'MI', 5);
INSERT INTO Patient VALUES (4, 'Sara Kim', 'F', 'UnitedHealth', '44 Fourth St', 'Dearborn', 'MI', 1);
INSERT INTO Patient VALUES (5, 'Tom Clark', 'M', 'Humana', '55 Fifth St', 'Detroit', 'MI', 3);
```

### PatientPhone
```sql
INSERT INTO PatientPhone VALUES (1, '3131111111');
INSERT INTO PatientPhone VALUES (1, '3131112222');
INSERT INTO PatientPhone VALUES (2, '3132223333');
INSERT INTO PatientPhone VALUES (3, '3133334444');
INSERT INTO PatientPhone VALUES (4, '3134445555');
INSERT INTO PatientPhone VALUES (5, '3135556666');
```

### Drug
```sql
INSERT INTO Drug VALUES (1, 'Aspirin', 1, 100);
INSERT INTO Drug VALUES (2, 'Ibuprofen', 2, 200);
INSERT INTO Drug VALUES (3, 'Amoxicillin', 3, 150);
INSERT INTO Drug VALUES (4, 'Metformin', 1, 120);
INSERT INTO Drug VALUES (5, 'Lisinopril', 2, 180);
```

### PharmacySells
```sql
INSERT INTO PharmacySells VALUES (1, 1, 5.99);
INSERT INTO PharmacySells VALUES (1, 2, 7.49);
INSERT INTO PharmacySells VALUES (2, 3, 12.99);
INSERT INTO PharmacySells VALUES (2, 4, 9.99);
INSERT INTO PharmacySells VALUES (3, 5, 8.49);
INSERT INTO PharmacySells VALUES (3, 1, 6.49);
```

### Prescription
```sql
INSERT INTO Prescription VALUES (1, 1, 1, 1, '2026-01-10', 30);
INSERT INTO Prescription VALUES (2, 3, 2, 3, '2026-01-12', 20);
INSERT INTO Prescription VALUES (3, 5, 3, 5, '2026-01-15', 60);
INSERT INTO Prescription VALUES (4, 1, 4, 2, '2026-01-18', 15);
INSERT INTO Prescription VALUES (5, 3, 5, 4, '2026-01-20', 45);
```

### PharmacyContract
```sql
INSERT INTO PharmacyContract VALUES (1, 1, '2025-01-01', '2026-01-01');
INSERT INTO PharmacyContract VALUES (1, 2, '2025-02-01', '2026-02-01');
INSERT INTO PharmacyContract VALUES (2, 2, '2025-03-01', '2026-03-01');
INSERT INTO PharmacyContract VALUES (3, 3, '2025-04-01', '2026-04-01');
INSERT INTO PharmacyContract VALUES (2, 1, '2025-05-01', '2026-05-01');
```
