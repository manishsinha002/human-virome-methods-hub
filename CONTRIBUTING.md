# Contributing

## Principles
1. Every recommendation must be linked to evidence.
2. Tool-author conflicts should be disclosed.
3. Distinguish tool availability from independent validation.
4. Record software, database, and benchmark versions.
5. Use cautious language for claims not supported by independent benchmarks.

## Contribution routes
- **Correction:** open an issue with the affected record and supporting reference.
- **New method or tool:** [submit a proposal](https://github.com/virome-hub/human-virome-methods-hub/issues/new?template=add-method.yml) for maintainer review.
- **Data update:** edit the relevant CSV and open a pull request.

## Tool proposal review
Submitting a proposal creates a GitHub issue for the maintainers; it does not change the website directly. Maintainers review its relevance and evidence and may ask questions or decline it. If accepted, a maintainer updates the structured data in a pull request. The pull request must pass schema validation, and merging it to `main` triggers the website build and deployment. GitHub sends issue notifications according to each maintainer's repository notification settings.

All pull requests must pass schema validation before review.
