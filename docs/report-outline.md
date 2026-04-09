# Report Outline

---

## 1. Application Background

**Author: Ryan**

- Describe the enterprise: a regional chain of retail pharmacies operating
  across Michigan
- Explain the real-world context: pharmacies employ licensed pharmacists and
  technicians, contract with drug manufacturers, and serve patients whose
  doctors write prescriptions
- Motivate why a relational database is well-suited: multiple entities with
  complex relationships, high data volume, need for integrity constraints
- Keep to 1-2 paragraphs

---

## 2. Database Requirements

**Author: Ryan**

Describe informally what the database needs to capture:

- **Pharmacies** — name, address, phone; each employs staff and sells drugs
- **Employees** — name, address, birthday, shift; specialize into pharmacists or
  technicians (IS-A hierarchy)
- **Pharmacists** — pharmacy degree, license number; assigned patients; dispense
  prescriptions
- **Pharmacy Technicians** — certification; support pharmacists
- **Doctors** — name, specialty, phone, address; write prescriptions
- **Patients** — name, sex, insurance, birthday, address; multiple phone numbers
  (multi-valued); assigned a primary pharmacist
- **Drugs** — trade name, manufacturer, stock quantity, controlled substance
  flag
- **Drug Manufacturers** — name, address; manufacture drugs and contract with
  pharmacies
- **Prescriptions** — link doctor, pharmacist, patient, and drug; record date
  and quantity
- **Contracts** — between pharmacies and manufacturers; include start and end
  dates
- **Pricing** — each pharmacy sets its own price per drug

Highlight notable modeling decisions:

- Employee IS-A hierarchy (disjoint: pharmacist or technician, not both)
- Patient phone as a multi-valued attribute
- Age as a derived attribute (computed from birthday)
- Prescription captures both the prescribing doctor and the dispensing
  pharmacist — these are distinct roles

---

## 3. ER Diagram

**Author: Gavin**

- Include the full ER diagram (Lucidchart export)
- Caption or annotate key design decisions:
  - IS-A hierarchy with disjoint discriminator
  - Multi-valued attribute (Patient phone — double oval)
  - Derived attribute (Employee/Patient age — dashed oval)
  - Prescription relationship connecting Doctor, Pharmacist, Patient, Drug

---

## 4. Relational Schema

**Author: Ryan**

List the full logical schema with primary keys underlined and foreign keys
noted. Reference `schema/relational_schema.md` for the complete DDL.

- Pharmacy(<u>pharmacy_id</u>, name, street, city, state, phone)
- Employee(<u>employee_id</u>, pharmacy_id, name, street, city, state, birthday,
  employee_type, shift_time)
- Pharmacist(<u>employee_id</u>, degree, license_number)
- PharmacyTechnician(<u>employee_id</u>, certification)
- Doctor(<u>doctor_id</u>, name, specialty, phone, street, city, state)
- Patient(<u>patient_id</u>, name, sex, insurance, birthday, street, city,
  state, primary_pharmacist_id)
- PatientPhone(<u>patient_id, phone_number</u>)
- Drug(<u>drug_id</u>, trade_name, manufacturer_id, quantity,
  controlled_substance)
- DrugManufacturer(<u>manufacturer_id</u>, name, street, city, state)
- PharmacySells(<u>pharmacy_id, drug_id</u>, price)
- Prescription(<u>prescription_id</u>, doctor_id, pharmacist_id, patient_id,
  drug_id, prescription_date, quantity)
- PharmacyContract(<u>pharmacy_id, manufacturer_id</u>, contract_date,
  contract_end_date)

Include a brief note on each design decision (IS-A implementation, multi-valued
attribute, derived attribute, Prescription semantics).

---

## 5. Sample Database Instance

**Author: Ryan**

Show the scale of the data loaded into `PharmacyDB.db`:

| Table              | Rows |
| ------------------ | ---- |
| Pharmacy           | 5    |
| Employee           | 15   |
| Pharmacist         | 6    |
| PharmacyTechnician | 9    |
| Doctor             | 8    |
| Patient            | 20   |
| PatientPhone       | 26   |
| Drug               | 30   |
| DrugManufacturer   | 8    |
| PharmacySells      | 50   |
| Prescription       | 40   |
| PharmacyContract   | 19   |

Include a representative sample of rows from 3-4 key tables (e.g., Patient,
Prescription, Drug) to illustrate the data. Full insert statements are in
`schema/SQL Statements.md`.

---

## 6. SQL Statements and Query Results

**Authors: Gavin (queries 1–9), Ryan (queries 10–14)**

For each query, include:

1. A brief description of what it does and why it's useful
2. The SQL
3. The result

Reference `queries/queries.md` for SQL and `queries/query-outputs.md` for
results. Summarize all 14 queries in order. For the two UPDATE queries (12 and
13), show the state of affected rows before and after.

---

## 7. Team Responsibilities

**Author: Ryan**

| Member     | Responsibilities                                                                                                                   |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Ryan Allen | Doctor entity design, sample data expansion, queries 10–14, Django admin UI, report sections 1–2/4–7                               |
| Gavin Tank | ER diagram, relational schema, DDL, SQL inserts, database setup, queries 1–9, query outputs, report section 3, presentation slides |
