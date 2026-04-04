## Insert Statements

### Pharmacy
```sql
INSERT INTO Pharmacy VALUES (1, 'HealthPlus Pharmacy', '123 Main St', 'Dearborn', 'MI', '3135551000');
INSERT INTO Pharmacy VALUES (2, 'CareWell Pharmacy', '456 Oak Ave', 'Detroit', 'MI', '3135552000');
INSERT INTO Pharmacy VALUES (3, 'MediTrust Pharmacy', '789 Pine Rd', 'Ann Arbor', 'MI', '3135553000');
INSERT INTO Pharmacy VALUES (4, 'QuickScript Pharmacy', '321 Washtenaw Ave', 'Ypsilanti', 'MI', '3135554000');
INSERT INTO Pharmacy VALUES (5, 'GreenLeaf Pharmacy', '555 Michigan Ave', 'Lansing', 'MI', '5175555000');
```

### DrugManufacturer
```sql
INSERT INTO DrugManufacturer VALUES (1, 'Pfizer', '100 Pharma St', 'New York', 'NY');
INSERT INTO DrugManufacturer VALUES (2, 'Moderna', '200 Bio Ave', 'Cambridge', 'MA');
INSERT INTO DrugManufacturer VALUES (3, 'Johnson & Johnson', '300 Health Blvd', 'New Brunswick', 'NJ');
INSERT INTO DrugManufacturer VALUES (4, 'AbbVie', '1 North Waukegan Rd', 'North Chicago', 'IL');
INSERT INTO DrugManufacturer VALUES (5, 'Merck', '2000 Galloping Hill Rd', 'Kenilworth', 'NJ');
INSERT INTO DrugManufacturer VALUES (6, 'Novartis', '700 Pharma Pkwy', 'East Hanover', 'NJ');
INSERT INTO DrugManufacturer VALUES (7, 'AstraZeneca', '1800 Concord Pike', 'Wilmington', 'DE');
INSERT INTO DrugManufacturer VALUES (8, 'Eli Lilly', '893 Delaware St', 'Indianapolis', 'IN');
```

### Employee
```sql
INSERT INTO Employee VALUES (1, 1, 'Alice Smith', '12 Elm St', 'Dearborn', 'MI', '1985-04-12', 'Pharmacist', 'Morning');
INSERT INTO Employee VALUES (2, 1, 'Bob Johnson', '34 Maple St', 'Dearborn', 'MI', '1990-07-19', 'Technician', 'Evening');
INSERT INTO Employee VALUES (3, 2, 'Carol White', '56 Oak St', 'Detroit', 'MI', '1982-11-03', 'Pharmacist', 'Morning');
INSERT INTO Employee VALUES (4, 2, 'David Brown', '78 Pine St', 'Detroit', 'MI', '1995-02-25', 'Technician', 'Night');
INSERT INTO Employee VALUES (5, 3, 'Emma Davis', '90 Cedar St', 'Ann Arbor', 'MI', '1988-09-14', 'Pharmacist', 'Evening');
INSERT INTO Employee VALUES (6, 3, 'Grace Hopper', '123 Huron St', 'Ann Arbor', 'MI', '1994-03-20', 'Technician', 'Morning');
INSERT INTO Employee VALUES (7, 4, 'Frank Miller', '45 Cross St', 'Ypsilanti', 'MI', '1980-06-30', 'Pharmacist', 'Morning');
INSERT INTO Employee VALUES (8, 4, 'Hannah Scott', '67 Grove Ave', 'Ypsilanti', 'MI', '1997-01-15', 'Technician', 'Evening');
INSERT INTO Employee VALUES (9, 5, 'Ian Cooper', '88 Capitol Blvd', 'Lansing', 'MI', '1983-12-08', 'Pharmacist', 'Morning');
INSERT INTO Employee VALUES (10, 5, 'Julia Torres', '99 River Rd', 'Lansing', 'MI', '1991-08-22', 'Technician', 'Night');
INSERT INTO Employee VALUES (11, 1, 'Kevin Nguyen', '15 Birch Ln', 'Dearborn', 'MI', '1993-05-17', 'Technician', 'Morning');
INSERT INTO Employee VALUES (12, 2, 'Laura Martinez', '28 Spruce Dr', 'Detroit', 'MI', '1987-10-04', 'Pharmacist', 'Evening');
INSERT INTO Employee VALUES (13, 3, 'Nathan Reed', '41 Willow Ct', 'Ann Arbor', 'MI', '1996-03-28', 'Technician', 'Night');
INSERT INTO Employee VALUES (14, 4, 'Olivia Chang', '53 Depot St', 'Ypsilanti', 'MI', '1989-07-11', 'Technician', 'Morning');
INSERT INTO Employee VALUES (15, 5, 'Paul Washington', '72 Saginaw St', 'Lansing', 'MI', '1984-11-20', 'Technician', 'Evening');
```

