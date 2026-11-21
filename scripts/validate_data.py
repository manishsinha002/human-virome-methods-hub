from pathlib import Path
import csv, json, sys
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
reference_path=Path('data/references.csv')
methods_path=Path('data/methods.csv')
if reference_path.exists() and methods_path.exists():
 with reference_path.open(newline='',encoding='utf-8') as f:
  reference_ids={row['reference_id'].strip() for row in csv.DictReader(f) if row.get('reference_id')}
 with methods_path.open(newline='',encoding='utf-8') as f:
  for i,row in enumerate(csv.DictReader(f),start=2):
   for reference_id in (row.get('reference_ids') or '').split(';'):
    reference_id=reference_id.strip()
    if reference_id and reference_id not in reference_ids:
     errors.append(f'methods.csv:{i}: unknown reference_id {reference_id}')
workflow_path=Path('data/workflow.json')
if not workflow_path.exists():
    errors.append(f'Missing {workflow_path}')
else:
    try:
        workflow=json.loads(workflow_path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as error:
        errors.append(f'{workflow_path}:{error.lineno}: invalid JSON: {error.msg}')
    else:
        nodes=workflow.get('nodes') if isinstance(workflow,dict) else None
        if not isinstance(nodes,list) or not nodes:
            errors.append('workflow.json: nodes must be a non-empty list')
        else:
            with methods_path.open(newline='',encoding='utf-8') as f:
                known_method_ids={row['method_id'] for row in csv.DictReader(f)}
            node_ids=set()
            required_node_fields={'id','label','summary','why_it_matters','outputs','caveat','method_ids','review_sections','links'}
            for index,node in enumerate(nodes,start=1):
                if not isinstance(node,dict):
                    errors.append(f'workflow.json:nodes[{index-1}]: expected an object')
                    continue
                missing=required_node_fields-set(node)
                if missing:
                    errors.append(f'workflow.json:nodes[{index-1}]: missing fields {sorted(missing)}')
                for field in {'id','label','summary','why_it_matters','outputs','caveat'}:
                    value=node.get(field)
                    if not isinstance(value,str) or not value.strip():
                        errors.append(f'workflow.json:nodes[{index-1}]: {field} must be a non-empty string')
                node_id=node.get('id')
                if not isinstance(node_id,str) or not node_id.strip():
                    errors.append(f'workflow.json:nodes[{index-1}]: id must be a non-empty string')
                elif node_id in node_ids:
                    errors.append(f'workflow.json:nodes[{index-1}]: duplicate id {node_id}')
                else:
                    node_ids.add(node_id)
                method_ids=node.get('method_ids',[])
                if not isinstance(method_ids,list):
                    errors.append(f'workflow.json:nodes[{index-1}]: method_ids must be a list')
                else:
                    for method_id in method_ids:
                        if not isinstance(method_id,str) or not method_id.strip():
                            errors.append(f'workflow.json:nodes[{index-1}]: method_id values must be non-empty strings')
                        elif method_id not in known_method_ids:
                            errors.append(f'workflow.json:nodes[{index-1}]: unknown method_id {method_id}')
                review_sections=node.get('review_sections',[])
                if not isinstance(review_sections,list) or any(not isinstance(section,str) or not section.strip() for section in review_sections):
                    errors.append(f'workflow.json:nodes[{index-1}]: review_sections must be a list of non-empty strings')
                links=node.get('links',[])
                if not isinstance(links,list):
                    errors.append(f'workflow.json:nodes[{index-1}]: links must be a list')
                else:
                    for link_index,link in enumerate(links):
                        if not isinstance(link,dict) or not isinstance(link.get('label'),str) or not link['label'].strip() or not isinstance(link.get('url'),str) or not link['url'].strip():
                            errors.append(f'workflow.json:nodes[{index-1}].links[{link_index}]: label and url are required')
if errors:print('\n'.join(errors));sys.exit(1)
print('All structured data files passed schema validation.')
