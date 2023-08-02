# Bikeshare Case Study

## Introduction

Cyclistic is a (fictional) bikeshare company based in Chicago. The marketing director has set the goal of converting existing casual users into annual members. The data for this analysis is provided [here](https://divvy-tripdata.s3.amazonaws.com/index.html). My analysis is focusing on the time frame of July 2022 - June 2023. In order to guide business decisions, I am focusing on a singular question:

How do annual **members** and **casual** riders use Cyclistic bikes differently?

## Preparing Data

### Limitations

The current data records rides, not riders. I do not have information to compare how many times a specific rider uses the service.

### Cleaning Data

Prior to importing the data into R, I made some cleaning adjustments. I verified that the column names were consistent across files. I added the column *ride_length* using the difference between the columns *ended_at* and *started_at* in order to later learn more about the differences in ride lengths between users. I also added a *day_of_week* column using the WEEKDAY function in order to later compare usage across days of the week.

### Importing Packages and Data

```{r packages}
install.packages("tidyverse")
library("tidyverse")
```

```{r data import, warning=FALSE}
july <- read_csv("C:/Users/Z/Desktop/Bikeshare/2022.07_bikeshare.csv")
august <- read_csv("C:/Users/Z/Desktop/Bikeshare/2022.08_bikeshare.csv")
september <- read_csv("C:/Users/Z/Desktop/Bikeshare/2022.09_bikeshare.csv")
october <- read_csv("C:/Users/Z/Desktop/Bikeshare/2022.10_bikeshare.csv")
november <- read_csv("C:/Users/Z/Desktop/Bikeshare/2022.11_bikeshare.csv")
december <- read_csv("C:/Users/Z/Desktop/Bikeshare/2022.12_bikeshare.csv")
january <- read_csv("C:/Users/Z/Desktop/Bikeshare/2023.01_bikeshare.csv")
february <- read_csv("C:/Users/Z/Desktop/Bikeshare/2023.02_bikeshare.csv")
march <- read_csv("C:/Users/Z/Desktop/Bikeshare/2023.03_bikeshare.csv")
april <- read_csv("C:/Users/Z/Desktop/Bikeshare/2023.04_bikeshare.csv")
may <- read_csv("C:/Users/Z/Desktop/Bikeshare/2023.05_bikeshare.csv")
june <- read_csv("C:/Users/Z/Desktop/Bikeshare/2023.06_bikeshare.csv")
```

I then combined the data into a single dataframe, to better see overall trends.

```{r combine}
year <- rbind(january, february, march, april, may, june, july, august, september, october, november, december)
```
