# Presentation Outline

10 minutes total. Suggested split: ~1 min per slide.

**Slide assignments:**

- **Ryan**: Slides 6, 9, 10, 11, 12
- **Gavin**: Slides 1, 2, 3, 4, 5, 7, 8, 13

---

## Slide 1 — Title _(Gavin)_

**Content:**

- "Pharmacy Database System"
- CIS-421
- Ryan Allen, Gavin Tank
- Date

**Notes:**

- Brief intro — who you are, what the project is

---

## Slide 2 — Application Background _(Gavin)_

**Content:**

- A regional chain of retail pharmacies operating across Michigan
- Key actors: pharmacies, doctors, patients, pharmacists, technicians, drug
  manufacturers
- Core operations: prescriptions, drug inventory, staff scheduling, manufacturer
  contracts

**Notes:**

- Set the scene quickly — this slide shouldn't take more than 45 seconds
- Emphasize that this is a realistic enterprise with real relationships between
  entities, not a toy example

---

## Slide 3 — Database Requirements _(Gavin)_

**Content:**

- Track pharmacy locations and staff (IS-A: pharmacists and technicians)
- Track doctors who write prescriptions
- Track patients with multi-valued phone numbers
- Track drugs, manufacturers, and per-pharmacy pricing
- Track prescriptions: doctor → patient → pharmacist → drug
- Track contracts between pharmacies and manufacturers

**Notes:**

- Call out the interesting modeling challenges: IS-A hierarchy, multi-valued
  attribute, derived age from birthday
- This slide motivates why the ER diagram looks the way it does

---

## Slide 4 — ER Diagram _(Gavin)_

**Content:**

- Full ER diagram (Lucidchart export)

**Notes:**

- Walk through the diagram entity by entity — don't just show it silently
- Key points to call out:
  - IS-A hierarchy: Employee → Pharmacist / PharmacyTechnician (overlapping?
    disjoint?)
  - Prescription connects Doctor, Pharmacist, Patient, and Drug
  - Patient phone is a multi-valued attribute (double oval)
  - Age is a derived attribute (dashed oval) — computed from birthday at query
    time
- Don't get lost in the details — hit the highlights and move on

---

## Slide 5 — Relational Schema _(Gavin)_

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
- Mention Prescription has both `doctor_id` and `pharmacist_id` — doctors
  prescribe, pharmacists dispense

---

## Slide 6 — Sample Database _(Ryan)_

**Content:**

| Table            | Rows |
| ---------------- | ---- |
| Pharmacy         | 5    |
| Employee         | 15   |
| Doctor           | 8    |
| Patient          | 20   |
| Drug             | 30   |
| DrugManufacturer | 8    |
| Prescription     | 40   |
| PharmacySells    | 50   |
| PharmacyContract | 19   |

**Notes:**

- Data is Michigan-based: Dearborn, Detroit, Ann Arbor, Ypsilanti, Lansing
- Drug names are real FDA-approved drugs (Metformin, Lisinopril, Atorvastatin,
  etc.)
- 40 prescriptions distributed across all 5 pharmacies — enough to make
  aggregate queries meaningful

---

## Slide 7 — Query Highlights (Part 1) _(Gavin)_

**Content:**

_Query 3 — Pharmacies stocking all Pfizer drugs_

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

_Query 4 — Revenue per pharmacy_ → MediTrust $7,750 | CareWell $7,455 |
HealthPlus $5,291 | ...

_Query 2 — Top drug per doctor specialty_ → Gastroenterology: Carvedilol (2
prescriptions)

**Notes:**

- Query 3 is the division query — explain the double NOT EXISTS pattern briefly:
  "find pharmacies where there is no Pfizer drug that they don't carry"
- Query 4 joins 4 tables and multiplies quantity × price — show the SQL if time
  allows
- Query 2 uses a VIEW and correlated subquery to find the max per group

---

## Slide 8 — Query Highlights (Part 2) _(Gavin)_

**Content:**

_Query 9 — Pharmacist patient counts_ → Emma Davis (MediTrust): 6 | Alice Smith
(HealthPlus): 5 | Carol White (CareWell): 5 | ...

