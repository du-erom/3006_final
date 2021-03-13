# 3006_final
Repository for a group project looking at the correlation between covid prevalence and housing prices

## Participants
Eric Romberg (Housing Data)

Ben Hersh (Covid Data)

## Hypothesis
This project is looking for correlations between housing price changes and covid incidence rates in US Metropolitan areas.
Based on news reports and anecdotal stories of people moving out from urban areas seemed to be widespread. We hypothesize that based on this reported movement we should see some correlation between the incidence of covid and housing prices. This
correlation is hypothesized to be negative due to homeowners selling to move away (i.e, a seller’s market)

## Data
This project uses 3 sources of information
1. FHA Housing Price Index data (fha.gov)
2. Covid Case data (New York Times)
3. Census Population Estimates (census.gov)

## Prerequisites
Use the requirements.txt to install all the required libraries.

## Housing Data
The independent housing data is presented in the Housing report.ipynb notebook.

## Covid Data
The independent covid data is presented in the covid_data/covid_pipeline/covid_plots.ipynb notebook.

## Combined Data
The combined data is presented in the combined_plots/Combined_plots.ipynb.

Covid data is prepared for correlation to the Housing data in the combined_plots/prepare_covid.ipynb . The covid data 
was scaled by the population estimates for each locale. This processed is saved in this report in the 
combined_plots/metro_year_over_year_change_2020_with_covid.csv


# Conclusions
There is no strong evidence for a correlation between the rate of covid incidence and housing prices in the 
Metropolitan areas captured in this study.

## Making it better
1. Look at the housing data at a finer time resolution.
2. Look at the housing data from non-urban areas.