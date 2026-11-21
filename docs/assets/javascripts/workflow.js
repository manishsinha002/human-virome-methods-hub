(() => {
  const scriptUrl = document.currentScript?.src;
  const root = document.querySelector("[data-workflow]");
  if (!root) return;

  const status = root.querySelector("[data-workflow-status]");
  const buttons = [...root.querySelectorAll("[data-workflow-node]")];
  let workflowNodes = new Map();
  const detail = {
    title: root.querySelector("#workflow-detail-title"),
    summary: root.querySelector("#workflow-detail-summary"),
    rationale: root.querySelector("#workflow-detail-rationale"),
    output: root.querySelector("#workflow-detail-output"),
    caveat: root.querySelector("#workflow-detail-caveat"),
    toolsBlock: root.querySelector("#workflow-tools-block"),
    tools: root.querySelector("#workflow-tool-list"),
    linksBlock: root.querySelector("#workflow-links-block"),
    links: root.querySelector("#workflow-link-list"),
    citationsBlock: root.querySelector("#workflow-citations-block"),
    citations: root.querySelector("#workflow-citation-list"),
  };

  function showError(error) {
    console.error("Could not load workflow details.", error);
    status.textContent = "Workflow details could not be loaded. Please use the linked methods and guidance pages below, or try reloading.";
    status.hidden = false;
  }

  function makeLink(label, href) {
    const url = new URL(href, document.baseURI);
    if (!["http:", "https:"].includes(url.protocol)) {
      throw new Error(`Unsupported workflow link protocol: ${url.protocol}`);
    }

    const link = document.createElement("a");
    link.href = url.href;
    link.textContent = label;
    if (url.origin !== window.location.origin) {
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    }
    return link;
  }

  function fillList(block, list, items, renderItem) {
    list.replaceChildren();
    for (const item of items) {
      const entry = document.createElement("li");
      renderItem(entry, item);
      list.append(entry);
    }
    block.hidden = items.length === 0;
  }

  function renderMethod(entry, method) {
    const methodLink = makeLink(method.method_name, method.software_url);
    entry.append(methodLink);

    const description = document.createElement("p");
    description.textContent = `${method.best_use} Evidence: ${method.evidence_status}.`;
    entry.append(description);

    const limitation = document.createElement("p");
    limitation.textContent = `Limitation: ${method.main_limitation} Do not infer: ${method.unsupported_or_weak_claim}.`;
    entry.append(limitation);
  }

  function renderResource(entry, resource) {
    entry.append(makeLink(resource.label, resource.url));
  }

  function renderCitation(entry, reference) {
    const label = `${reference.title}${reference.year ? ` (${reference.year})` : ""}`;
    let href = reference.doi ? `https://doi.org/${reference.doi}` : "";
    if (!href && reference.pmid) href = `https://pubmed.ncbi.nlm.nih.gov/${reference.pmid}/`;

    if (href) {
      entry.append(makeLink(label, href));
    } else {
      entry.append(document.createTextNode(label));
    }
    if (reference.review_status) {
      const statusText = document.createElement("span");
      statusText.textContent = ` — ${reference.review_status}`;
      entry.append(statusText);
    }
  }

  function selectNode(node) {
    for (const button of buttons) {
      const selected = button.dataset.workflowNode === node.id;
      button.classList.toggle("is-active", selected);
      button.setAttribute("aria-pressed", String(selected));
    }

    detail.title.textContent = node.label;
    detail.summary.textContent = node.summary;
    detail.rationale.textContent = node.why_it_matters;
    detail.output.textContent = node.outputs;
    detail.caveat.textContent = node.caveat;

    fillList(detail.toolsBlock, detail.tools, node.methods, renderMethod);
    fillList(detail.linksBlock, detail.links, node.links, renderResource);

    const references = new Map();
    for (const method of node.methods) {
      for (const reference of method.references) {
        references.set(reference.reference_id, reference);
      }
    }
    const citations = [...references.values()];
    if (node.review_sections.length) {
      citations.unshift({
        reference_id: "review-context",
        title: `Review-draft context: sections ${node.review_sections.join(", ")}`,
      });
    }
    fillList(detail.citationsBlock, detail.citations, citations, renderCitation);
  }

  for (const button of buttons) {
    button.addEventListener("click", () => {
      const node = workflowNodes.get(button.dataset.workflowNode);
      if (node) selectNode(node);
    });
  }

  async function loadWorkflow() {
    try {
      if (!scriptUrl) throw new Error("Workflow script URL is unavailable.");
      const response = await fetch(new URL("../data/workflow.json", scriptUrl));
      if (!response.ok) throw new Error(`Workflow data request failed (${response.status}).`);

      const data = await response.json();
      if (!Array.isArray(data.nodes)) throw new Error("Workflow data does not contain a nodes list.");

      workflowNodes = new Map(data.nodes.map((node) => [node.id, node]));
      const initialNode = workflowNodes.get(buttons[0]?.dataset.workflowNode);
      if (!initialNode) throw new Error("The initial workflow stage is missing from the workflow data.");

      for (const button of buttons) {
        if (!workflowNodes.has(button.dataset.workflowNode)) {
          throw new Error(`Workflow data is missing stage "${button.dataset.workflowNode}".`);
        }
      }
      selectNode(initialNode);
    } catch (error) {
      showError(error);
    }
  }

  loadWorkflow();
})();