### Pharmacist
```sql
INSERT INTO Pharmacist VALUES (1, 'PharmD');
INSERT INTO Pharmacist VALUES (3, 'PharmD');
INSERT INTO Pharmacist VALUES (5, 'PharmD');
INSERT INTO Pharmacist VALUES (7, 'PharmD');
INSERT INTO Pharmacist VALUES (9, 'PharmD');
INSERT INTO Pharmacist VALUES (12, 'RPh');
```

### PharmacyTechnician
```sql
INSERT INTO PharmacyTechnician VALUES (2, 'Certified Technician');
INSERT INTO PharmacyTechnician VALUES (4, 'Registered Technician');
INSERT INTO PharmacyTechnician VALUES (6, 'Certified Technician');
INSERT INTO PharmacyTechnician VALUES (8, 'Certified Technician');
INSERT INTO PharmacyTechnician VALUES (10, 'Registered Technician');
INSERT INTO PharmacyTechnician VALUES (11, 'Certified Technician');
INSERT INTO PharmacyTechnician VALUES (13, 'Registered Technician');
INSERT INTO PharmacyTechnician VALUES (14, 'Certified Technician');
INSERT INTO PharmacyTechnician VALUES (15, 'Registered Technician');
```

### Patient
```sql
INSERT INTO Patient VALUES (1, 'John Doe', 'M', 'BlueCross', '11 First St', 'Dearborn', 'MI', 1);
INSERT INTO Patient VALUES (2, 'Jane Roe', 'F', 'Aetna', '22 Second St', 'Detroit', 'MI', 3);
INSERT INTO Patient VALUES (3, 'Mike Lee', 'M', 'Cigna', '33 Third St', 'Ann Arbor', 'MI', 5);
INSERT INTO Patient VALUES (4, 'Sara Kim', 'F', 'UnitedHealth', '44 Fourth St', 'Dearborn', 'MI', 1);
INSERT INTO Patient VALUES (5, 'Tom Clark', 'M', 'Humana', '55 Fifth St', 'Detroit', 'MI', 3);
INSERT INTO Patient VALUES (6, 'Amy Chen', 'F', 'BlueCross', '66 Sixth St', 'Ann Arbor', 'MI', 5);
INSERT INTO Patient VALUES (7, 'Brian Hall', 'M', 'Aetna', '77 Seventh St', 'Ypsilanti', 'MI', 7);
INSERT INTO Patient VALUES (8, 'Diana Ross', 'F', 'Cigna', '88 Eighth St', 'Lansing', 'MI', 9);
INSERT INTO Patient VALUES (9, 'Eric Wong', 'M', 'UnitedHealth', '99 Ninth St', 'Dearborn', 'MI', 1);
INSERT INTO Patient VALUES (10, 'Fiona Grant', 'F', 'Humana', '110 Tenth St', 'Detroit', 'MI', 12);
INSERT INTO Patient VALUES (11, 'George Bell', 'M', 'BlueCross', '121 Lake Dr', 'Ann Arbor', 'MI', 5);
INSERT INTO Patient VALUES (12, 'Helen Park', 'F', 'Aetna', '132 Hill Ave', 'Ypsilanti', 'MI', 7);
INSERT INTO Patient VALUES (13, 'Ivan Cruz', 'M', 'Cigna', '143 Valley Rd', 'Lansing', 'MI', 9);
INSERT INTO Patient VALUES (14, 'Jenny Liu', 'F', 'UnitedHealth', '154 Brook Ln', 'Dearborn', 'MI', 1);
INSERT INTO Patient VALUES (15, 'Kyle Adams', 'M', 'Humana', '165 Ridge St', 'Detroit', 'MI', 3);
INSERT INTO Patient VALUES (16, 'Lana Morris', 'F', 'BlueCross', '176 Elm Ct', 'Ann Arbor', 'MI', 5);
INSERT INTO Patient VALUES (17, 'Marcus Young', 'M', 'Aetna', '187 Park Ave', 'Ypsilanti', 'MI', 7);
INSERT INTO Patient VALUES (18, 'Nina Patel', 'F', 'Cigna', '198 Center St', 'Lansing', 'MI', 9);
INSERT INTO Patient VALUES (19, 'Oscar Diaz', 'M', 'UnitedHealth', '209 Front St', 'Dearborn', 'MI', 12);
INSERT INTO Patient VALUES (20, 'Paula West', 'F', 'Humana', '220 Back St', 'Detroit', 'MI', 3);
```

