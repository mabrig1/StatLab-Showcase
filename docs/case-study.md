# Engineering case study: StatLab

## Problem
Survey researchers need reproducible calculations, explicit assumptions and understandable output without disclosing confidential data.

## Approach
Separate aggregate frequency inputs from respondent-level analysis, validate input and report the denominator used in variance calculations. The original documentation describes separate browser and local Python editions, including exploratory factor analysis and power analysis in the latter. This showcase does not establish independent validation of those advanced methods.

## Demonstration
The independent frequency summary uses synthetic data and calculates weighted mean, population and sample standard deviation. Aggregated counts do not reconstruct respondent-level relationships. No production engine or private dataset is included.

## Interview topics
Numerical correctness, methodological limits, testing, data privacy and reproducibility.
