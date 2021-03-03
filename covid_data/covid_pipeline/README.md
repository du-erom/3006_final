# Schemas
Documentation of the pandas dataframe schemas

## New York Times Data
Source: us-counties.csv

|index|Column|Non-Null|Type|Description|
|---|---|---|---|---|
|0|date|Yes|object|YYYY-MM-DD|
|1|county|Yes|object|County Name|
|2|state|Yes|object|Full State Name|
|3|fips|Yes|float64|FIPS value|
|4|cases|Yes|int64|Number of cases for day|
|5|deaths|Yes|float64|Number of deaths for day|

## Census Delineation Data
Source: census_cbsa.csv

|index|Column|Non-Null|Type|
|---|---|---|---|
|0|CBSA Code|Yes|int64|
|1|Metropolitian Division Code|Yes|float64|
|2|CSA Code|Yes|float64|
|3|CBSA Title|Yes|object|
|4|Metropolitan/Micropolitan Statistical Area|Yes|object|
|5|Metropolitan Division Title|Yes|object|
|6|CSA Title|Yes|object|
|7|County/County Equivalent|Yes|objct|
|8|State Name|Yes|object|
|9|FIPS State Code|Yes|int64|
|10|FIPS County Code|Yes|int64|
|11|Central/Outlying County|Yes|object|

## Census Population Data
Source: census_population_only_estimates_2019.csv

|index|Column|Non-Null|Type|Description|
|---|---|---|---|---|
|0|SUMLEV|Yes|int64|Geographic summary level|
|1|REGION|Yes|int64|Census Region code|
|2|DIVISION|Yes|int64|Census Division code|
|3|STATE|Yes|int64|State FIPS code|
|4|COUNTY|Yes|int64|County FIPS code|
|5|STNAME|Yes|int64|State name|
|6|CTYNAME|Yes|object|County name|
|7|POPESTIMATE2019|Yes|int64|7/1/2019 resident total population estimate|

## Group by Fips
|index|Column|Non-Null|Type|Description|
|---|---|---|---|---|
|0|date|Yes|object|YYYY-MM-DD|
|1|cases,sum|Yes|int64|sum of counts
|4|min_new_cases|Yes|int64|Min Number of new cases across the fips code for that day|
|5|max_new_cases|Yes|int64|Max Number of new cases across the fips code for that day|
|6|mean_new_cases|Yes|float64|Mean number of new cases across the fips code for that day|
|7|sum_new_cases|Yes|int64|Sum of  new cases across the fips code for that day|
|8|min_new_deaths|Yes|int64|Min Number of new deaths across the fips code for that day|
|9|max_new_deaths|Yes|int64|Max Number of new deaths across the fips code for that day|
|10|mean_new_deaths|Yes|float64|Mean number of new deaths across the fips code for that day|
|11|sum_new_deaths|Yes|int64|Sum of new deaths across the fips code for that day|
