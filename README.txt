Jo-Jo Feng, Shreya Dixit, Hendrick Townley

Please see the write up included with our submission for more information about the motivation and functionality of our databases project. This README includes information necessary to loading and manipulating the frontend interface that we have created. 

** Loading the frontend interface

- Our interface can be accessed at the following URL: 
	https://jjf32897.github.io/bulldogenergy/
- The code we wrote for the backend can be accessed at the following github:
	https://github.com/shreyadixit19/yenergi
- The code we wrote for the frontend can be accessed at the following github:
	https://github.com/jjf32897/bulldogenergy
- Please allow a few minutes for the heroku server to start and for the data to be properly loaded, this may require refreshing a few times until you see circles appear on the map


** Manipulating the frontend interface

Several options to manipulate the data visualization are located to the left of the map.

- Adjusting the slider specifies which month to view data from. The month selected is displayed above the slider. Buildings are displayed on the maps as circles, with the size of the circle corresponding to how much energy the building used that month. Notice how the circles expand and contract as the slider is changed, demonstrating how energy usage of various buildings changes month by month. Zoom and drag on the map as you please. Hover over any circle displays the name of the building and how much energy it is using. Below the slider is the average temperature (in Fahrenheit) of the selected month. Notice that the color of the circles displayed on the map changes with temperature (becomes redder with higher temperatures, bluer with colder).
- Further below the slider is the total energy used by all of the buildings displayed on the map. This value will change to the total number of students if the data being displayed is student counts per residential college.
- You can filter the buildings displayed by specifying the maximum energy consumption to display. Select a filter, and notice how only buildings with consumption levels below the threshold are displayed; all buildings with higher consumption are eliminated from the map.
- For more specialized analysis of residential college usage, you can select "Only colleges" to view only residential colleges. You can see college energy usage fluctuate over time. Relatedly, you can change the map to view student count per residential college instead of energy usage data. This provides more insight into the relationship between energy use and student number within colleges. (Note that student data is only available for Fall 2018, because it had to be manually scraped from the Yale Facebook, which only displays data for the current academic semester.)
