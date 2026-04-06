# Pharmacy Database - Queries

## 1. Patients with prescriptions from more than one doctor

Find all patients who have received prescriptions written by at least two
different doctors. Show the patient name and how many distinct doctors have
prescribed to them.

'''sql
SELECT patient.name, COUNT(DISTINCT doctor.name) as num_doctors
FROM Prescription
JOIN Patient ON Prescription.patient_id = Patient.patient_id
JOIN Doctor ON Prescription.doctor_id = Doctor.doctor_id
GROUP BY patient.name 
HAVING num_doctors >= 2;
'''

## 2. Most commonly prescribed drug per doctor specialty

For each doctor specialty, find the drug that appears most often in
prescriptions. Show the specialty, drug name, and prescription count.

## 3. Pharmacies that sell every drug made by Pfizer

Find pharmacies that stock all drugs manufactured by Pfizer (relational
division). Show pharmacy name.

## 4. Revenue per pharmacy

Calculate the total revenue for each pharmacy based on prescription quantity
times the drug's selling price at that pharmacy. Show pharmacy name and total
revenue, ordered highest to lowest.

## 5. Patients with multiple phone numbers

List all patients who have more than one phone number on file. Show the patient
name and count of phone numbers.

## 6. Doctors who have prescribed to patients at every pharmacy

Find doctors whose prescriptions have been dispensed at all 5 pharmacies (via
the pharmacist's employer). Show doctor name.

## 7. Drugs never prescribed

Find all drugs in the database that do not appear in any prescription. Show
drug name and manufacturer name.

## 8. Average drug price comparison across pharmacies

For each drug sold by more than one pharmacy, show the drug name, lowest price,
highest price, and average price across all pharmacies that carry it.

## 9. Pharmacists and their patient counts, ranked

For each pharmacist, count how many unique patients they have dispensed
prescriptions to. Include the pharmacy they work at. Order by patient count
descending.

## 10. Prescriptions filled in the last 30 days

List all prescriptions filled within 30 days of the most recent prescription
date in the database. Show patient name, doctor name, drug name, pharmacist
name, date, and quantity.

## 11. Patients whose primary pharmacist has never dispensed to them

Find patients whose assigned primary pharmacist has not dispensed any of their
prescriptions. Show patient name, primary pharmacist name, and pharmacy.

## 12. Update drug prices by manufacturer

Increase the selling price by 10% for all drugs manufactured by AstraZeneca
across every pharmacy that carries them.

## 13. Transfer an employee to a different pharmacy

Move employee 'Laura Martinez' from her current pharmacy to 'MediTrust
Pharmacy' and update her shift to 'Morning'.
