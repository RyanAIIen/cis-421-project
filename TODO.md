# Pharmacy Database Project - TODO

## Remaining Work

### Queries

- [ ] Write SQL for queries 10–13 (Ryan)
- [ ] Add output results for queries 10–14 to `Query Outputs.md`
- [ ] Queries 6 and 7 have been reframed — Gavin's SQL in `queries.md` needs
      updating to match the new descriptions

### ER Diagram

- [ ] Update ER diagram in Lucidchart to reflect all changes since original:
  - Add Doctor entity and update Prescription relationship
  - Add `birthday` to Patient
  - Add `license_number` to Pharmacist
  - Add `controlled_substance` to Drug
- [ ] Re-export and commit updated diagram to `docs/`

### Report

- [ ] Write the project report (see sections below)
  - [ ] Application background
  - [ ] Database requirements specification
  - [ ] ER diagram
  - [ ] Relational schema
  - [ ] Sample database instance
  - [ ] SQL statements and query/update results
  - [ ] Team member responsibilities

### Presentation

- [ ] Build slides from `docs/presentation-outline.md`
- [ ] Practice to fit within 10 minutes

### Django Admin UI (Ryan)

- [ ] Set up Django project (`django-admin startproject pharmacydb`)
- [ ] Create a Django app (`python manage.py startapp pharmacy`)
- [ ] Point `settings.py` at the existing `PharmacyDB.db` file
- [ ] Run `python manage.py inspectdb` and clean up generated models
- [ ] Register all 12 models in `admin.py` with sensible `list_display`,
      `search_fields`, and `list_filter` options
- [ ] Verify CRUD works for all tables in the admin
- [ ] Create a superuser for the demo

**Notes:**
- Use `managed = False` on all models (don't let Django touch the existing schema)
- The IS-A hierarchy (Employee → Pharmacist/Technician) may need
  `OneToOneField` instead of the auto-generated FK — check inspectdb output
- No custom views or query UI needed — basic admin CRUD is sufficient
- Gavin can jump in if he has bandwidth
