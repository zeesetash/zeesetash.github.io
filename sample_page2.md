# Virginia Public Schools

As a former teacher, I have great interest in educational data. As an educator, you are constantly looking at data comparing students, classes, schools, and even divisions. Each division wants to be the best. Each school wants to be the best. This lead me to my overarching question: 

**What are common traits within the best and worst performing schools?**

## The Data 
I taught in Virginia, so my focus in on Virignia public schools. This uses the most recent complete data which is from the 2021- 2022 school year. All of the data is sourced from the Virginia Department of Education which I cleaned and compiled on [Kaggle](https://www.kaggle.com/datasets/zsetash/virginia-public-schools). As there are multiple schools with the same name in different divisions, I created a primary key titled Sch_Div that is present through all of the datasets to ensure there was no confusion over which school was which. The data contains information about:
- State Assessment (SOL) Pass Rates
- Chronic Absenteeism Rates
- Graduation Rates
- Free and Reduced Lunch Eligibility
- State and Federal Funding
- Teacher Experience, Education, and Licensure
- Student Demographic information

In order to define the *best* and *worst* schools, I used the end of state testing, the Virginia Standards of Learning (SOL) Test. For my analysis, I excluded schools that are geared towards students with disabilities or behavior issues. The best schools are the schools that ranked in the 95th percentile or above for average pass rate on the SOL tests. These were average  pass rates of 88.6 or higher. The worst schools are the schools that ranked in the 5th percentile or below for average pass rate on the SOL tests. These were average pass rates of 38 or below. 

## Analysis

### Geographic Trends
<img src="images/Story 1.png?raw=true"/>

Both the top ranked and bottom ranked schools are gathered near cities. Most of the lower performing schools are in cities. The top schools are more spread out, while the bottom schools tend to be more clustered. There do not appear to be trends based on the per capita income. Both high and low performing schools can be found accross the income spectrum by county.

## School Funding
<img src="images/Story 1 (3).png?raw=true"/>

The lowest perfoming schools spend more money per pupil. The bottom schools spend $2,000 more per pupil than the top schools on average and $3,000 more per pupil than all other schools on average. However, the higher performing schools spend more money overall on average. There are some costs that are excluded from the per pupil calculation but are included in the total expenditure. According the the VDOE:
> Excluded expenditures include adult education, community services, non-regular school day programs, capital purchases, debt service, food services, and fund transfers.

Therefore, the higher performing schools are spending more money on extracurricular activities.

The images are from my [Tableau](https://public.tableau.com/views/VirginiaPublicSchools/Story1?:language=en-US&:display_count=n&:origin=viz_share_link) dashboard.
