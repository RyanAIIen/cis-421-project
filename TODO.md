# Pharmacy Database Project - TODO

## Schema Decisions

### 1. "Prescribes" Problem (CRITICAL)

Pharmacists don't prescribe - doctors do. Two options:

**A. Add Doctor entity** (preferred)

- Doctor entity: `Doctor(<u>doctor_id</u>, name, specialty, license_number, phone, street, city, state)`
- Split into two tables:
  - Prescription: doctor_id, patient_id, drug_id, prescription_date, quantity, refills_remaining, dosage_instructions
  - Dispensing: prescription_id, pharmacist_id, pharmacy_id, dispense_date, quantity_dispensed
- More realistic, better queries, demonstrates understanding

**B. Quick fix**

- Just rename to "Dispenses"
- Less work but less realistic/impressive

### 2. Other Enhancements to Discuss

- **Pharmacy address**: Split into street/city/state (matches other entities)
- **Patient birthday**: Add for age-based queries (employees already have it)
- **Drug details**: Add generic_name, dosage_form, strength
- **Prescription fields**: Add refills_remaining, dosage_instructions, expiration_date
- **Credentials**: Add license/cert numbers and expiration dates to pharmacist/technician

## Implementation Checklist

### Must fix:

- [ ] Prescribes semantic issue (add Doctor or rename)

### Should do:

- [ ] Pharmacy address (split into street/city/state)
- [ ] Add birthday to Patient
- [ ] Enhance Drug entity with generic name, form, strength
- [ ] Prescription details (refills, instructions, expiration)

### If we have time:

- [ ] License/certification tracking
- [ ] Controlled substance flag on drugs

## Sample Data Plan

Quantities needed:

- 3-5 Pharmacies
- 10-15 Employees
- 20-30 Patients
- 30-50 Drugs
- 5-10 Manufacturers
- 40+ Prescriptions

Data sources:

- Real FDA drug names (Lipitor, Advil, Metformin)
- Fake name generator for people
- MD/DC/VA cities for addresses

Must demonstrate: Foreign keys, CHECK constraints, NOT NULL, multi-valued attributes, IS-A hierarchy

## Query Ideas (need 10+)

Categories to cover:

- Simple selects (pharmacies by state, drugs by manufacturer)
- Joins (prescriptions with names, employees with pharmacy)
- Aggregates (count per pharmacist, average prices, totals)
- Complex (division query, multiple joins, NOT EXISTS)
- Subqueries (more than average)
- Updates/Deletes (price changes, employee transfers)

Specific examples:

1. Pharmacies in Maryland selling Lipitor
2. Pharmacists and their patient counts
3. Patients with 5+ medications
4. Total revenue per pharmacy
5. Drugs not stocked anywhere
6. Prescriptions filled in last 30 days
7. Manufacturers supplying all pharmacies (division)
8. Patients with multiple phone numbers
9. Expiring licenses (if implemented)
10. Most commonly prescribed drugs

## Django Admin UI (Ryan)

A lightweight Django app pointing at `PharmacyDB.db` for a polished demo.
Ryan is handling this — Gavin can jump in if he has bandwidth.

### Steps:

- [ ] Set up Django project (`django-admin startproject pharmacydb`)
- [ ] Create a Django app (`python manage.py startapp pharmacy`)
- [ ] Point `settings.py` at the existing `PharmacyDB.db` file
- [ ] Run `python manage.py inspectdb` and clean up generated models
- [ ] Register all 12 models in `admin.py` with sensible `list_display`,
      `search_fields`, and `list_filter` options
- [ ] Verify CRUD works for all tables in the admin
- [ ] Create a superuser for the demo

### Notes:

- Use `managed = False` on all models (don't let Django touch the existing schema)
- The IS-A hierarchy (Employee → Pharmacist/Technician) may need
  `OneToOneField` instead of the auto-generated FK — check inspectdb output
- No custom views or query UI needed — basic admin CRUD is sufficient

## Timeline

**This week:**

- Meet and decide on Doctor entity
- Fix pharmacy address
- Update ER diagram

**Week 1:** Finalize schema, write DDL, test in SQLite
**Week 2:** Create sample data, load it, write queries
**Week 3:** Finish queries, write report, make slides, practice presentation

Report sections: background, requirements, ER, schema, data, queries/results, team responsibilities

## Notes

- WorkShift: ✓ RESOLVED (added shift_time to Employee)
- Patient phone: ✓ Multi-valued (PatientPhone table created)
- PatientPharmacist: ✓ RESOLVED (removed bridge table, added FK to Patient)
- Address: Implemented as street/city/state columns
- Employee IS-A: Using discriminator + separate Pharmacist/Technician tables
- ER tool: Lucidchart
