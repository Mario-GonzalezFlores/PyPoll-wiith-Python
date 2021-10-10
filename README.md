# PyPoll-with-Python

## Overview of election audit: Purpose of this election audit

The purpose of this exercise is to determine the results of the vote session for the US congressional presinct of Colorado, giving a concise report on the turnout, votes per county and determine the votes each candidate recieved and who is the winner of the election.

## Election audit results:

### Total votes and votes per county
![Total_Votes](https://user-images.githubusercontent.com/89816213/136707359-2cf6221c-e303-4f59-aefb-9502d7eb8ba9.PNG)

The total turnout was of 369,711 votes among the three districts: Jefferson, Denver and Arapahoe; of which each of them had the following participation in the total:

![image](https://user-images.githubusercontent.com/89816213/136707467-baca2e01-8603-4b77-ae7d-a0d27f267ee9.png)

It's evident that most of the votes came from Denver, with a weight of 82.78%, followed by Jefferson with 10.51% and, at last, Arapahoe represented 6.71% of the vote.

### Votes per Candidate

![Candidates_results](https://user-images.githubusercontent.com/89816213/136707790-c80f04d3-d801-4afc-8aef-32546bd3b79b.PNG)

As for the candidates, as shown in the image above, we can see that Diana DeGette won with a wide margin, obtaining 73.8% of the total vote (272,892 votes); followed, not close, by Charles Stockham, with 23% of the votes (85,213). At this point, it0s important to pint out that the winner recieved at least three times as much votes as the immediate next, conceding no chance for doubt as for the results in the election. Raymond Donane obtained 11,606 votes, representing 3014% of the tota.


## The script: Refactoring oprions

This code can be used, as it currently is written, to audit similar election processes, being able to preent the results for candidates and counties:

![Code_variables](https://user-images.githubusercontent.com/89816213/136708647-955d8162-cc44-40a2-af25-928a550d9d32.PNG)

By seeing this code we can infere that actually it's possible to breakdown the results and know the winner in each county by creating a dictionary of dictionaries that could hold both the candidate votes and the county votes. 

Also, we could, by turning that dictionary on the opposite side, know the votes each candidate recieved in each county. Though both options sound similar, they would offer different vies to ease the analysis given the needs of whom uses it.
