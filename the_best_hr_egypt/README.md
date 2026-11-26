# the_best_hr_egypt

Egypt payroll logic for The Best HR, kept outside the hrms core so upstream merges stay clean.
Status: **Implemented + unit-tested (pure Python)**. Not yet wired into Salary Slip, not run on a Frappe bench, not production-ready.
Rates are data (`payroll/egypt_rates_2026.json`) with source and effective year; confirm against official sources before real payroll.
Run tests: `python3 -m unittest discover -s tests -t .` from this folder.
