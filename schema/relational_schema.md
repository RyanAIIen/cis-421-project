# Pharmacy Database - Relational Schema

## Entities

### Pharmacy

Retail pharmacy location that employs staff, sells drugs, and contracts with
manufacturers.

#### Logical Schema

Pharmacy(<u>pharmacy_id</u>, name, address, phone)

#### DDL

```sql
CREATE TABLE Pharmacy(
    pharmacy_id: INTEGER PRIMARY KEY,
    name: VARCHAR(100) NOT NULL,
    address: VARCHAR(200),
    phone: VARCHAR(15)
)
```

### Employee

Staff member working at a pharmacy. Specializes into `Pharmacist` or
`PharmacyTechnician`.

#### Logical Schema

Employee(<u>employee_id</u>, pharmacy_id, name, street, city, state, birthday,
employee_type, shift_time)

#### DDL

```sql
CREATE TABLE Employee(
    employee_id: INTEGER PRIMARY KEY,
    pharmacy_id: INTEGER NOT NULL,
    name: VARCHAR(100) NOT NULL,
    street: VARCHAR(100),
    city: VARCHAR(50),
    state: VARCHAR(2),
    birthday: DATE,
    employee_type: VARCHAR(20) NOT NULL CHECK (employee_type IN ('Pharmacist', 'Technician')),
    shift_time: VARCHAR(50),
    FOREIGN KEY (pharmacy_id) REFERENCES Pharmacy(pharmacy_id)
)
```

### Pharmacist

Licensed healthcare professional with pharmacy degree who can verify and
dispense prescriptions.

#### Logical Schema

Pharmacist(<u>employee_id</u>, degree)

#### DDL

```sql
CREATE TABLE Pharmacist(
    employee_id: INTEGER PRIMARY KEY,
    degree: VARCHAR(100),
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id) ON DELETE CASCADE
)
```

### PharmacyTechnician

Certified support staff who assists pharmacists with routine tasks like
inventory and preparation.

#### Logical Schema

PharmacyTechnician(<u>employee_id</u>, certification)

#### DDL

```sql
CREATE TABLE PharmacyTechnician(
    employee_id: INTEGER PRIMARY KEY,
    certification: VARCHAR(100),
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id) ON DELETE CASCADE
)
```

### Patient

Customer who receives prescriptions and pharmaceutical services from the
pharmacy.

#### Logical Schema

Patient(<u>patient_id</u>, name, sex, insurance, street, city, state,
primary_pharmacist_id)

#### DDL

```sql
CREATE TABLE Patient(
    patient_id: INTEGER PRIMARY KEY,
    name: VARCHAR(100) NOT NULL,
    sex: CHAR(1) CHECK (sex IN ('M', 'F', 'O')),
    insurance: VARCHAR(100),
    street: VARCHAR(100),
    city: VARCHAR(50),
    state: VARCHAR(2),
    primary_pharmacist_id: INTEGER,
    FOREIGN KEY (primary_pharmacist_id) REFERENCES Pharmacist(employee_id)
)
```

### PatientPhone

Phone numbers for patients (multi-valued attribute - a patient can have multiple
phone numbers).

#### Logical Schema

PatientPhone(<u>patient_id, phone_number</u>)

#### DDL

```sql
CREATE TABLE PatientPhone(
    patient_id: INTEGER,
    phone_number: VARCHAR(15),
    PRIMARY KEY (patient_id, phone_number),
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id) ON DELETE CASCADE
)
```

### Drug

Pharmaceutical product sold by the pharmacy and produced by a manufacturer.

#### Logical Schema

Drug(<u>drug_id</u>, trade_name, manufacturer_id)

#### DDL

```sql
CREATE TABLE Drug(
    drug_id: INTEGER PRIMARY KEY,
    trade_name: VARCHAR(100) NOT NULL,
    manufacturer_id: INTEGER NOT NULL,
    quantity: INTEGER NOT NULL,
    FOREIGN KEY (manufacturer_id) REFERENCES DrugManufacturer(manufacturer_id)
)
```

### DrugManufacturer

