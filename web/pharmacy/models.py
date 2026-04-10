from django.db import models


class Pharmacy(models.Model):
    pharmacy_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Pharmacy"
        verbose_name_plural = "Pharmacies"

    def __str__(self):
        return self.name


class DrugManufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "DrugManufacturer"
        verbose_name = "Drug Manufacturer"
        verbose_name_plural = "Drug Manufacturers"

    def __str__(self):
        return self.name


class Drug(models.Model):
    drug_id = models.AutoField(primary_key=True)
    trade_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        DrugManufacturer,
        on_delete=models.CASCADE,
        db_column="manufacturer_id",
    )
    quantity = models.IntegerField()
    controlled_substance = models.BooleanField()

    class Meta:
        managed = False
        db_table = "Drug"

    def __str__(self):
        return self.trade_name


class Employee(models.Model):
    EMPLOYEE_TYPES = [
        ("Pharmacist", "Pharmacist"),
        ("Technician", "Technician"),
    ]

    employee_id = models.AutoField(primary_key=True)
    pharmacy = models.ForeignKey(
        Pharmacy,
        on_delete=models.CASCADE,
        db_column="pharmacy_id",
    )
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    employee_type = models.CharField(max_length=20, choices=EMPLOYEE_TYPES)
    shift_time = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Employee"

    def __str__(self):
        return self.name


class Pharmacist(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column="employee_id",
    )
    degree = models.CharField(max_length=50, blank=True, null=True)
    license_number = models.CharField(max_length=50, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Pharmacist"

    def __str__(self):
        return self.employee.name


class PharmacyTechnician(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column="employee_id",
    )
    certification = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "PharmacyTechnician"
        verbose_name = "Pharmacy Technician"
        verbose_name_plural = "Pharmacy Technicians"

    def __str__(self):
        return self.employee.name


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Doctor"

    def __str__(self):
        return f"Dr. {self.name}"


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, blank=True, null=True)
    insurance = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    primary_pharmacist = models.ForeignKey(
        Pharmacist,
        on_delete=models.SET_NULL,
        db_column="primary_pharmacist_id",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "Patient"

    def __str__(self):
        return self.name


class PatientPhone(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        db_column="patient_id",
    )
    phone_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "PatientPhone"
        verbose_name = "Patient Phone"
        verbose_name_plural = "Patient Phones"
        unique_together = (("patient", "phone_number"),)

    def __str__(self):
        return f"{self.patient.name}: {self.phone_number}"


class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        db_column="doctor_id",
    )
    pharmacist = models.ForeignKey(
        Pharmacist,
        on_delete=models.CASCADE,
        db_column="pharmacist_id",
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        db_column="patient_id",
    )
    drug = models.ForeignKey(
        Drug,
        on_delete=models.CASCADE,
        db_column="drug_id",
    )
    prescription_date = models.DateField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = "Prescription"

    def __str__(self):
        return f"Rx #{self.prescription_id} - {self.patient.name}"


class PharmacyContract(models.Model):
    id = models.AutoField(primary_key=True)
    pharmacy = models.ForeignKey(
        Pharmacy,
        on_delete=models.CASCADE,
        db_column="pharmacy_id",
    )
    manufacturer = models.ForeignKey(
        DrugManufacturer,
        on_delete=models.CASCADE,
        db_column="manufacturer_id",
    )
    contract_date = models.DateField(blank=True, null=True)
    contract_end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "PharmacyContract"
        verbose_name = "Pharmacy Contract"
        verbose_name_plural = "Pharmacy Contracts"
        unique_together = (("pharmacy", "manufacturer"),)

    def __str__(self):
        return f"{self.pharmacy.name} <-> {self.manufacturer.name}"


class PharmacySells(models.Model):
    id = models.AutoField(primary_key=True)
    pharmacy = models.ForeignKey(
        Pharmacy,
        on_delete=models.CASCADE,
        db_column="pharmacy_id",
    )
    drug = models.ForeignKey(
        Drug,
        on_delete=models.CASCADE,
        db_column="drug_id",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = "PharmacySells"
        verbose_name = "Pharmacy Sells"
        verbose_name_plural = "Pharmacy Sells"
        unique_together = (("pharmacy", "drug"),)

    def __str__(self):
        return f"{self.pharmacy.name} sells {self.drug.trade_name} @ ${self.price}"
