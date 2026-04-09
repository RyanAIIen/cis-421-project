# Pharmacy Database - Queries

## 1. Patients with prescriptions from more than one doctor

Find all patients who have received prescriptions written by at least two
different doctors. Show the patient name and how many distinct doctors have
prescribed to them.

```sql
SELECT patient.name, COUNT(DISTINCT doctor.name) as num_doctors
FROM Prescription
JOIN Patient ON Prescription.patient_id = Patient.patient_id
JOIN Doctor ON Prescription.doctor_id = Doctor.doctor_id
GROUP BY patient.name
HAVING num_doctors >= 2;
```

## 2. Most commonly prescribed drug per doctor specialty

For each doctor specialty, find the drug that appears most often in
prescriptions. Show the specialty, drug name, and prescription count.

```sql
CREATE VIEW doctor_prescription_summary AS
SELECT specialty, trade_name, COUNT(prescription.prescription_id) as num_prescriptions
FROM doctor
JOIN prescription ON Doctor.doctor_id = prescription.doctor_id
JOIN drug ON prescription.drug_id = drug.drug_id
GROUP BY specialty, trade_name;
```

```sql
SELECT specialty, trade_name, num_prescriptions
FROM doctor_prescription_summary AS main
WHERE num_prescriptions = (
    SELECT MAX(num_prescriptions)
    FROM doctor_prescription_summary AS sub
    WHERE main.specialty = sub.specialty
);
```

```sql
DROP VIEW doctor_prescription_summary;
```

## 3. Pharmacies that sell every drug made by Pfizer

Find pharmacies that stock all drugs manufactured by Pfizer (relational
division). Show pharmacy name.

```sql
SELECT Pharmacy.name
FROM Pharmacy
WHERE NOT EXISTS (
    SELECT Drug.drug_id
    FROM Drug
    JOIN DrugManufacturer ON Drug.manufacturer_id = DrugManufacturer.manufacturer_id
    WHERE DrugManufacturer.name = 'Pfizer'
    AND NOT EXISTS (
        SELECT PharmacySells.drug_id
        FROM PharmacySells
        WHERE PharmacySells.pharmacy_id = Pharmacy.pharmacy_id
        AND PharmacySells.drug_id = Drug.drug_id
    )
);
```

## 4. Revenue per pharmacy

Calculate the total revenue for each pharmacy based on prescription quantity
times the drug's selling price at that pharmacy. Show pharmacy name and total
revenue, ordered highest to lowest.

```sql
SELECT Pharmacy.name, SUM(Prescription.quantity * PharmacySells.price) AS total_revenue
FROM Prescription
JOIN Employee ON Prescription.pharmacist_id = Employee.employee_id
JOIN Pharmacy ON Employee.pharmacy_id = Pharmacy.pharmacy_id
JOIN PharmacySells ON Pharmacy.pharmacy_id = PharmacySells.pharmacy_id
    AND Prescription.drug_id = PharmacySells.drug_id
GROUP BY Pharmacy.name
ORDER BY total_revenue DESC;
```

## 5. Patients with multiple phone numbers

List all patients who have more than one phone number on file. Show the patient
name and count of phone numbers.

```sql
SELECT Patient.name, COUNT(PatientPhone.phone_number) AS phone_count
FROM Patient
JOIN PatientPhone ON Patient.patient_id = PatientPhone.patient_id
GROUP BY Patient.patient_id
HAVING phone_count > 1;
```

## 6. Doctors who have prescribed at 3 or more pharmacies

