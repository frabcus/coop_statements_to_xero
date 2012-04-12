Co-operative Bank to Xero
=========================

Pythons cript to convert Co-operative Bank Business Account statements to Xero.


Instructions
============

1. Download script.py from this repository, install Python if you haven't already.

2. From your Co-operative Bank online banking, download the CSV file as a spreadsheet.

3. cat the file into the Python script, and store the output CSV file.

    $ cat Report-20120410133658.csv | ./script.py > ~/Downloads/xero.csv

4. Go to the bank account, choose Manage Account, and Import a Statement.

5. Select the CSV file. And Import.

6. The first time you will need to match against Xero's terminology. Use the
*last* column which contains Debit-Credit for the account value.


Technical notes
===============

Input has a few header lines, then lines like this (with some numbers replaced with X):

 Date,Description,Bank     Reference,Customer  Reference,Credit,Debit,Additional Information,Running  Balance
16/02/2012,Standing Order,EPXXXXXXXXXXXXXX,BYTEMARK HOSTING,,XXXX.XX,BENEFICIARY ACCOUNT - XXXXXXXXXXXXXXXXXXXX,XXXXXXXXX.XX

Output converts Credit/Debit into one number


