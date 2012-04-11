Converts Co-operative Bank business statements in CSV format for loading into Xero.

Input has a few header lines, then lines like this (with some numbers replaced with X):

 Date,Description,Bank     Reference,Customer  Reference,Credit,Debit,Additional Information,Running  Balance
16/02/2012,Standing Order,EPXXXXXXXXXXXXXX,BYTEMARK HOSTING,,XXXX.XX,BENEFICIARY ACCOUNT - XXXXXXXXXXXXXXXXXXXX,XXXXXXXXX.XX

Output converts Credit/Debit into one number

