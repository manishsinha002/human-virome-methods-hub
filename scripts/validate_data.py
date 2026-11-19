from pathlib import Path
import csv, sys
required={
'methods.csv':{'method_id','method_name','method_category','analysis_stage','input_type','main_strength','main_limitation','best_use','unsupported_or_weak_claim','evidence_status','reference_ids','review_section','last_reviewed'},
'strategies.csv':{'strategy_id','strategy','principal_fraction_measured','strengths','major_limitations_and_blind_spots','best_suited_applications','review_section','last_reviewed'},
'specimen_matrix.csv':{'record_id','specimen','method_or_strategy','viral_fraction_recovered','viral_fraction_depleted','best_use','limitation','evidence_status','last_reviewed'},
'benchmarks.csv':{'benchmark_id','name','sample_type','ground_truth_type','sequencing_type','controls_available','accession_or_url','reference_id','last_reviewed'},
'references.csv':{'reference_id','doi','pmid','title','year','topic','evidence_type','date_added','review_status'}}
errors=[]
for filename,fields in required.items():
 p=Path('data')/filename
 if not p.exists():errors.append(f'Missing {p}');continue
 with p.open(newline='',encoding='utf-8') as f:
  reader=csv.DictReader(f);missing=fields-set(reader.fieldnames or [])
  if missing:errors.append(f'{filename}: missing columns {sorted(missing)}')
  ids=[]
  for i,row in enumerate(reader,start=2):
   if not any((v or '').strip() for v in row.values()):errors.append(f'{filename}:{i}: blank row')
   first=(reader.fieldnames or [''])[0]; value=(row.get(first) or '').strip()
   if value in ids:errors.append(f'{filename}:{i}: duplicate {first} {value}')
   ids.append(value)
if errors:print('\n'.join(errors));sys.exit(1)
print('All structured data files passed schema validation.')