### PatientPhone
```sql
INSERT INTO PatientPhone VALUES (1, '3131111111');
INSERT INTO PatientPhone VALUES (1, '3131112222');
INSERT INTO PatientPhone VALUES (2, '3132223333');
INSERT INTO PatientPhone VALUES (3, '3133334444');
INSERT INTO PatientPhone VALUES (4, '3134445555');
INSERT INTO PatientPhone VALUES (5, '3135556666');
INSERT INTO PatientPhone VALUES (5, '3135557777');
INSERT INTO PatientPhone VALUES (6, '7341110001');
INSERT INTO PatientPhone VALUES (7, '7341110002');
INSERT INTO PatientPhone VALUES (7, '7341110003');
INSERT INTO PatientPhone VALUES (8, '5171110001');
INSERT INTO PatientPhone VALUES (9, '3131110009');
INSERT INTO PatientPhone VALUES (10, '3131110010');
INSERT INTO PatientPhone VALUES (10, '3131110011');
INSERT INTO PatientPhone VALUES (11, '7341110004');
INSERT INTO PatientPhone VALUES (12, '7341110005');
INSERT INTO PatientPhone VALUES (13, '5171110002');
INSERT INTO PatientPhone VALUES (14, '3131110014');
INSERT INTO PatientPhone VALUES (14, '3131110015');
INSERT INTO PatientPhone VALUES (15, '3131110016');
INSERT INTO PatientPhone VALUES (16, '7341110006');
INSERT INTO PatientPhone VALUES (17, '7341110007');
INSERT INTO PatientPhone VALUES (18, '5171110003');
INSERT INTO PatientPhone VALUES (18, '5171110004');
INSERT INTO PatientPhone VALUES (19, '3131110019');
INSERT INTO PatientPhone VALUES (20, '3131110020');
```

### Drug
```sql
INSERT INTO Drug VALUES (1, 'Aspirin', 1, 100);
INSERT INTO Drug VALUES (2, 'Ibuprofen', 2, 200);
INSERT INTO Drug VALUES (3, 'Amoxicillin', 3, 150);
INSERT INTO Drug VALUES (4, 'Metformin', 1, 120);
INSERT INTO Drug VALUES (5, 'Lisinopril', 2, 180);
INSERT INTO Drug VALUES (6, 'Atorvastatin', 1, 250);
INSERT INTO Drug VALUES (7, 'Amlodipine', 1, 90);
INSERT INTO Drug VALUES (8, 'Omeprazole', 7, 160);
INSERT INTO Drug VALUES (9, 'Losartan', 5, 140);
INSERT INTO Drug VALUES (10, 'Albuterol', 7, 75);
INSERT INTO Drug VALUES (11, 'Gabapentin', 1, 110);
INSERT INTO Drug VALUES (12, 'Hydrochlorothiazide', 5, 200);
INSERT INTO Drug VALUES (13, 'Sertraline', 1, 130);
INSERT INTO Drug VALUES (14, 'Simvastatin', 5, 170);
INSERT INTO Drug VALUES (15, 'Montelukast', 5, 85);
INSERT INTO Drug VALUES (16, 'Escitalopram', 8, 95);
INSERT INTO Drug VALUES (17, 'Rosuvastatin', 7, 60);
INSERT INTO Drug VALUES (18, 'Levothyroxine', 4, 300);
INSERT INTO Drug VALUES (19, 'Pantoprazole', 6, 140);
INSERT INTO Drug VALUES (20, 'Furosemide', 6, 190);
INSERT INTO Drug VALUES (21, 'Prednisone', 1, 220);
INSERT INTO Drug VALUES (22, 'Tramadol', 3, 80);
INSERT INTO Drug VALUES (23, 'Tamsulosin', 4, 70);
INSERT INTO Drug VALUES (24, 'Clopidogrel', 8, 110);
INSERT INTO Drug VALUES (25, 'Carvedilol', 6, 130);
INSERT INTO Drug VALUES (26, 'Trazodone', 3, 150);
INSERT INTO Drug VALUES (27, 'Metoprolol', 7, 240);
INSERT INTO Drug VALUES (28, 'Duloxetine', 8, 100);
INSERT INTO Drug VALUES (29, 'Meloxicam', 4, 160);
INSERT INTO Drug VALUES (30, 'Fluticasone', 6, 55);
```

