# Presentation Outline

10 minutes total. Suggested split: ~1 min per slide.

**Slide assignments:**

- **Ryan**: Slides 6, 9, 10, 11, 12
- **Gavin**: Slides 1, 2, 3, 4, 5, 7, 8, 13

---

## Slide 1 - Title _(Gavin)_

**Content:**

- "Pharmacy Database System"
- CIS-421
- Ryan Allen, Gavin Tank
- Date

**Notes:**

- Brief intro: who you are and what the project is

---

## Slide 2 - Application Background _(Gavin)_

**Content:**

- A regional group of retail pharmacies operating across Michigan
- Key actors: pharmacies, employees, doctors, patients, drugs, and drug
  manufacturers
- Core operations: prescription fulfillment, inventory management, staffing, and
  manufacturer contracts

**Notes:**

- Set the scene quickly. This slide shouldn't take more than 45 seconds.
- Emphasize that this is a realistic enterprise with real relationships between
  entities, not a toy example
- Mention that each pharmacy manages its own inventory, pricing, and
  manufacturer contracts

---

## Slide 3 - Database Requirements _(Gavin)_

**Content:**

- Track each pharmacy's location, staff, inventory, and pricing
- Track employees using an IS-A hierarchy: pharmacist or pharmacy technician
- Track doctors who write prescriptions and patients who receive them
- Track patient phone numbers as a multi-valued attribute
- Track drugs, drug manufacturers, and pharmacy-manufacturer contracts
- Track prescriptions linking doctor, patient, pharmacist, and drug

**Notes:**

- Call out the interesting modeling challenges: IS-A hierarchy, multi-valued
  attribute, derived age from birthday
- Clarify that pharmacists and pharmacy technicians are modeled as subtypes of
  Employee
- This slide motivates why the ER diagram looks the way it does

---

## Slide 4 - ER Diagram _(Gavin)_

**Content:**

- Full ER diagram (Lucidchart export)
- Visual callouts: `Employee -> Pharmacist / PharmacyTechnician`,
  `PatientPhone`, `Prescription`

**Notes:**

- Walk through the diagram entity by entity. Don't just show it silently.
- Key points to call out:
  - IS-A hierarchy: Employee → Pharmacist / PharmacyTechnician (disjoint)
  - Prescription connects Doctor, Pharmacist, Patient, and Drug
  - Patient phone is a multi-valued attribute (double oval)
  - Age is a derived attribute (dashed oval), computed from birthday at query
    time
- Don't get lost in the details. Hit the highlights and move on.

---

## Slide 5 - Relational Schema _(Gavin)_

**Content:**

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

**Notes:**

- Explain how the IS-A hierarchy was implemented: discriminator column
  (`employee_type`) in Employee plus separate Pharmacist and PharmacyTechnician
  tables for subtype attributes
- Briefly explain how PatientPhone handles the multi-valued attribute
- Mention Prescription has both `doctor_id` and `pharmacist_id`: doctors
  prescribe, pharmacists dispense
- Keep the verbal walkthrough selective; the goal is to show structure, not read
  every attribute aloud

---

## Slide 6 - Sample Database _(Ryan)_

**Content:**

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
| Prescription       | 40   |
| PharmacySells      | 50   |
| PharmacyContract   | 19   |

**Notes:**

- Data is Michigan-based: Dearborn, Detroit, Ann Arbor, Ypsilanti, Lansing
- Drug names are real FDA-approved drugs (Metformin, Lisinopril, Atorvastatin,
  etc.)
- The row counts reinforce two key modeling choices: 6 pharmacists and 9
  technicians under `Employee`, plus 26 patient phone numbers for 20 patients
- 40 prescriptions distributed across all 5 pharmacies, enough to make aggregate
  queries meaningful without making the dataset hard to explain

---

## Slide 7 - Query Highlights (Part 1) _(Gavin)_

**Content:**

_Query 3: Pharmacies stocking all Pfizer drugs_

```sql
SELECT Pharmacy.name FROM Pharmacy
WHERE NOT EXISTS (
    SELECT Drug.drug_id FROM Drug
    JOIN DrugManufacturer ON Drug.manufacturer_id = DrugManufacturer.manufacturer_id
    WHERE DrugManufacturer.name = 'Pfizer'
    AND NOT EXISTS (
        SELECT PharmacySells.drug_id FROM PharmacySells
        WHERE PharmacySells.pharmacy_id = Pharmacy.pharmacy_id
        AND PharmacySells.drug_id = Drug.drug_id
    )
);
```

→ HealthPlus Pharmacy

_Query 4: Revenue per pharmacy_ → MediTrust $7,750 | CareWell $7,455 |
HealthPlus $5,291 | ...

_Query 2: Top drug per doctor specialty_ → Gastroenterology: Carvedilol (2
prescriptions)

**Notes:**

- Query 3 is the division query. Explain the double NOT EXISTS pattern briefly:
  "find pharmacies where there is no Pfizer drug that they don't carry"
- Query 4 joins 4 tables and multiplies quantity × price. It is a good example
  of a useful business query, not just a trivial join
