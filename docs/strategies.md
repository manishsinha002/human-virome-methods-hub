# Sequencing strategies

Sequencing strategy determines which viral fractions are observable and how well samples support detection, genome recovery, and interpretation. Compare the trade-offs below in the context of your specimen and research question. On narrower screens, scroll the table horizontally to see every column.

<div class="strategies-table">

<table><thead><tr>
<th>Strategy</th>
<th>Principal fraction measured</th>
<th>Strengths</th>
<th>Blind spots</th>
<th>Best-suited applications</th>
</tr></thead><tbody>
<tr>
<td>Total DNA metagenomics</td>
<td>DNA viruses, intracellular viral DNA, replicative DNA intermediates, prophages and integrated viral elements, together with microbial and host DNA</td>
<td>Preserves broader community context; supports detection of intracellular and integrated viral sequences; requires no prior viral target selection</td>
<td>Host and microbial DNA can overwhelm low-abundance viral signals; limited recovery of rare extracellular viruses; does not detect RNA-virus genomes directly</td>
<td>Community-level profiling, prophage analysis, integrated viral elements and agnostic DNA-virus discovery</td>
</tr>
<tr>
<td>VLP-enriched DNA sequencing</td>
<td>Predominantly extracellular, encapsidated and nuclease-protected DNA viruses</td>
<td>Increases the proportion of viral reads; improves detection of low-abundance viruses and assembly of viral genomes</td>
<td>May exclude intracellular and integrated viruses; filtration can remove large or particle-associated viruses; chemical or enzymatic treatments may reduce recovery of enveloped, damaged or unprotected viruses; enrichment can distort relative abundance</td>
<td>Extracellular virome profiling, bacteriophage discovery and recovery of viral metagenome-assembled genomes</td>
</tr>
<tr>
<td>Total metatranscriptomics</td>
<td>RNA-virus genomes and transcripts produced by RNA and DNA viruses, together with transcriptionally active microorganisms and host RNA</td>
<td>Detects RNA viruses; provides evidence of viral transcription; enables simultaneous assessment of microbial activity and host response</td>
<td>Dominated by host and ribosomal RNA; sensitive to RNA degradation; affected by depletion and reverse-transcription biases; RNA detection does not necessarily establish active replication</td>
<td>RNA virome profiling, respiratory and mucosal viromes, transcriptional activity and virus-microbiome-host interactions</td>
</tr>
<tr>
<td>Capture-enriched sequencing</td>
<td>Viral DNA or RNA sufficiently related to sequences represented in the probe set</td>
<td>Improves analytical sensitivity, viral read depth and genome coverage in host-rich or low-viral-biomass specimens</td>
<td>Requires prior sequence information; may miss highly divergent or unrepresented viruses; probe mismatches can produce uneven coverage; abundance estimates may be distorted by differential capture efficiency</td>
<td>Sensitive detection, confirmation, surveillance and genome recovery for known or genetically related viruses</td>
</tr>
<tr>
<td>Short-read sequencing</td>
<td>Short fragments of viral DNA or complementary DNA retained by the selected extraction and library workflow</td>
<td>High base-level accuracy, depth, throughput and scalability; supports sensitive detection, variant calling and reference-guided reconstruction</td>
<td>Can produce fragmented assemblies; limited resolution of repeats, integration junctions, haplotypes and mixed or microdiverse viral populations</td>
<td>High-throughput detection, population studies, reference-guided genome recovery and sequence-variant analysis</td>
</tr>
<tr>
<td>Long-read sequencing</td>
<td>Long viral molecules, complete genomic segments, transcripts, structural variants and integration junctions</td>
<td>Improves de novo assembly, genome continuity, haplotype and strain resolution, structural-variant detection and real-time analysis</td>
<td>May require more input material; lower effective depth for rare viruses; platform-specific error profiles; accuracy, cost and computational requirements vary by platform and workflow</td>
<td>Complete-genome reconstruction, mixed infections, haplotype analysis, structural variation and viral integration</td>
</tr>
<tr>
<td>Hybrid short- and long-read sequencing</td>
<td>Viral genomes represented by complementary short- and long-read data</td>
<td>Combines short-read depth and accuracy with long-range genomic continuity; improves genome completeness, error correction and strain resolution</td>
<td>Requires parallel library preparation and sequencing; increases cost, workflow complexity and computational demands</td>
<td>Reference-quality genome reconstruction, strain-resolved analysis and complex or highly microdiverse viral populations</td>
</tr>
</tbody></table>

</div>
