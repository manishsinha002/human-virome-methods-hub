# Computational methods matrix

This matrix supports the review but is not a general catalogue. It emphasizes method fit, evidentiary limits, and human-virome interpretation.

<div class="table-scroll"><table><thead><tr>
<th>Method</th>
<th>Category</th>
<th>Input</th>
<th>Main strength</th>
<th>Main limitation</th>
<th>Best use</th>
<th>Do not infer</th>
<th>Evidence</th>
<th>Review section</th>
</tr></thead><tbody>
<tr>
<td>Seal (BBTools)</td>
<td>Host-read removal</td>
<td>Quality-controlled reads</td>
<td>Fast k-mer-based binning</td>
<td>Performance depends on reference composition and parameterization; less independently benchmarked in viromics than major aligners</td>
<td>Rapid host-read screening and binning</td>
<td>Proof that retained reads are non-human or that removed reads are exclusively host-derived</td>
<td>Tool documentation plus review discussion</td>
<td>3.a</td>
</tr>
<tr>
<td>Bowtie2</td>
<td>Host-read removal</td>
<td>Quality-controlled reads</td>
<td>High precision and configurable sensitivity</td>
<td>High-sensitivity modes increase runtime; reference and pairing choices affect removal</td>
<td>Sensitive short-read host depletion</td>
<td>Guaranteed privacy or complete preservation of virus-like host sequences</td>
<td>Multiple independent benchmarks</td>
<td>3.a</td>
</tr>
<tr>
<td>Minimap2</td>
<td>Host-read removal</td>
<td>Reads</td>
<td>Fast alignment across read lengths</td>
<td>Sensitivity depends on preset and reference; host-like viral sequence may be removed</td>
<td>Fast host depletion, including long reads</td>
<td>Complete removal of identifiable human sequence without residual-risk assessment</td>
<td>Used within Hostile; independent context-specific benchmarking needed</td>
<td>3.a</td>
</tr>
<tr>
<td>Hostile</td>
<td>Host-read removal</td>
<td>Reads</td>
<td>High host-read removal with strong microbial-read retention</td>
<td>Still depends on reference masking and cannot preserve every host-like viral signal</td>
<td>Laptop-scale host decontamination</td>
<td>Detection of endogenous viral elements after strict host removal</td>
<td>Primary benchmark with comparisons</td>
<td>3.a</td>
</tr>
<tr>
<td>SRA Human Scrubber (HRRT)</td>
<td>Host-read removal</td>
<td>Reads</td>
<td>Operationally aligned with SRA public-deposition screening</td>
<td>Not optimized to retain every microbial or host-like viral read</td>
<td>Submission-oriented privacy screening</td>
<td>Biologically neutral host depletion</td>
<td>Benchmarked against alternative host-removal methods</td>
<td>3.a</td>
</tr>
<tr>
<td>nf-core/detaxizer</td>
<td>Host-read removal</td>
<td>Reads</td>
<td>Containerized, reproducible taxon-removal workflow</td>
<td>Recall and false-positive balance depends strongly on database and chained passes</td>
<td>Standardized, auditable decontamination</td>
<td>Universally optimal host removal</td>
<td>Primary benchmarking study</td>
<td>3.a</td>
</tr>
<tr>
<td>Phanta</td>
<td>Read-based profiling</td>
<td>Quality-controlled reads</td>
<td>Coverage-aware profiling improves specificity over raw read counts</td>
<td>Cannot discover viruses absent from the reference; database composition controls labels</td>
<td>Rapid profiling of known/reference-represented viruses</td>
<td>Confirmation of a novel virus or complete genome recovery</td>
<td>Primary method paper; human-gut evaluation</td>
<td>3.b</td>
</tr>
<tr>
<td>Kraken2</td>
<td>Read-based classification</td>
<td>Reads or contigs</td>
<td>Very fast and scalable</td>
<td>Closely related taxa and database contamination can generate false positives; raw counts do not establish genome coverage</td>
<td>Rapid screening and exploratory profiling</td>
<td>Species confirmation from a few reads</td>
<td>Extensively benchmarked generally; human-virome-specific calibration limited</td>
<td>3.b;3.d</td>
</tr>
<tr>
<td>metaSPAdes</td>
<td>Metagenomic assembly</td>
<td>Quality-controlled reads</td>
<td>Widely used de novo assembler for complex communities</td>
<td>Microdiversity, repeats and uneven coverage fragment or collapse viral genomes</td>
<td>General short-read metagenome assembly before viral calling</td>
<td>Proof that a contig is viral or non-chimeric</td>
<td>Primary assembler paper; extensive use</td>
<td>3.b;3.c</td>
</tr>
<tr>
<td>MEGAHIT</td>
<td>Metagenomic assembly</td>
<td>Quality-controlled reads</td>
<td>Fast and memory-efficient for large datasets</td>
<td>Does not eliminate fragmentation, collapse or chimeric assembly risks</td>
<td>Large short-read metagenomic cohorts</td>
<td>Independent confirmation of viral origin</td>
<td>Primary method paper; widely used</td>
<td>3.b;3.c</td>
</tr>
<tr>
<td>geNomad</td>
<td>Viral identification</td>
<td>Assembled contigs or genomes</td>
<td>Integrated marker, gene-content and neural-network evidence</td>
<td>Short or atypical elements may lack decisive features; taxonomy is often above species level</td>
<td>General viral contig and provirus identification</td>
<td>Experimental function, infectivity or artifact-free assembly</td>
<td>Primary benchmark and broad evaluations</td>
<td>3.b;3.d;3.g</td>
</tr>
<tr>
<td>VirSorter2</td>
<td>Viral identification</td>
<td>Assembled contigs</td>
<td>Multi-classifier framework across diverse viral groups</td>
<td>False positives increase without post-filtering; performance varies by group and contig length</td>
<td>Sensitive candidate discovery followed by quality control</td>
<td>Automatic confirmation that every score-positive contig is viral</td>
<td>Primary benchmark; independent comparisons available</td>
<td>3.d;3.g</td>
</tr>
<tr>
<td>VIBRANT</td>
<td>Viral identification and annotation</td>
<td>Assembled contigs</td>
<td>Combines viral identification with protein annotation</td>
<td>Database and training representation affect sensitivity; functional calls remain putative</td>
<td>Phage/provirus recovery with preliminary annotation</td>
<td>Validated biological function or infectivity</td>
<td>Primary method paper; independent comparisons available</td>
<td>3.d;3.g</td>
</tr>
<tr>
<td>DeepVirFinder</td>
<td>Sequence-composition ML</td>
<td>Contigs</td>
<td>Alignment-free detection of divergent and shorter sequences</td>
<td>Probabilistic score is sensitive to training data, length and atypical cellular sequences</td>
<td>Prioritizing divergent candidates for multi-evidence review</td>
<td>Standalone confirmation of a novel virus</td>
<td>Primary method paper; independent comparisons available</td>
<td>3.d;3.e</td>
</tr>
<tr>
<td>CheckV</td>
<td>Viral genome quality</td>
<td>Predicted viral contigs</td>
<td>Standardized estimates and host-boundary support</td>
<td>Novel groups may receive uncertain completeness estimates; not a viral detector</td>
<td>Post-identification genome quality and provirus assessment</td>
<td>Proof of infectivity or taxonomic identity</td>
<td>Primary method paper; widely adopted</td>
<td>3.b;3.c;3.h</td>
</tr>
<tr>
<td>Vclust</td>
<td>Viral genome clustering</td>
<td>Viral contigs/genomes</td>
<td>Fast large-scale ANI and clustering</td>
<td>Cluster quality depends on input completeness, alignment coverage and thresholds</td>
<td>vOTU dereplication and within/across-study clustering</td>
<td>Formal taxonomy or biological equivalence without supporting evidence</td>
<td>Primary method/tool evidence</td>
<td>3.h</td>
</tr>
<tr>
<td>iPHoP</td>
<td>Virus-host prediction</td>
<td>Viral genomes/contigs plus host references</td>
<td>Integrates multiple host-prediction signals</td>
<td>Accuracy and taxonomic resolution vary; database coverage limits hosts</td>
<td>Prioritized bacteriophage-host hypotheses</td>
<td>Confirmed infection, productive replication or strain-level host without validation</td>
<td>Primary benchmark; external testing desirable</td>
<td>3.h;5.d</td>
</tr>
<tr>
<td>Foldseek</td>
<td>Structure similarity search</td>
<td>Predicted or experimental protein structures; optionally sequences</td>
<td>Sensitive remote-homology search beyond sequence similarity</td>
<td>A structural match does not prove exact function, viral origin or contig authenticity</td>
<td>Hypothesis generation for viral protein dark matter</td>
<td>Experimentally validated function from structure alone</td>
<td>Primary method paper; broad structural benchmarking</td>
<td>3.f;5.e</td>
</tr>
<tr>
<td>AlphaFold</td>
<td>Protein structure prediction</td>
<td>Protein sequences</td>
<td>Provides structural hypotheses for proteins lacking homologs</td>
<td>pLDDT measures local structural confidence, not functional correctness; disordered regions may remain unresolved</td>
<td>Supporting structure-informed annotation</td>
<td>Validated function, viral origin or biological activity</td>
<td>Extensively benchmarked structurally; viral function requires additional evidence</td>
<td>3.f;5.e</td>
</tr>
<tr>
<td>Pharokka</td>
<td>Phage genome annotation</td>
<td>Phage genomes/contigs</td>
<td>Rapid standardized phage annotation</td>
<td>Unknown proteins remain hypothetical; annotations inherit database errors</td>
<td>Initial annotation of phage genomes</td>
<td>Experimental confirmation of gene function</td>
<td>Primary method paper; independent benchmarking limited</td>
<td>3.h;5.e</td>
</tr>
</tbody></table></div>