- Query 2 uses a VIEW and correlated subquery to find the max per group

---

## Slide 8 - Query Highlights (Part 2) _(Gavin)_

**Content:**

_Query 9: Pharmacist patient counts_ → Emma Davis (MediTrust): 6 | Alice Smith
(HealthPlus): 5 | Carol White (CareWell): 5 | ...

_Query 11: Patients whose primary pharmacist never dispensed to them_

- Correlated NOT EXISTS across Patient and Prescription tables

_Query 12: Bulk price update_

```sql
UPDATE PharmacySells
SET price = ROUND(price * 1.10, 2)
WHERE drug_id IN (
    SELECT drug_id FROM Drug
    JOIN DrugManufacturer ON Drug.manufacturer_id = DrugManufacturer.manufacturer_id
    WHERE DrugManufacturer.name = 'AstraZeneca'
);
```

- Example result: Omeprazole at pharmacy 2 changed from 15.99 to 17.59

**Notes:**

- Query 9 demonstrates joining through the IS-A hierarchy (Pharmacist → Employee
  → Pharmacy)
- Query 11 is a good real-world example: a patient's assigned pharmacist may not
  be the one who fills their scripts in practice
- Query 12 shows a meaningful UPDATE, not just `SET x = y`, and uses a subquery
  filtering by manufacturer
- Mention one concrete updated row so the audience sees the effect immediately

---

## Slide 9 - Query Highlights (Part 3) _(Ryan)_

**Content:**

_Query 10: Prescriptions filled in the last 30 days_

- Date-filtered query against the most recent prescription date
- Columns: patient, doctor, drug, pharmacist, date, quantity
- Example latest row: Ivan Cruz | Dr. James Wilson | Aspirin | Emma Davis |
  2026-02-25 | 30

_Queries 12 & 13: Updates_

- Q12: +10% price on all AstraZeneca drugs across all pharmacies
- Q13: Transfer Laura Martinez from CareWell to MediTrust, shift Evening to
  Morning

_Query 14: Pharmacists licensed to dispense controlled substances_

- Joins license_number from Pharmacist with controlled_substance flag on Drug
- Shows which licensed pharmacists dispensed Gabapentin, Tramadol, or Trazodone

**Notes:**

- Run queries 12 and 13 live in the terminal to show the database is writable
- Query 10 is a practical day-to-day operational query. It is easy to understand
  and good for showing the data is realistic
- Query 14 is a good demo of how pharmacist credentials connect to
  controlled-substance dispensing, and the `controlled_substance` field also
  maps cleanly to a Django BooleanField in the admin
- If time is tight, show one row before and after for Query 13 instead of
  narrating the whole update

---

## Slide 10 - Django Admin Demo (1/3) _(Ryan)_

**Content:**

- Screenshot: Django admin index listing all 12 tables
- Headline: "Built a web UI on top of PharmacyDB.db using Django Admin"

**Notes:**

- "We pointed Django directly at the same SQLite file, with no data duplication"
- "No frontend code was written. Django generates all of this from the models"
- Keep this slide brief. It sets up the demo, and the next two slides show the
  actual functionality

---

## Slide 11 - Django Admin Demo (2/3) _(Ryan)_

**Content:**

- Screenshot: Prescription list view with patient name, doctor, drug, date,
  quantity columns
- Screenshot: single Prescription record open showing FK dropdowns

**Notes:**

- Point out the list filters (by pharmacist, by date). This shows the data is
  navigable
- The FK dropdowns are the key thing to highlight: clicking into a Prescription
  shows the linked Doctor, Patient, Pharmacist, and Drug records
- "All foreign key relationships from the schema are represented here"
- If possible, use a Prescription example that includes a controlled substance
  or a clearly recognizable drug name

---

## Slide 12 - Django Admin Demo (3/3) _(Ryan)_

**Content:**

- Live: create a new Prescription record via the admin form
- Live: edit a PharmacySells price

**Notes:**

- Full CRUD works on all 12 tables
- If time allows, intentionally enter an invalid value (e.g., wrong
  employee_type) to show the CHECK constraint fires
- "This shows the database isn't just a static design. It's a working system"

---

## Slide 13 - Team Responsibilities & Q&A _(Gavin)_

**Content:**

| Member | Responsibilities                                                                                                                                                                                             |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Ryan   | Refined the entity design, expanded the sample dataset, developed queries 10-14, built the Django admin interface, and prepared the written report.                                                          |
| Gavin  | Designed the ER diagram, finalized the relational schema and DDL, prepared the insert statements and database setup, developed queries 1-9, captured query outputs, and prepared the presentation materials. |

**Notes:**

- Keep the responsibilities summary quick, then move to questions
- Anticipated questions:
  - "Why did you choose a pharmacy?" - familiar domain, rich relationships
  - "How did you handle the IS-A hierarchy?" - discriminator + subtype tables
  - "Why does Prescription have both doctor_id and pharmacist_id?" - doctors
    prescribe, pharmacists dispense; these are different roles
  - "What does query X return and why?" - be ready for any of the 14
- End with: "Questions?"