### Doctor
```sql
INSERT INTO Doctor VALUES (1, 'Dr. Robert Chen', 'Cardiology', '3139991001', '200 Medical Dr', 'Dearborn', 'MI');
INSERT INTO Doctor VALUES (2, 'Dr. Lisa Patel', 'Family Medicine', '3139991002', '210 Health Ave', 'Detroit', 'MI');
INSERT INTO Doctor VALUES (3, 'Dr. James Wilson', 'Internal Medicine', '3139991003', '220 Clinic Rd', 'Ann Arbor', 'MI');
INSERT INTO Doctor VALUES (4, 'Dr. Maria Garcia', 'Endocrinology', '3139991004', '230 Wellness Blvd', 'Dearborn', 'MI');
INSERT INTO Doctor VALUES (5, 'Dr. Kevin Park', 'Orthopedics', '3139991005', '240 Care Ln', 'Detroit', 'MI');
INSERT INTO Doctor VALUES (6, 'Dr. Sarah Kim', 'Pulmonology', '5179991006', '250 Breath Way', 'Lansing', 'MI');
INSERT INTO Doctor VALUES (7, 'Dr. Thomas Reed', 'Psychiatry', '7349991007', '260 Mind St', 'Ypsilanti', 'MI');
INSERT INTO Doctor VALUES (8, 'Dr. Angela Foster', 'Gastroenterology', '3139991008', '270 Digest Ave', 'Detroit', 'MI');
```

### PharmacySells
```sql
INSERT INTO PharmacySells VALUES (1, 1, 5.99);
INSERT INTO PharmacySells VALUES (1, 2, 7.49);
INSERT INTO PharmacySells VALUES (1, 4, 11.99);
INSERT INTO PharmacySells VALUES (1, 6, 14.99);
INSERT INTO PharmacySells VALUES (1, 7, 8.99);
INSERT INTO PharmacySells VALUES (1, 11, 22.49);
INSERT INTO PharmacySells VALUES (1, 13, 18.99);
INSERT INTO PharmacySells VALUES (1, 18, 9.49);
INSERT INTO PharmacySells VALUES (1, 21, 6.99);
INSERT INTO PharmacySells VALUES (1, 27, 12.49);
INSERT INTO PharmacySells VALUES (2, 3, 12.99);
INSERT INTO PharmacySells VALUES (2, 4, 9.99);
INSERT INTO PharmacySells VALUES (2, 8, 15.99);
INSERT INTO PharmacySells VALUES (2, 9, 13.49);
INSERT INTO PharmacySells VALUES (2, 12, 7.99);
INSERT INTO PharmacySells VALUES (2, 14, 16.99);
INSERT INTO PharmacySells VALUES (2, 19, 19.99);
INSERT INTO PharmacySells VALUES (2, 22, 24.99);
INSERT INTO PharmacySells VALUES (2, 25, 17.49);
INSERT INTO PharmacySells VALUES (2, 28, 28.99);
INSERT INTO PharmacySells VALUES (3, 1, 6.49);
INSERT INTO PharmacySells VALUES (3, 5, 8.49);
INSERT INTO PharmacySells VALUES (3, 10, 21.99);
INSERT INTO PharmacySells VALUES (3, 15, 19.49);
INSERT INTO PharmacySells VALUES (3, 16, 23.99);
INSERT INTO PharmacySells VALUES (3, 17, 31.49);
INSERT INTO PharmacySells VALUES (3, 20, 10.99);
INSERT INTO PharmacySells VALUES (3, 26, 14.49);
INSERT INTO PharmacySells VALUES (3, 29, 11.99);
INSERT INTO PharmacySells VALUES (3, 30, 27.99);
INSERT INTO PharmacySells VALUES (4, 1, 5.49);
INSERT INTO PharmacySells VALUES (4, 2, 6.99);
INSERT INTO PharmacySells VALUES (4, 5, 9.49);
INSERT INTO PharmacySells VALUES (4, 8, 14.99);
INSERT INTO PharmacySells VALUES (4, 10, 20.99);
INSERT INTO PharmacySells VALUES (4, 18, 8.99);
INSERT INTO PharmacySells VALUES (4, 23, 26.49);
INSERT INTO PharmacySells VALUES (4, 24, 19.99);
INSERT INTO PharmacySells VALUES (4, 27, 11.49);
INSERT INTO PharmacySells VALUES (4, 30, 29.99);
INSERT INTO PharmacySells VALUES (5, 3, 11.49);
INSERT INTO PharmacySells VALUES (5, 6, 13.99);
INSERT INTO PharmacySells VALUES (5, 9, 12.49);
INSERT INTO PharmacySells VALUES (5, 11, 21.99);
INSERT INTO PharmacySells VALUES (5, 14, 15.99);
INSERT INTO PharmacySells VALUES (5, 16, 22.49);
INSERT INTO PharmacySells VALUES (5, 20, 9.99);
INSERT INTO PharmacySells VALUES (5, 22, 23.49);
INSERT INTO PharmacySells VALUES (5, 25, 16.49);
INSERT INTO PharmacySells VALUES (5, 29, 12.99);
```

