# Requirements

<!-- markdownlint-disable MD013 --><!-- Tables cannot be split up over lines, hence will break 80 characters per line -->

Requirement ID|Requirement description                                             | Risk description     | Risk severity  | Risk probability | Mitigation strategy 
--------------|--------------------------------------------------------------------|-------------------------------------------------------|-------|-----|---------------------------------------------------------------------------------
R1            |Reading the data file follows best practices                        | | | |
R1.1          |The data file can be read                                           | No file or corrupted | S4 | P4 | Check if file exists, check data integrity, error message if not
R1.2          |Reading the data file produces a table                              | Wrong file format/type | S4 | P4 | Check file extesion, check file format, number of columns, data types in columns
R1.2          |The table produced from reading the data has correct column names   | |  |  | 
R1.3          |The table produced from reading the data has the correct content    |  |  |  | 
R1.4          |Read data file is read in a short time                              | File taking to long time to load | S2 | P3 | Limit on the number of rows in the input file
R1.5          |Reading an absent file gives an error                               | see R1.1  | |  | 
R1.6          |Table column names are documented                                   | |  |  |
R2            |Can work with `datetime` strings                                    | | | |
R2.1          |The function `is_datetime` detects a `datetime` correctly           | Returns TRUE if not `datetime`/Returns FALSE if `datetime` | S4 | P4 | Explicitly, a lot of tests 
R2.1.1        |`is_datetime` works on a string                                     | see R2.1 | | |
R2.1.2        |`is_datetime` works on a string of the correct length               | see R2.1 | | |
R2.1.3        |A `datetime` string has a valid year                                | Out of range, keep track of current year | S3 | P3 | Specify the input range at the start
R2.1.4        |A `datetime` string has a dash between year and month               | No dashes, weird format of the datetie | S3 | P3 | Rewrite the requirements to check for is String and then for format
R2.1.5        |A `datetime` string has a valid month                               | Month is not an int | S3 | P3 | Rewrite the requirements to check for is Int and then if is in Range(1,12)
R2.1.6        |A `datetime` string has a dash between month and day                | see R2.1.4 | | |
R2.1.7        |A `datetime` string has a valid day                                 | see R2.1.5 | S3 | P3 | Rewrite the requirements to check for is Int and then if is in Range(1,y), y depending on month and year
R2.1.8        |A `datetime` string has a space between date and time               | see R2.1.4 | | |
R2.1.9        |A `datetime` string has a valid hour                                | see R2.1.5 | S0 | P3 | (optional)
R2.1.10       |A `datetime` string has a colon between hours and minutes           | see R2.1.9 | | |
R2.1.11       |A `datetime` string has a valid minute                              | see R2.1.9 | | |
R2.1.12       |Different months have different amounts of days                     | see R2.1.7 | S3 | P3 | Use a library?? 
R2.1.13       |Leap years have 29 days in February                                 | see R2.1.12 |  |  |
R2.2          |The function `is_datetime` describes the `datetime` limits          |  |  |  |
R3            |Can predict temperatures by interpolation                           | | | | 
predicting the temperature on the time a temperature measurement is made, the exact measurement is returned
R90           |Can convert temperature from Celsius to Kelvin                      |Passes the test cases |||`convert_celsius_to_kelvin(-273.15)` returns zero (Kelvin), `convert_celsius_to_kelvin(0)` returns `273.15` (Kelvin)
R91           |Can convert temperature from Kelvin to Celsius                      |Passes the test cases |||`convert_kelvin_to_celsius(0)` returns -273.15 (Celsius), `convert_kelvin_to_celsius(273.15)` returns `0` (Celsius)
R100          |Best practices are followed                                         |All team members agree|||We think we follow the best practices as found in the academic literature
R100.1        |Best practices are discussed                                        |All team members agree|||If the team agrees a practice found in the academic literature to be best, it is discussed
R100.2        |Decisions are made democratically                                   |All team members agree|||If there are candidate better practices, these are voted for/against
R100.2        |Decisions are adopted                                               |All team members agree|||If a majority vote favors a practice, we adopt it
A new line | foo| foo | foo| foo | f
<!-- markdownlint-enable MD013 -->
