# dNBR_calculator
Final Project for python programming. this tool will generate a differenced normalized burn ratio index and calculate total area of wildfire damage. the README file contains a more detailed description of the project.

##Summary
this project is an attempt to recreate a dNBR python tutorial made by Leah Wasser and Megan Cattau. they wrote most of the code in my program but left a lot of crucial code out of the tutorial to try and teach the thought process and workflow of a project like this. with that being said I never got to run the code in my program to see if my solutions or changes actually worked. the computers i had to work with could not install third party python libraries. to see more of the tutorial go to 
https://www.earthdatascience.org/courses/earth-analytics-python/multispectral-remote-sensing-modis/calculate-dNBR-Landsat-8

##Overview and Application
with wildfires becoming more destructive and deadly across the western united states it is important to be able to gauge wildfire damage and severity without using in situ data. an effective tool for gauging wilfire burn severity is an index known as a normalized burn index (NBR). an NBR estimates the burn severity using landsat 8 imagery bands 5 (NIR) and bands 7 (SWIR2). 
###NBR = ((NIR band - SWIR2 band)/(NIR band + SWIR2 band)). 
an NBR alone does not tell us anything about burn severity specifically. to get a complete story on burn severity it is important to calculate NBR prefire and subtract it from the NBR postfire.
###dNBR = (NBR prefire - NBR postfire)

##problems and concerns 
since i was never able to run the code i do not actually have a concrete answer for the requirements to make this code run. earth analytics has a tutorial on how to set up the python environment we will need. the tutorial can be found here
https://www.earthdatascience.org/workshops/setup-earth-analytics-python/
the other issue with this program is that it was above my current skill level and expected the people in the tutorial to recall code from earlier lessons in earthdatascience.org. overall the tutorial would have been easier if i had more experience with these third party libraries and had been following alond with all of their lessons.