_Query 11 — Patients whose primary pharmacist never dispensed to them_

- Correlated NOT EXISTS across Patient and Prescription tables

_Query 12 — Bulk price update_

```sql
UPDATE PharmacySells
SET price = price * 1.10
WHERE drug_id IN (
    SELECT drug_id FROM Drug
    JOIN DrugManufacturer ON Drug.manufacturer_id = DrugManufacturer.manufacturer_id
    WHERE DrugManufacturer.name = 'AstraZeneca'
);
```

**Notes:**

- Query 9 demonstrates joining through the IS-A hierarchy (Pharmacist → Employee
  → Pharmacy)
- Query 11 is a good real-world example: a patient's assigned pharmacist may not
  be the one who fills their scripts in practice
- Query 12 shows a meaningful UPDATE — not just `SET x = y` but with a subquery
  filtering by manufacturer

---

## Slide 9 — Query Highlights (Part 3) _(Ryan)_

**Content:**

_Query 10 — Prescriptions filled in the last 30 days_

- Date-filtered query against the most recent prescription date
- Columns: patient, doctor, drug, pharmacist, date, quantity

_Queries 12 & 13 — Updates_

- Q12: +10% price on all AstraZeneca drugs across all pharmacies
- Q13: Transfer Laura Martinez to MediTrust Pharmacy, shift → Morning

_Query 14 — Pharmacists licensed to dispense controlled substances_

- Joins license_number from Pharmacist with controlled_substance flag on Drug
- Shows which licensed pharmacists dispensed Gabapentin, Tramadol, or Trazodone

**Notes:**

- Run queries 12 and 13 live in the terminal to show the database is writable
- Query 10 is a practical day-to-day operational query — easy to understand,
  good for showing the data is realistic
- Query 14 is a good demo of the two new fields added late in the project —
  mention that controlled_substance maps to a Django BooleanField (checkbox in
  admin)

---

## Slide 10 — Django Admin Demo (1/3) _(Ryan)_

**Content:**

- Screenshot: Django admin index listing all 12 tables
- Headline: "Built a web UI on top of PharmacyDB.db using Django Admin"

**Notes:**

- "We pointed Django directly at the same SQLite file — no data duplication"
- "No frontend code was written — Django generates all of this from the models"
- Keep this slide brief — it's just the intro to the demo, the next two slides
  show the actual functionality

---

## Slide 11 — Django Admin Demo (2/3) _(Ryan)_

**Content:**

- Screenshot: Prescription list view with patient name, doctor, drug, date,
  quantity columns
- Screenshot: single Prescription record open showing FK dropdowns

**Notes:**

- Point out the list filters (by pharmacist, by date) — shows the data is
  navigable
- The FK dropdowns are the key thing to highlight: clicking into a Prescription
  shows the linked Doctor, Patient, Pharmacist, and Drug records
- "All foreign key relationships from the schema are represented here"

---

## Slide 12 — Django Admin Demo (3/3) _(Ryan)_

**Content:**

- Live: create a new Prescription record via the admin form
- Live: edit a PharmacySells price

**Notes:**

- Full CRUD works on all 12 tables
- If time allows, intentionally enter an invalid value (e.g., wrong
  employee_type) to show the CHECK constraint fires
- "This shows the database isn't just a homework exercise — it's functional"

---

## Slide 13 — Team Responsibilities & Q&A _(Gavin)_

**Content:**

| Member | Responsibilities                                                                       |
| ------ | -------------------------------------------------------------------------------------- |
| Ryan   | Doctor entity, sample data, queries 10–14, Django admin UI, slides 6/9–12              |
| Gavin  | Schema DDL, SQL inserts, database setup, queries 1–9, query outputs, slides 1–5/7–8/13 |

**Notes:**

- Mention that both members can run and explain any query
- Anticipated questions:
  - "Why did you choose a pharmacy?" — familiar domain, rich relationships
  - "How did you handle the IS-A hierarchy?" — discriminator + subtype tables
  - "Why does Prescription have both doctor_id and pharmacist_id?" — doctors
    prescribe, pharmacists dispense; these are different roles
  - "What does query X return and why?" — be ready for any of the 14
- End with: "Questions?"