### Prescription
```sql
-- Pharmacy 1 (pharmacists 1, 12) sells drugs: 1,2,4,6,7,11,13,18,21,27
INSERT INTO Prescription VALUES (1, 1, 1, 1, 1, '2026-01-10', 30);
INSERT INTO Prescription VALUES (2, 2, 1, 4, 4, '2026-01-12', 90);
INSERT INTO Prescription VALUES (3, 1, 1, 9, 6, '2026-01-14', 30);
INSERT INTO Prescription VALUES (4, 4, 1, 14, 18, '2026-01-16', 60);
INSERT INTO Prescription VALUES (5, 2, 1, 1, 2, '2026-01-18', 20);
INSERT INTO Prescription VALUES (6, 1, 1, 19, 7, '2026-01-20', 30);
INSERT INTO Prescription VALUES (7, 3, 1, 4, 11, '2026-01-22', 90);
INSERT INTO Prescription VALUES (8, 4, 1, 9, 13, '2026-01-24', 30);
INSERT INTO Prescription VALUES (9, 2, 12, 14, 21, '2026-02-01', 10);
INSERT INTO Prescription VALUES (10, 1, 12, 19, 27, '2026-02-03', 30);
-- Pharmacy 2 (pharmacists 3) sells drugs: 3,4,8,9,12,14,19,22,25,28
INSERT INTO Prescription VALUES (11, 2, 3, 2, 3, '2026-01-12', 20);
INSERT INTO Prescription VALUES (12, 3, 3, 5, 8, '2026-01-15', 30);
INSERT INTO Prescription VALUES (13, 8, 3, 10, 9, '2026-01-19', 60);
INSERT INTO Prescription VALUES (14, 2, 3, 15, 12, '2026-01-23', 30);
INSERT INTO Prescription VALUES (15, 5, 3, 20, 22, '2026-01-27', 15);
INSERT INTO Prescription VALUES (16, 3, 3, 2, 14, '2026-02-02', 90);
INSERT INTO Prescription VALUES (17, 8, 3, 10, 25, '2026-02-06', 30);
INSERT INTO Prescription VALUES (18, 2, 3, 15, 28, '2026-02-10', 60);
INSERT INTO Prescription VALUES (19, 1, 3, 5, 19, '2026-02-14', 30);
INSERT INTO Prescription VALUES (20, 4, 3, 20, 4, '2026-02-18', 90);
-- Pharmacy 3 (pharmacists 5) sells drugs: 1,5,10,15,16,17,20,26,29,30
INSERT INTO Prescription VALUES (21, 3, 5, 3, 5, '2026-01-15', 60);
INSERT INTO Prescription VALUES (22, 6, 5, 6, 10, '2026-01-20', 30);
INSERT INTO Prescription VALUES (23, 7, 5, 11, 16, '2026-01-25', 90);
INSERT INTO Prescription VALUES (24, 3, 5, 16, 26, '2026-02-01', 30);
INSERT INTO Prescription VALUES (25, 6, 5, 3, 15, '2026-02-05', 60);
INSERT INTO Prescription VALUES (26, 7, 5, 6, 17, '2026-02-09', 30);
INSERT INTO Prescription VALUES (27, 3, 5, 11, 29, '2026-02-13', 15);
INSERT INTO Prescription VALUES (28, 5, 5, 16, 30, '2026-02-17', 30);
INSERT INTO Prescription VALUES (29, 6, 5, 8, 20, '2026-02-21', 60);
INSERT INTO Prescription VALUES (30, 3, 5, 13, 1, '2026-02-25', 30);
-- Pharmacy 4 (pharmacists 7) sells drugs: 1,2,5,8,10,18,23,24,27,30
INSERT INTO Prescription VALUES (31, 5, 7, 7, 1, '2026-01-11', 30);
INSERT INTO Prescription VALUES (32, 7, 7, 12, 5, '2026-01-17', 90);
INSERT INTO Prescription VALUES (33, 4, 7, 17, 23, '2026-01-23', 60);
INSERT INTO Prescription VALUES (34, 5, 7, 7, 24, '2026-01-29', 30);
INSERT INTO Prescription VALUES (35, 8, 7, 12, 27, '2026-02-04', 30);
INSERT INTO Prescription VALUES (36, 7, 7, 17, 8, '2026-02-10', 90);
-- Pharmacy 5 (pharmacists 9) sells drugs: 3,6,9,11,14,16,20,22,25,29
INSERT INTO Prescription VALUES (37, 6, 9, 8, 6, '2026-01-13', 60);
INSERT INTO Prescription VALUES (38, 7, 9, 13, 11, '2026-01-19', 30);
INSERT INTO Prescription VALUES (39, 6, 9, 18, 22, '2026-01-25', 90);
INSERT INTO Prescription VALUES (40, 8, 9, 8, 25, '2026-02-01', 30);
```

