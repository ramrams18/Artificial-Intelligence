Programming Language Used : Python

----------------------------------------------------------------

Task1:

To execute the program, run the following command:
    $ python compute_a_posteriori.py [observations]

Example:
    $ python compute_a_posteriori.py CCCCC

Note:
- The output is stored in result.txt
- All the decimal values are corrected to 5 points.

----------------------------------------------------------------

Task2:

To execute the program, run the following command:
    $ python bnet.py [conditions]

Example:
    $ python bnet.py Bt Af given Mf    $ python bnet.py Af Et    $ python bnet.py Jt Af given Bt Ef    $ python bnet.py Bt Af Mf Jt Et

Note:
- 'given' should be in lower case.
- Every item should start with Upper Case 'X' and end with lower case.
- The Upper case of item represents events, where 
    'A' - Alarm
    'B' - Burglary
    'E' - Earthquake
    'M' - Mary Calls
    'J' - John Calls
- While the Lower case of item represents happening in boolean. Like:
    't' - True
    'f' - False
- Say, the item is 'Af' it means Event 'Alarm Rings did not happen'.
- required-parameters and on-given-parameters are collection of items separated by space.