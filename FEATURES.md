# Features
## 1) Days since first infection (done)
This feature can be made obsolete if we use sequence prediction models.
## 2,3) No. of cases/fatalities previous day (won't do because it will affect the testing step of the model)
Again, made obsolete by sequence prediction.
## 4) No. of ICUs / population (done)
Don't know if publicly available for every country, but can probably predict fatality rate.
## 5) No. of face masks / population
Very low probability of getting this type of information from anywhere, but worth a try.  
Study finds that surgical masks reduce infection chance for the influenza virus:  
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3591312/  
Since SARS-CoV-2 transmission is similar, there is sufficient reason to believe they are effective against this virus as well.  
## 6) Use of off-label medicine/degree of self-medication
The willingness of the populace to try experimental drugs
## 7) Chloroquine/Hydroxichloroquine/HCQ + azithromycin use (done)
Countries that have higher than average use of these drugs may have lower infection rates. Look at countries where malaria is present: chloroquine and hydroxichloroquine are antimalarials.  
Lots of studies (in vitro) and empirical observations confirm this:  
https://www.nature.com/articles/s41421-020-0156-0  
https://www.youtube.com/watch?v=n4J8kydOvbc (French)  
## 8) Avg. age/Ratio between people >55 (>65? >70?) yrs. and total population (done)
High mortality among the elderly.
## 9) GDP per capita
https://web.archive.org/web/20200322232005/https:/twitter.com/MaxCRoser/status/1241850312203415552  
Maybe a confounder for something else. Usually the higher the GDP, the more financial elites the country has. Elites tend to travel and interact with people from other countries. Maybe this relationship is present only in the first stages of infection.  
## 10) Pollution levels
The virus has thrived in the Hubei region of China and the northern part of Italy, both strong industrial polls with above average air pollution levels. The virus is known to transmit through aerosols and particles that float in the air, so there is reason to believe that pollution levels are positively correlated with infection rates.  
## 11) Sanitation level
SARS-CoV-2 can be transmitted through the fecal-oral route, so lack of bathrooms could also play a role in the transmission of the virus.
## 12) Temperature
## 13) Relative/absolute humidity
Studies that discuss this relationship can be found here:  
https://web.archive.org/web/20200319132214/https://twitter.com/LoCtrl/status/1240050094394634240
## 14) Ethnicity/race
Study here:  
https://www.biorxiv.org/content/10.1101/2020.01.26.919985v1.full  
Could be a factor, but would be a bit strange to use. Shold we use haplogroups or folk understanding of rthnicity/race?
## 15) Climate
Can be estimated using latitude and longitude. Greatest number of cases usually concentrated around lat. 40&deg;N.
## xx) Ski areas
This one is a bit of a joke, but > 0 probability that it correlates with infection rates.

# Data sources:
## a) https://ourworldindata.org/coronavirus

# Additional notes:
\**The number of cases over time can be modeled by an exponential function. Maybe we can exploit this information.*  
\*\**We should estimate the number of people that stay home somehow. This has strong predictive power. Maybe how many users from a country have visited facebook/twitter on that day?*  
\*\*\**There are other viruses which are similar in some respects to the novel coronavirus: influenza (transmission vector), SARS-CoV and other related viruses (MERS-CoV).*  
