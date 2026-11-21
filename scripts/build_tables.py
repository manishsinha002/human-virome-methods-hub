from pathlib import Path
import csv, html
ROOT=Path(__file__).resolve().parents[1]
def read(name):
    with (ROOT/'data'/name).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
def esc(v):return html.escape(v or '')
def table(rows, cols):
    out=['<div class="table-scroll"><table><thead><tr>']+[f'<th>{esc(label)}</th>' for _,label in cols]+['</tr></thead><tbody>']
    for r in rows:
        out.append('<tr>');out += [f'<td>{esc(r.get(key,''))}</td>' for key,_ in cols];out.append('</tr>')
    out += ['</tbody></table></div>'];return '\n'.join(out)
methods=read('methods.csv')
method_cols=[('method_name','Method'),('method_category','Category'),('input_type','Input'),('main_strength','Main strength'),('main_limitation','Main limitation'),('best_use','Best use'),('unsupported_or_weak_claim','Do not infer'),('evidence_status','Evidence'),('review_section','Review section')]
text='# Computational methods matrix\n\nThis matrix supports the review but is not a general catalogue. It emphasizes method fit, evidentiary limits, and human-virome interpretation.\n\nHave a tool to suggest? [Submit a proposal for maintainer review](https://github.com/virome-hub/human-virome-methods-hub/issues/new?template=add-method.yml).\n\n'+table(methods,method_cols)+'\n'
(ROOT/'docs/methods.md').write_text(text,encoding='utf-8')
strategies=read('strategies.csv')
strategy_cols=[('strategy','Strategy'),('principal_fraction_measured','Principal fraction measured'),('strengths','Strengths'),('major_limitations_and_blind_spots','Blind spots'),('best_suited_applications','Best-suited applications')]
text='# Sequencing strategy matrix\n\nThis is the living-resource version of manuscript Table 1.\n\n'+table(strategies,strategy_cols)+'\n'
(ROOT/'docs/strategies.md').write_text(text,encoding='utf-8')
print(f'Built {len(methods)} method rows and {len(strategies)} strategy rows.')
