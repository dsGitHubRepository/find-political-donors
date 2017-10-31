# Contents
1. [Introduction: Political Fundraising](RAEDME.md#objective)
2. [Challenge Summary](README.md#challenge-summary)
3. [Details of the challenge](README.md#input-data)
4. [Approach towards solution](README.md#solution)


### Introduction
Federal election commission regularly publishes campaign contributions. Though identifying individual donors in terms of their $ contributions are important but we will not do it since federal law phohibits that. As a data analyst we would rather identify lucrrative time and area for soliciting future donations for similar candidates.  

### Challenge Summary
Fom campaign contributions input files such as  cn.txt, cm.txt, ccl.txt; etc were chosen. From each entry only relevant field such as committee ID, zip code, transaction date, transaction amount and other ID was chosen to distill two ouput files such as 

1. medianvals-by-zip.txt
2. medianvals-by-date.txt

medianvals-by-zip: Presents a running median, total dollar amount and total number of contributions by recipient and zip codes.

medianvals-by-date: Presents calculated median, total dolalr amount and total number of contributions by recipient and date.

### Details of the challenge
From available data sets construct "itcont.txt" where each entry would contain information regarding campaign contribution that was made on a particular "date" from a donar to a political campaign, committee or other similar entity. 

We are primarily interested with

1.  donor ID  ( OTHER-ID )
2. donor zip code  ( ZIP-CODE )
3. $ amount contributed ( TRANSACTION-AMT )
4. date of transaction ( TRANSACTION-DT )
5. recipient ID  ( CMTE-ID )

### Approach towards solution

For this work I picked "itoth.txt" from link: http://classic.fec.gov/finance/disclosure/ftpdet.shtml#a2017_2018
This input exceeds the 25MB limit so I pasted first few lines in /input/.

Initially I splitted each line entry into parts so that IDs, zip codes, transaction, date can be pulled conveniently as per the requirement of the challenge.

In step 02, from each splitted line since the date MM/DD/YYYY, transaction dollar and other-ID whether it exists or empty appears 
in successive order, so at this stage an "INDEX[]" was introduced to filter data for which OTHER-ID is "empty" as required. Here the date 
"DATE[]" and "DOLLAR[]" are listed for which OTHER-ID is empty. At this stage I also made sure taht YYYY of date is 2017-> (7) and 2016 -> (6) has been set as filtering condition in the code.

In step 03, an additional input file states.txt which is basically an alphabatical list of US states "USSTATES[]" is introduced to facilitate listing of zip codes since zip codes appears right after states such as NY 20003. since zip code appears as 5 or 9 digit though many other split entry of each line is 5 or 9 digit, hence additional states.txt was introduced. 

Here I have listed the valid zip code "ZIP-CODE[]" corresponding ids "ID[]" and an index that corresponds to valid zip code list eventually be used to list the corresponding dolalr contribution "DOLLARRBZ[]" and date "DATERBZ[]"

From zip code list identical zip codes sorted along with their indices and those indices been used to produce output file to get the rolling sum of dollar contribution. Remaining part of the code can be done the same way but indices for indentical date be sorted first and the procedure as this one.







