**Research Question**

Has the timing of seasonal temperature transitions shifted over time?

**Hypothesis**

There has been a shift in seasonal temperature transitions from the 1700s to the 21st century.

**Methods**

A comparative analysis across four time periods, using the 1700s–1800 as a baseline:

- Period 1: 1700s–1800 (baseline)
- Period 2: 1800–1900
- Period 3: 1900–2000
- Period 4: 2000–2025

**Results**

Data will be presented in graphs and assessed using p-values.

## Discussion
This will be trend analysis or comparative study on data available only with out any input of historical events




# Requirements

<!-- markdownlint-disable MD013 --><!-- Tables cannot be split up over lines, hence will break 80 characters per line -->

Requirement ID|Requirement description                                             |Acceptance criteria   |Test cases                                                                |Risk analysis
--------------|--------------------------------------------------------------------|----------------------|---------------------------------------------------------------------------------|----------------------------------------------
R1            |Reading the data file follows best practices                        |Passes the test case  |The `.csv` file is parsed correctly by a function called `read_data` | the file could be misread without a clear and defend title.
R1.1          |The data file can be read                                           |Passes the test case  |The content of the file can be read without errors
R1.2          |Reading the data file produces a table                              |Passes the test case  |Reading the existing data file (in `/data`) produces a table
R1.2          |The table produced from reading the data has correct column names   |Passes the test case  |The column names must match between file and the table that is created by reading the file
R1.3          |The table produced from reading the data has the correct content    |Passes the test case  |The column names must match between file and the table that is created by reading the file
.             |.                                                                   |Passes the test case  |The content of the first row of the table created by loading the file, matches exactly the content of the first row in the file
R1.4          |Read data file is read in a short time                              |Passes the test case  |The file is read within 1 second
R1.5          |Reading an absent file gives an error                               |Passes the test case  |If the file cannot be found, create a helpful error message, that includes the path of the absent file
R1.6          |Table column names are documented                                   |Passes the test case  |The documentation contains the names of the columns
.             |.                                                                   |Two humans agree      |The documentation describes the content of the columns
R2            |Can work with `datetime` strings                                    |Passes all test cases |. | this could be over engineered
R2.1          |The function `is_datetime` detects a `datetime` correctly           |Passes all test cases |`is_datetime` returns true if the string passed to it is `2025-02-28 16:40`
R2.1.1        |`is_datetime` works on a string                                     |Passes all test cases |`is_datetime` raises an exception if it is passed something else than a string as its only argument
R2.1.2        |`is_datetime` works on a string of the correct length               |Passes all test cases |`is_datetime` returns false if the string passed to it has a length other than 16, e.g. `nonsense`
R2.1.3        |A `datetime` string has a valid year                                |Passes all test cases |`is_datetime` returns false if the first 4 characters of a `datetime` string are not numbers, e.g. `XXXX-02-28 16:40`
R2.1.4        |A `datetime` string has a dash between year and month               |Passes all test cases |`is_datetime` returns false if the 5th character of a `datetime` string is not a dash, e.g. `2025X02-28 16:40`
R2.1.5        |A `datetime` string has a valid month                               |Passes all test cases |`is_datetime` returns false if the 6th and 7th character of a `datetime` string is not a number from `01` to and including `12`, e.g. `2025-99-28 16:40`
R2.1.6        |A `datetime` string has a dash between month and day                |Passes all test cases |`is_datetime` returns false if the 8th character of a `datetime` string is not a dash, e.g. `2025-02X28 16:40`
R2.1.7        |A `datetime` string has a valid day                                 |Passes all test cases |`is_datetime` returns false if the 9th and 10th character of a `datetime` string is not a number from `01` to and including `31`, e.g. `2025-02-99 16:40`
R2.1.8        |A `datetime` string has a space between date and time               |Passes all test cases |`is_datetime` returns false if the 11th character of a `datetime` string is not a space, e.g. `2025-02-28X16:40`
R2.1.9        |A `datetime` string has a valid hour                                |Passes all test cases |`is_datetime` returns false if the 12th and 13th character of a `datetime` string is not a number from `00` to and including `23`, e.g. `2025-02-28 99:40`
R2.1.10       |A `datetime` string has a colon between hours and minutes           |Passes all test cases |`is_datetime` returns false if the 14th character of a `datetime` string is not a colon, e.g. `2025-02-28 16X40`
R2.1.11       |A `datetime` string has a valid minute                              |Passes all test cases |`is_datetime` returns false if the 15th and 16th character of a `datetime` string is not a number from `00` to and including `59`, e.g. `2025-02-28 16:99`
R2.1.12       |Different months have different amounts of days                     |Passes all test cases |`is_datetime` returns false if the date is not valid in regular years, e.g. `2025-02-31 16:40`
R2.1.13       |Leap years have 29 days in February                                 |Passes all test cases |`is_datetime` returns true for the date 29th February of a leap year, e.g. `2024-02-29 16:40`, but false for a non-leap year, e.g. `2023-02-29 16:40`
R2.2          |The function `is_datetime` describes the `datetime` limits          |Two humans agree      |The documentation describes the limits of a `datetime` string, e.g. going from year 1 to and including year 9999
R3            |Can predict temperatures by interpolation                           |Passes the test cases |.
.             |The function `predict_temparature`'s first argument is the data     |Passes the test case  |Passing `predict_temperature` the data read from the file as a first argument gives no exception
.             |.                                                                   |Passes the test case  |Passing `predict_temperature` any other type of data as a first argument raises an exception
.             |The function `predict_temparature`'s second argument is a `datetime`|Passes the test case  |Passing `predict_temperature` a `datetime` as a second argument gives no exception
.             |.                                                                   |Passes the test case  |Passing `predict_temperature` any other type of data as a second argument raises an exception
.             |Predicting before the first measurement fails                       |Passes the test case  |The function `predict_temparature` raises an exception
.             |.                                                                   |.                     |When predicting the temperature on the time exactly between two temperature measurements, the predicted temperature is the average of the two
.             |.                                                                   |.                     |When predicting the temperature on the time a temperature measurement is made, the exact measurement is returned
R90           |Can convert temperature from Celsius to Kelvin                      |Passes the test cases |`convert_celsius_to_kelvin(-273.15)` returns zero (Kelvin), `convert_celsius_to_kelvin(0)` returns `273.15` (Kelvin)
R91           |Can convert temperature from Kelvin to Celsius                      |Passes the test cases |`convert_kelvin_to_celsius(0)` returns -273.15 (Celsius), `convert_kelvin_to_celsius(273.15)` returns `0` (Celsius)
R100          |Best practices are followed                                         |All team members agree|We think we follow the best practices as found in the academic literature
R100.1        |Best practices are discussed                                        |All team members agree|If the team agrees a practice found in the academic literature to be best, it is discussed
R100.2        |Decisions are made democratically                                   |All team members agree|If there are candidate better practices, these are voted for/against
R100.2        |Decisions are adopted                                               |All team members agree|If a majority vote favors a practice, we adopt it

<!-- markdownlint-enable MD013 -->




What is a Verification and validation? 
	- Verification - if the Software is doing what it should be doing
	- Validation - is that Software stable, not such for me but for others
Both of these steps are needed for a good quality in coding and software. 

What are requirements and why do they need to be specific? 
	- What is needed and important in that particular software to function to the best of its capability. 

Regulatory requirements - used to show how you designed something and how AI is used in your work. 

Software Requirements Specification (SRS) - 
Requirements need to be specific but not too much so you don’t lose your information and cause confusion - so you need to use the minimum amount to reach the desired level. Sometimes you define a requirement as a high level so there needs to be an underline base understanding. 
- Risk of over-engineering and risk of under-specifying 
- Risk of sharing data AI when it comes to specific requirements 
- Write a test for your requirement and see if you filled that requirement 
- Define and draft requirements


Hope and dream - version control 
  

