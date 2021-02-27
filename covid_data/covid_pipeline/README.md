# Schemas
Documentation of the pandas dataframe schemas

## New York Times Data

|index|Column|Non-Null|Type|Description|
|---|---|---|---|---|
|0|date|Yes|object|YYYY-MM-DD|
|1|county|Yes|object|County Name|
|2|state|Yes|object|Full State Name|
|3|fips|Yes|float64|FIPS value|
|4|cases|Yes|int64|Number of cases for day|
|5|deaths|Yes|float64|Number of deaths for day|

## Census Delineation Data

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