Find doctors whose prescriptions have been dispensed at 3 or more distinct
pharmacies (via the pharmacist's employer). Show doctor name and pharmacy count.

```sql
SELECT Doctor.name, COUNT(DISTINCT Employee.pharmacy_id) AS pharmacy_count
FROM Doctor
JOIN Prescription ON Doctor.doctor_id = Prescription.doctor_id
JOIN Employee ON Prescription.pharmacist_id = Employee.employee_id
GROUP BY Doctor.doctor_id
HAVING pharmacy_count >= 3
ORDER BY pharmacy_count DESC, Doctor.name;
```

## 7. Drugs stocked at exactly one pharmacy

Find drugs carried by only a single pharmacy — useful for identifying exclusive
or low-distribution medications. Show drug name and manufacturer.

```sql
SELECT Drug.trade_name, DrugManufacturer.name AS manufacturer
FROM Drug
JOIN DrugManufacturer ON Drug.manufacturer_id = DrugManufacturer.manufacturer_id
WHERE (
    SELECT COUNT(DISTINCT PharmacySells.pharmacy_id)
    FROM PharmacySells
    WHERE PharmacySells.drug_id = Drug.drug_id
) = 1
ORDER BY Drug.trade_name;
```

## 8. Average drug price comparison across pharmacies

For each drug sold by more than one pharmacy, show the drug name, lowest price,
highest price, and average price across all pharmacies that carry it.

```sql
SELECT
    Drug.trade_name,
    MIN(PharmacySells.price) AS lowest_price,
    MAX(PharmacySells.price) AS highest_price,
    AVG(PharmacySells.price) AS average_price
FROM Drug
JOIN PharmacySells ON Drug.drug_id = PharmacySells.drug_id
GROUP BY Drug.trade_name
HAVING COUNT(DISTINCT PharmacySells.pharmacy_id) > 1;
```

## 9. Pharmacists and their patient counts, ranked

For each pharmacist, count how many unique patients they have dispensed
prescriptions to. Include the pharmacy they work at. Order by patient count
descending.

```sql
SELECT Employee.name AS Pharmacist_name, Pharmacy.name AS Pharmacy_name,
    COUNT(DISTINCT Prescription.patient_id) AS patient_count
FROM Pharmacist
JOIN Employee ON Pharmacist.employee_id = Employee.employee_id
JOIN Pharmacy ON Employee.pharmacy_id = Pharmacy.pharmacy_id
JOIN Prescription ON Pharmacist.employee_id = Prescription.pharmacist_id
GROUP BY Pharmacist.employee_id, Employee.name, Pharmacy.name
ORDER BY patient_count DESC;
```

## 10. Prescriptions filled in the last 30 days

List all prescriptions filled within 30 days of the most recent prescription
date in the database. Show patient name, doctor name, drug name, pharmacist
name, date, and quantity.

```sql
SELECT Patient.name AS patient, Doctor.name AS doctor, Drug.trade_name AS drug,
    Employee.name AS pharmacist, Prescription.prescription_date AS date,
    Prescription.quantity
FROM Prescription
JOIN Patient ON Prescription.patient_id = Patient.patient_id
JOIN Doctor ON Prescription.doctor_id = Doctor.doctor_id
JOIN Drug ON Prescription.drug_id = Drug.drug_id
JOIN Employee ON Prescription.pharmacist_id = Employee.employee_id
WHERE Prescription.prescription_date >= DATE(
    (SELECT MAX(prescription_date) FROM Prescription), '-30 days'
)
ORDER BY Prescription.prescription_date DESC;
```

## 11. Patients whose primary pharmacist has never dispensed to them

Find patients whose assigned primary pharmacist has not dispensed any of their
prescriptions. Show patient name, primary pharmacist name, and pharmacy.

```sql
SELECT Patient.name AS patient, Employee.name AS primary_pharmacist,
    Pharmacy.name AS pharmacy
FROM Patient
JOIN Pharmacist ON Patient.primary_pharmacist_id = Pharmacist.employee_id
JOIN Employee ON Pharmacist.employee_id = Employee.employee_id
JOIN Pharmacy ON Employee.pharmacy_id = Pharmacy.pharmacy_id
WHERE NOT EXISTS (
    SELECT * FROM Prescription
    WHERE Prescription.patient_id = Patient.patient_id
    AND Prescription.pharmacist_id = Patient.primary_pharmacist_id
)
ORDER BY Patient.name;
```

## 12. Update drug prices by manufacturer

Increase the selling price by 10% for all drugs manufactured by AstraZeneca
across every pharmacy that carries them.

```sql
UPDATE PharmacySells
SET price = ROUND(price * 1.10, 2)
WHERE drug_id IN (
    SELECT Drug.drug_id FROM Drug
    JOIN DrugManufacturer ON Drug.manufacturer_id = DrugManufacturer.manufacturer_id
    WHERE DrugManufacturer.name = 'AstraZeneca'
);
```

## 13. Transfer an employee to a different pharmacy

Move employee 'Laura Martinez' from her current pharmacy to 'MediTrust Pharmacy'
and update her shift to 'Morning'.

```sql
UPDATE Employee
SET pharmacy_id = (SELECT pharmacy_id FROM Pharmacy WHERE name = 'MediTrust Pharmacy'),
    shift_time = 'Morning'
WHERE name = 'Laura Martinez';
```

## 14. Pharmacists licensed to dispense controlled substances

List all pharmacists who have dispensed at least one controlled substance, along
with their license number, pharmacy, and the controlled drugs they dispensed.

```sql
SELECT DISTINCT Employee.name AS pharmacist, Pharmacist.license_number,
    Pharmacy.name AS pharmacy, Drug.trade_name AS controlled_drug
FROM Pharmacist
JOIN Employee ON Pharmacist.employee_id = Employee.employee_id
JOIN Pharmacy ON Employee.pharmacy_id = Pharmacy.pharmacy_id
JOIN Prescription ON Pharmacist.employee_id = Prescription.pharmacist_id
JOIN Drug ON Prescription.drug_id = Drug.drug_id
WHERE Drug.controlled_substance = 1
ORDER BY Employee.name, Drug.trade_name;
```
