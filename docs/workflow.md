# Human virome workflow

Human virome analysis is not one universal pipeline. Specimen biology, laboratory choices, reference databases, and computational thresholds all shape the virome that is observed. Use this map to explore the major decisions and complementary analysis routes—not as a one-size-fits-all protocol.

<div class="workflow-intro">
  <strong>How to explore</strong>
  <span>Select any stage or substep. The detail panel explains its purpose, outputs, caveats, and tools or references connected to the repository's curated methods data.</span>
</div>

<div class="workflow-app" data-workflow>
  <p class="workflow-load-error" data-workflow-status role="status" hidden></p>
  <div class="workflow-layout">
    <nav class="workflow-map" aria-label="Interactive human virome workflow">
      <div class="workflow-section-label">Study design and sample processing</div>
      <div class="workflow-sequence">
        <button class="workflow-node is-active" type="button" data-workflow-node="design" aria-pressed="true">
          <span class="workflow-node-number">01</span>
          <span class="workflow-node-title">Question, specimen and controls</span>
          <span class="workflow-node-subtitle">Define what can be observed</span>
        </button>
        <span class="workflow-connector" aria-hidden="true">→</span>
        <button class="workflow-node" type="button" data-workflow-node="sample-prep" aria-pressed="false">
          <span class="workflow-node-number">02</span>
          <span class="workflow-node-title">Recovery and sequencing strategy</span>
          <span class="workflow-node-subtitle">Choose fractions and library approach</span>
        </button>
        <span class="workflow-connector" aria-hidden="true">→</span>
        <button class="workflow-node" type="button" data-workflow-node="read-qc" aria-pressed="false">
          <span class="workflow-node-number">03</span>
          <span class="workflow-node-title">Read quality control</span>
          <span class="workflow-node-subtitle">Inspect, trim and retain provenance</span>
        </button>
        <span class="workflow-connector" aria-hidden="true">→</span>
        <button class="workflow-node" type="button" data-workflow-node="host-removal" aria-pressed="false">
          <span class="workflow-node-number">04</span>
          <span class="workflow-node-title">Human-read removal</span>
          <span class="workflow-node-subtitle">Balance privacy, sensitivity and retention</span>
        </button>
      </div>

      <div class="workflow-section-label">Analyze reads and/or assemble sequences</div>
      <div class="workflow-branches">
        <section class="workflow-lane workflow-lane-read" aria-labelledby="read-route-title">
          <h2 id="read-route-title">Read-based route</h2>
          <p>Fast screening of reference-represented viruses; can detect signals too sparse to assemble.</p>
          <div class="workflow-lane-nodes">
            <button class="workflow-node" type="button" data-workflow-node="read-kmer" aria-pressed="false">
              <span class="workflow-node-title">K-mer and profile-based screening</span>
              <span class="workflow-node-subtitle">Classify reads against a versioned database</span>
            </button>
            <button class="workflow-node" type="button" data-workflow-node="read-mapping" aria-pressed="false">
              <span class="workflow-node-title">Reference mapping and recruitment</span>
              <span class="workflow-node-subtitle">Evaluate identity, breadth and depth</span>
            </button>
            <button class="workflow-node" type="button" data-workflow-node="read-abundance" aria-pressed="false">
              <span class="workflow-node-title">Abundance and comparison</span>
              <span class="workflow-node-subtitle">Normalize and compare with controls</span>
            </button>
          </div>
        </section>

        <section class="workflow-lane workflow-lane-assembly" aria-labelledby="assembly-route-title">
          <h2 id="assembly-route-title">Assembly-based route</h2>
          <p>Reconstruct contigs for candidate discovery, genome-level comparison and downstream interpretation.</p>
          <div class="workflow-lane-nodes">
            <button class="workflow-node" type="button" data-workflow-node="assembly" aria-pressed="false">
              <span class="workflow-node-title">De novo assembly</span>
              <span class="workflow-node-subtitle">Build contigs from reads</span>
            </button>
            <button class="workflow-node" type="button" data-workflow-node="viral-identification" aria-pressed="false">
              <span class="workflow-node-title">Viral-sequence identification</span>
              <span class="workflow-node-subtitle">Homology, markers, composition and ML</span>
            </button>
            <button class="workflow-node" type="button" data-workflow-node="genome-quality" aria-pressed="false">
              <span class="workflow-node-title">Genome quality and similarity</span>
              <span class="workflow-node-subtitle">Completeness, boundaries, clustering and ANI</span>
            </button>
          </div>
        </section>
      </div>

      <div class="workflow-merge" aria-hidden="true"><span>Evidence from both routes informs candidate review</span></div>
      <div class="workflow-section-label">Interpret, validate and report</div>
      <div class="workflow-sequence workflow-sequence-downstream">
        <button class="workflow-node" type="button" data-workflow-node="taxonomy" aria-pressed="false">
          <span class="workflow-node-number">05</span>
          <span class="workflow-node-title">Taxonomy and genome context</span>
          <span class="workflow-node-subtitle">Compare sequence and genome evidence</span>
        </button>
        <span class="workflow-connector" aria-hidden="true">→</span>
        <button class="workflow-node" type="button" data-workflow-node="host-function" aria-pressed="false">
          <span class="workflow-node-number">06</span>
          <span class="workflow-node-title">Host and functional hypotheses</span>
          <span class="workflow-node-subtitle">Predict cautiously; validate key claims</span>
        </button>
        <span class="workflow-connector" aria-hidden="true">→</span>
        <button class="workflow-node" type="button" data-workflow-node="validation-reporting" aria-pressed="false">
          <span class="workflow-node-number">07</span>
          <span class="workflow-node-title">Validation and reporting</span>
          <span class="workflow-node-subtitle">Make evidence and uncertainty reproducible</span>
        </button>
      </div>
    </nav>

    <aside class="workflow-details" id="workflow-details" aria-live="polite" aria-labelledby="workflow-detail-title">
      <span class="workflow-detail-kicker">Selected workflow step</span>
      <h2 id="workflow-detail-title">Question, specimen and controls</h2>
      <p id="workflow-detail-summary">Start with the biological question and specimen. These choices constrain which viral fractions can be recovered and what a negative result can mean.</p>
      <div class="workflow-detail-block">
        <h3>Why it matters</h3>
        <p id="workflow-detail-rationale">The observed virome reflects both biology and technical selection across collection, enrichment, extraction and sequencing.</p>
      </div>
      <div class="workflow-detail-block">
        <h3>Key outputs or decisions</h3>
        <p id="workflow-detail-output">A defined target, specimen context, controls and sequencing strategy.</p>
      </div>
      <div class="workflow-detail-block workflow-caution">
        <h3>Interpretation check</h3>
        <p id="workflow-detail-caveat">A method-negative result does not establish biological absence when the target fraction may not have been recovered or the assay lacks sensitivity.</p>
      </div>
      <div class="workflow-detail-block" id="workflow-tools-block" hidden>
        <h3>Methods in this hub</h3>
        <ul id="workflow-tool-list"></ul>
      </div>
      <div class="workflow-detail-block" id="workflow-links-block" hidden>
        <h3>Related resources</h3>
        <ul id="workflow-link-list"></ul>
      </div>
      <div class="workflow-detail-block" id="workflow-citations-block" hidden>
        <h3>Evidence and references</h3>
        <ul id="workflow-citation-list"></ul>
      </div>
    </aside>
  </div>
</div>

<noscript>
  <p>This workflow map needs JavaScript to update the detail panel. The complete tools catalogue and evidence context are also available on the <a href="../methods/">computational methods</a>, <a href="../strategies/">sequencing strategies</a>, and <a href="../evidence-standards/">evidence standards</a> pages.</p>
</noscript>

!!! info "A map, not a mandatory pipeline"
    Read-based screening and assembly-based discovery answer different questions and can be run in parallel. Average nucleotide identity (ANI) is a genome/contig comparison concept, not a read-classification method. Choose stages and thresholds for the study question, viral group, specimen, and available evidence.

## Evidence sources and scope

This map is organized around topics in the project's current review draft and the tools already curated in this hub. The section numbers shown in the detail panel are internal references to an unpublished draft, not stand-alone citations; treat its wording and recommendations as provisional until finalized and reviewed. Follow the linked method papers and documentation for tool-specific evidence. Links to the broader [Awesome-Virome catalogue](https://github.com/shandley/awesome-virome) are discovery resources, not endorsements or evidence that a tool has been validated for human viromics.
