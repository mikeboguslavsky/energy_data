The code in this repo requires the pandasdmx library (for querying the U.N. Energy Statistics Database), as well as pandas and seaborn.

Utility functions are defined in utils.py.

The notebook analysis.ipynb imports the functions, loads U.N. energy data, and operates on the dataframes.

The answers to questions #1 and #2 are presented in the notebook.

For question #3, my questions about the dataset are:

(1) My results for electricity production by source are generally in line with published sources (for example https://www.iea.org/data-and-statistics/charts/world-gross-electricity-production-by-source-2019), except the share of natural gas is 3.5% lower. I'm curious why this is.

(2) Electricity production from combustible fuels should match between the U.N. Energy Statistics and the Energy Balances databases, but they don't seem to. I wonder if my energy unit conversion was not correct, and/or there is some non-obvious energy accounting involved in the conversion of fuel to electricity.
