# The Best HR: gap audit (Egypt edition)

Base: fork of frappe/hrms `develop` (commit 817351d78, 2026-11-19). Branch: `egypt-edition-v2`.
Status words used everywhere in this repo:
- **Implemented**: code is on the branch.
- **Verified**: run/tested (state where: unit test, dev bench, real device).
- **Production-ready**: reviewed for legal and operational use. Nothing is production-ready yet.

## Legal constraint (internal decision, pending owner review)
Biometric features (face check-in) are **demo on an isolated environment only**. No real employees enrolled, no real biometric or location data moved, no payroll based on it, no production deployment until the Egyptian PDPC requirements are reviewed (biometric data is sensitive: separate licence, mandatory non-biometric alternative).

## Audit table (state on the branch today)

| Area | Upstream already has | Egypt gap | State |
|---|---|---|---|
| Branding | - | The Best HR / TB title, PWA icons | Implemented (3 commits), not Verified visually |
| Attendance and check-in | Employee Checkin, Shift Type, auto attendance, late/early grace, shift locations with lat/long (geofence), mobile PWA | Per-site geofence UX check, Arabic labels | Upstream feature, not Verified by us |
| Lateness / absence | Late entry marking, grace period, absent marking | Egypt deduction policy (late minutes to salary) | Gap |
| Overtime | Overtime Type / Slip / Details | Egyptian overtime rates (labour law) as settings | Gap |
| Payroll tax | India and UAE regional code only; generic Income Tax Slab | Egyptian earned-income tax slabs (as settings) | Gap |
| Social insurance | none | Law 148/2019 employee/employer shares, min/max insurable wage (as settings, not hard-coded) | Gap |
| Arabic | `hrms/locale/ar.po` exists | ~1500 of ~2250 entries still empty (counted by empty msgstr, approximate) | Gap |
| RTL | Org chart RTL fix upstream | Full UI RTL check on dev bench | Gap, not tested |
| Fingerprint devices | Generic check-in API | Device integration (ZKTeco push/pull) | Gap |
| Face check-in | none | Demo behind launch gate, off by default | Gap |
| Deployment | docker/ | New Proxmox, not yet provided | Blocked on owner |

## Rules for the next steps
1. Egypt logic lives in a separate custom app (`the_best_hr_egypt`), not in the core fork, so upstream merges stay clean.
2. Tax and insurance numbers are editable settings with a stated source and effective date; values must be confirmed against current official sources before use.
3. Every claim in reports is labelled Implemented / Verified / Production-ready.
