# Election-Analysis

## Project Overview

The purpose of this project is to help a Colorado Board of Elections employee named Tom with an election audit. Tom has provided the tabulated results for a U.S. congressional precinct. This audit will be done with Python instead of Excel. This Python script is also capable of auditing other elections for the Colorado Board of Elections.

This project will:

  1. Calculate the total number of votes.
  2. Get a complete list of the candidates who received votes.
  3. Calculate the total number of votes each candidate.
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on popular vote.
  
  
## Election Results

- Total votes: 369,711

- County votes:
  - Jefferson:   10.5%   (38,855)
  - Denver:      82.8%   (306,055)
  - Arapahoe:    6.7%    (24,801)
  
- County with the largest turnout: Denver

- Votes by candidate:
  - Charles Casper Stockham:  23.0%   (85,213)
  - Diana DeGette:            73.8%   (272,892)
  - Raymon Anthony Doane:     3.1%    (11,606)
  
- Winner of the election: Diana DeGette with 272,892 votes and 73.8% of the vote.


 ## Resources
 
 -Data Source: election_results.csv
 -Software: Python 3.10.5, Visual Studio Code 1.72.2
 
 
## Summary


This project has provided the Colorado Board of Elections with a valuable tool to audit tabulated elections. It has been written in such a way that it retrieves county and candidate names from the data source to automate inputs. Currently, this code could be used for other similar elections by changing the input data. With slight modifications the code can be used for state and local elections. Counties can be easily replaced by precincts or districts and candidates can be replaced by ballot initiatives. I believe it would be in the best interest of the Colorado Board of Elections to continue this business partnership and allow me to help with the analysis of future elections.