### PharmacyContract
```sql
INSERT INTO PharmacyContract VALUES (1, 1, '2025-01-01', '2026-01-01');
INSERT INTO PharmacyContract VALUES (1, 2, '2025-02-01', '2026-02-01');
INSERT INTO PharmacyContract VALUES (1, 4, '2025-03-01', '2026-03-01');
INSERT INTO PharmacyContract VALUES (2, 1, '2025-05-01', '2026-05-01');
INSERT INTO PharmacyContract VALUES (2, 3, '2025-03-01', '2026-03-01');
INSERT INTO PharmacyContract VALUES (2, 5, '2025-06-01', '2026-06-01');
INSERT INTO PharmacyContract VALUES (2, 7, '2025-04-01', '2026-04-01');
INSERT INTO PharmacyContract VALUES (3, 2, '2025-01-15', '2026-01-15');
INSERT INTO PharmacyContract VALUES (3, 5, '2025-04-01', '2026-04-01');
INSERT INTO PharmacyContract VALUES (3, 6, '2025-07-01', '2026-07-01');
INSERT INTO PharmacyContract VALUES (3, 8, '2025-02-01', '2026-02-01');
INSERT INTO PharmacyContract VALUES (4, 1, '2025-06-01', '2026-06-01');
INSERT INTO PharmacyContract VALUES (4, 4, '2025-08-01', '2026-08-01');
INSERT INTO PharmacyContract VALUES (4, 7, '2025-03-15', '2026-03-15');
INSERT INTO PharmacyContract VALUES (4, 8, '2025-05-01', '2026-05-01');
INSERT INTO PharmacyContract VALUES (5, 1, '2025-02-01', '2026-02-01');
INSERT INTO PharmacyContract VALUES (5, 3, '2025-04-15', '2026-04-15');
INSERT INTO PharmacyContract VALUES (5, 5, '2025-06-01', '2026-06-01');
INSERT INTO PharmacyContract VALUES (5, 6, '2025-09-01', '2026-09-01');
```
