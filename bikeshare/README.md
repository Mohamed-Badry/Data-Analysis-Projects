### Summary
The following code pulls the data from the provided csv files, prompts the user for input that is used to filter the data accordingly, then displays some useful statistics from the filtered data.

### Data Structure:
File format: The data is stored in three CSV files, named `chicago.csv`, `new_york_city.csv`, and `washington.csv`, where each file represents bikeshare data for a specific city.

Features: Each CSV file contains the following features for each bikeshare trip:
  - Start time
  - End time
  - Trip duration (calculated from start and end times)
  - Start station
  - End station
  - User type (e.g., subscriber, customer)
  - Gender (if available)
  - Birth year (if available)

### Tools 
Only python and pandas are used in this project.

### Techniques
A filter is applied to the data first, then simple statistical measures are drawn out of it such as:
- The most frequent time of travel
- The most popular stations and trips
- The total and average trip duration
