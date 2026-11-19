from pathlib import Path
import csv
import sys

required = {
    'methods.csv': {'method_id', 'method_name', 'analysis_stage', 'input_type', 'main_strength', 'main_limitation', 'best_use', 'evidence_status', 'last_reviewed'},
    'specimen_matrix.csv': {'record_id', 'specimen', 'method_or_strategy', 'viral_fraction_recovered', 'viral_fraction_depleted', 'best_use', 'limitation', 'evidence_status', 'last_reviewed'},
    'benchmarks.csv': {'benchmark_id', 'name', 'sample_type', 'ground_truth_type', 'sequencing_type', 'controls_available', 'accession_or_url', 'reference_id', 'last_reviewed'},
    'references.csv': {'reference_id', 'doi', 'pmid', 'title', 'year', 'topic', 'evidence_type', 'date_added', 'review_status'},
}

errors = []
for filename, fields in required.items():
    path = Path('data') / filename
    if not path.exists():
        errors.append(f'Missing {path}')
        continue
    with path.open(newline='', encoding='utf-8') as handle:
        reader = csv.DictReader(handle)
        missing = fields - set(reader.fieldnames or [])
        if missing:
            errors.append(f'{filename}: missing columns {sorted(missing)}')
        for line_number, row in enumerate(reader, start=2):
            if not any((value or '').strip() for value in row.values()):
                errors.append(f'{filename}:{line_number}: blank row')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('All structured data files passed schema validation.')
