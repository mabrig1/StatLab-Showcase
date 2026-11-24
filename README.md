# MABRIG StatLab | Scientific Software Engineering Portfolio

**Statistical computing · Research analytics · Reproducible methods**

StatLab is an independent research statistics prototype, not IBM SPSS or a complete replacement. Its documented architecture separates a local Python/FastAPI workstation from a static browser edition; advanced local methods are not represented as browser capabilities.

## Explore the portfolio

- [Conceptual architecture](docs/architecture.md)
- [Engineering case study](docs/case-study.md)
- [Interactive frequency calculator](demo/index.html) — download and open locally.
- [Independent Python statistical example](demo/frequencies.py)
- [Automated tests](demo/test_frequencies.py)
- [CI workflow](.github/workflows/demo.yml)

## Reproduce the example

```sh
python demo/frequencies.py
python -m unittest discover -s demo -v
```

Python 3.10+; no dependencies or API keys. Synthetic five-point counts demonstrate weighted mean, percentages and population/sample standard deviations with explicit denominators. Numeric scores are treated as equally spaced. Aggregate counts cannot establish respondent-level relationships. This example does not validate the full production engine or advanced statistical methods.

## Engineering competencies

Numerical computation, research data validation, reproducibility, methodological transparency, data visualization and automated testing.

## Intellectual property and technical review

See [NOTICE.md](NOTICE.md). The examples are independently authored, with no production implementation or confidential datasets copied. Contact [MABRIG Technologies](https://www.mabrigkorie.org) for a guided demonstration or scoped technical discussion. [Developer profile](https://github.com/mabrig1).
