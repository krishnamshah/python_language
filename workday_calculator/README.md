# Workday calendar

## Description
We need a way to calculate where we end up if we go back or forth x number of working days, from a given point in time. A working day is defined as a day from Monday to Friday which is not a holiday. We need to be able to set which days shall be regarded as holidays. Holidays shall not count as a working day. We also need to be able to register recurring holidays. A recurring holiday says that the given date is to be regarded as a holiday on the same date every year. We need to be able to set when a working day starts and stops. We need to be able to add some working days to a given start datetime and get the resulting datetime. The date in the result must be a workday. The time in the result must be within the working hours set by the start and stop time, even though the start date need not follow this rule.

*According to this rule then 15:07 + 0.25 working days will be 9:07, and 4:00 + 0.5 working days will be 12:00.*

## Example
- Set workday start 08:00, end 16:00
- Set recurring holiday 17 May.
- Set single holiday 27 May 2004.
- Start date = 24.05.2004 18:05
- Add -5.5 workdays.
- The result should be 14.05.2004 12:00

### Some other correct results:
* 24-05-2004 19:03 with the addition of 44.723656 working days is 27-07-2004 13:47
* 24-05-2004 18:03 with the addition of -6.7470217 working days is 13-05-2004 10:02
* 24-05-2004 08:03 with the addition of 12.782709 working days is 10-06-2004 14:18
* 24-05-2004 07:03 with the addition of 8.276628 working days is 04-06-2004 10:12 

## Setup
To run this program, you will need Python 3 installed on your machine. You can check if you have Python 3 installed by running the following command in your terminal:
```
python3 --version
```


## Usage

You can run the program from the command line by navigating to the directory where the program is located and running the following command:

```python
python3 workingdaycalculator.py
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pytest.

```bash
pip install pytest
```


## Future Updates
* Get the input directly from the command line.
* Make it faster with the use of Cython.
