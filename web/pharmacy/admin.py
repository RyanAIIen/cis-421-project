from django.contrib import admin
from .models import (
    Pharmacy,
    DrugManufacturer,
    Drug,
    Employee,
    Pharmacist,
    PharmacyTechnician,
    Doctor,
    Patient,
    PatientPhone,
    Prescription,
    PharmacyContract,
    PharmacySells,
)


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ( "name", "city", "state", "phone")
    search_fields = ("name", "city")
    list_filter = ("state",)


@admin.register(DrugManufacturer)
class DrugManufacturerAdmin(admin.ModelAdmin):
    list_display = ( "name", "city", "state")
    search_fields = ("name",)
    list_filter = ("state",)


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = (
        "trade_name",
        "manufacturer",
        "quantity",
        "controlled_substance",
    )
    search_fields = ("trade_name",)
    list_filter = ("controlled_substance", "manufacturer")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ( "name", "pharmacy", "employee_type", "shift_time")
    search_fields = ("name",)
    list_filter = ("employee_type", "pharmacy", "shift_time")


@admin.register(Pharmacist)
class PharmacistAdmin(admin.ModelAdmin):
    list_display = ("employee", "degree", "license_number")
    search_fields = ("employee__name", "license_number")
    list_filter = ("degree",)


@admin.register(PharmacyTechnician)
class PharmacyTechnicianAdmin(admin.ModelAdmin):
    list_display = ("employee", "certification")
    search_fields = ("employee__name",)
    list_filter = ("certification",)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ( "name", "specialty", "phone", "city", "state")
    search_fields = ("name", "specialty")
    list_filter = ("specialty", "state")


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sex",
        "insurance",
        "birthday",
        "city",
        "state",
    )
    search_fields = ("name",)
    list_filter = ("sex", "insurance", "state")


@admin.register(PatientPhone)
class PatientPhoneAdmin(admin.ModelAdmin):
    list_display = ("patient", "phone_number")
    search_fields = ("patient__name", "phone_number")


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = (
        "prescription_date",
        "patient",
        "doctor",
        "pharmacist",
        "drug",
        "quantity",
    )
    search_fields = ("patient__name", "doctor__name", "drug__trade_name")
    list_filter = ("prescription_date", "drug")
    date_hierarchy = "prescription_date"


@admin.register(PharmacyContract)
class PharmacyContractAdmin(admin.ModelAdmin):
    list_display = ("pharmacy", "manufacturer", "contract_date", "contract_end_date")
    search_fields = ("pharmacy__name", "manufacturer__name")
    list_filter = ("pharmacy", "manufacturer")


@admin.register(PharmacySells)
class PharmacySellsAdmin(admin.ModelAdmin):
    list_display = ("pharmacy", "drug", "price")
    search_fields = ("pharmacy__name", "drug__trade_name")
    list_filter = ("pharmacy",)
