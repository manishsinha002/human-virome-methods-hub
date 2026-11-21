from pathlib import Path
import csv, html
ROOT=Path(__file__).resolve().parents[1]
def read(name):
    with (ROOT/'data'/name).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
def esc(v):return html.escape(v or '')
def table(rows, cols):
    out=['<table><thead><tr>']+[f'<th>{esc(label)}</th>' for _,label in cols]+['</tr></thead><tbody>']
    for r in rows:
        out.append('<tr>');out += [f'<td>{esc(r.get(key,''))}</td>' for key,_ in cols];out.append('</tr>')
    out += ['</tbody></table>'];return '\n'.join(out)
methods=read('methods.csv')
method_categories=[
    'Human-read removal',
    'Read-based profiling',
    'Assembly',
    'Viral-sequence identification',
    'Genome quality and clustering',
    'Virus–host and functional interpretation',
]
uncategorized=sorted({row['method_category'] for row in methods}-set(method_categories))
if uncategorized:
    raise ValueError(f'Unrecognized method categories: {uncategorized}')
method_cols=[('method_name','Method/tool'),('input_type','Input'),('main_strength','Main strength'),('main_limitation','Main limitation'),('best_use','Best use'),('unsupported_or_weak_claim','Do not infer'),('evidence_status','Evidence'),('review_section','Review section')]
method_sections=[]
for category in method_categories:
    rows=[row for row in methods if row['method_category']==category]
    if rows:
        method_sections += [f'## {category}\n\n<div class="methods-table">\n\n{table(rows,method_cols)}\n\n</div>']
text='# Computational methods matrix\n\nCompare tools by their primary analysis role. Category headings group the methods; the table focuses on input, fit, limitations, and evidentiary boundaries. These groupings are not endorsements. On narrower screens, scroll a table horizontally to see every column. For a tool to suggest, [submit a proposal for maintainer review](https://github.com/virome-hub/human-virome-methods-hub/issues/new?template=add-method.yml).\n\n'+'\n\n'.join(method_sections)+'\n'
(ROOT/'docs/methods.md').write_text(text,encoding='utf-8')
strategies=read('strategies.csv')
strategy_cols=[('strategy','Strategy'),('principal_fraction_measured','Principal fraction measured'),('strengths','Strengths'),('major_limitations_and_blind_spots','Blind spots'),('best_suited_applications','Best-suited applications')]
text='# Sequencing strategies\n\nSequencing strategy determines which viral fractions are observable and how well samples support detection, genome recovery, and interpretation. Compare the trade-offs below in the context of your specimen and research question. On narrower screens, scroll the table horizontally to see every column.\n\n<div class="strategies-table">\n\n'+table(strategies,strategy_cols)+'\n\n</div>\n'
(ROOT/'docs/strategies.md').write_text(text,encoding='utf-8')
print(f'Built {len(methods)} method rows and {len(strategies)} strategy rows.')