Company that produces pharmaceutical drugs and contracts with pharmacies for
distribution.

#### Logical Schema

DrugManufacturer(<u>manufacturer_id</u>, name, street, city, state)

#### DDL

```sql
CREATE TABLE DrugManufacturer(
    manufacturer_id: INTEGER PRIMARY KEY,
    name: VARCHAR(100) NOT NULL,
    street: VARCHAR(100),
    city: VARCHAR(50),
    state: VARCHAR(2)
)
```

## Relationships

### Works (Employee works at Pharmacy)

```sql
-- M:1 relationship captured by `pharmacy_id` foreign key in `Employee` table
-- Attribute: shift_time included as attribute in `Employee` table
```

### Has (Pharmacist has Patients) - 1:M

```sql
-- 1:M relationship: one pharmacist has many patients
-- Captured by `primary_pharmacist_id` foreign key in `Patient` table
```

### Sells (Pharmacy sells Drugs) - M:M

#### Logical Schema

PharmacySells(<u>pharmacy_id, drug_id</u>, price)

#### DDL

```sql
CREATE TABLE PharmacySells(
    pharmacy_id: INTEGER,
    drug_id: INTEGER,
    price: DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (pharmacy_id, drug_id),
    FOREIGN KEY (pharmacy_id) REFERENCES Pharmacy(pharmacy_id),
    FOREIGN KEY (drug_id) REFERENCES Drug(drug_id)
)
```

### Prescribes (Pharmacist prescribes Drug to Patient) - Ternary M:M:M

#### Logical Schema

Prescription(<u>prescription_id</u>, pharmacist_id, patient_id, drug_id,
prescription_date, quantity)

#### DDL

```sql
CREATE TABLE Prescription(
    prescription_id: INTEGER PRIMARY KEY,
    pharmacist_id: INTEGER NOT NULL,
    patient_id: INTEGER NOT NULL,
    drug_id: INTEGER NOT NULL,
    prescription_date: DATE NOT NULL,
    quantity: INTEGER NOT NULL,
    FOREIGN KEY (pharmacist_id) REFERENCES Pharmacist(employee_id),
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (drug_id) REFERENCES Drug(drug_id)
)
```

### Manufactures (DrugManufacturer manufactures Drug) - 1:M

```sql
-- Already captured by manufacturer_id foreign key in Drug table
```

### Contracts (Pharmacy contracts with DrugManufacturer) - M:M

#### Logical Schema

PharmacyContract(<u>pharmacy_id, manufacturer_id</u>, contract_date,
contract_end_date)

#### DDL

```sql
CREATE TABLE PharmacyContract(
    pharmacy_id: INTEGER,
    manufacturer_id: INTEGER,
    contract_date: DATE,
    contract_end_date: DATE,
    PRIMARY KEY (pharmacy_id, manufacturer_id),
    FOREIGN KEY (pharmacy_id) REFERENCES Pharmacy(pharmacy_id),
    FOREIGN KEY (manufacturer_id) REFERENCES DrugManufacturer(manufacturer_id)
)
```

## Notes and Design Decisions

1. **Employee Specialization**: Used a discriminator column (`employee_type`) in
   the `Employee` table with separate tables for `Pharmacist` and
   `PharmacyTechnician` to store their specific attributes (`degree` and
   `certification`).

2. **Composite Attributes**: Address attributes (`street`, `city`, `state`) are
   flattened into the tables rather than creating separate address tables.

3. **Derived Attribute**: `age` can be calculated from `birthday` at query time,
   so it's not stored.

4. **Ternary Relationship**: The `Prescribes` relationship connects
   `Pharmacist`, `Patient`, and `Drug`. Created a `Prescription` table with a
   surrogate key for easier referencing.

5. **Primary Keys**: Used `INTEGER` for all primary keys for simplicity. In a
   real system, you might use auto-incrementing integers or UUIDs.

6. **Additional Considerations**:
   - May want to add timestamps (`created_at`, `updated_at`) to tables
   - Consider adding indexes on foreign keys and frequently queried columns
   - May need additional validation constraints (e.g., `quantity` > 0,
     `price` >= 0)
