
# CITYBYTES

## SOFTWARE CODE DOCUMENTATION

<p align="center">
    <img width="300" src="docs/assets/images.jfif" alt="NC Logo">
</p>

## TEAM MEMBERS

| Name | UnityID |
|--------|--------|
|Nirav Shah | nshah28 |
| Vishwa Gandhi | vgandhi |
| Pradymna Khawas | ppkhawas | 
| Vrushanki Patel | vpatel25 |
| Priya Saroj | pbsaroj | 

## INTRODUCTION

Moving to a new location can be a daunting endeavor, especially when you have the entire United States to choose from. Finding a new home from scratch while prioritizing certain aspects might be very challenging given the variety of nations and cities. However, with the advancement of technology, information from earlier times can now be leveraged to offer a number of vital insights about a certain location. Our project succeeds in one of those objectives. We seek to present that information in our project because there are many other elements that are taken into consideration when choosing a place to reside, such as weather, temperature, entertainment options, landmark locations, education, and many more. The project is totally created using a variety of technologies, including some of the accessible APIs that are utilized to fetch real-time data.

Although this project is still in its early phases of development, it can be expanded up even further by including multiple features that can benefit society in a variety of different ways. This article offers a critical viewpoint that users can use to comprehend the project, adopt it as open source software, and add further features before releasing it to the market. The document also serves as a starting point for the project and helps developers understand the code.

The technologies listed below were used to build the entire project, and it is advised that the group of developers who take on this project in the future retain these tools on hand.
* Python
* Django
* Pytest
* HTML
* CSS
* JavaScript
* BootStrap

Although we have used HTML, CSS and Bootstrap for the frontend logic the user can use any technologies and combine it with backend such as Angular, React etc.

## CODE FUNCTIONALITIES

The project basically uses Django for the backend logic. Django is a Python framework that is useful to build websites. It uses model view and templates architecture. Some of the files used in Django are as follows:-
* Views.py:- Backend logic is being written in this file. It takes http requests as arguments, imports relevant models and figures out what data needs to be sent to the template and returns the final result.
* Models.py:- Django has Object Relational Mapping which makes it easier to work with databases.The model provides data from the database.
* templates/:- They are used to store templates for frontend development and html files.
* Urls.py:- They are used to set the urls of the django project and apps. The endpoints created are stored in the urls files.
* Tests.py:- They are used to write the test cases for the code. They are used to check the code.
* Settings.py:- It has the basic information about the various api’s used and initializes the environment required for the project.

## HOW DOES CITYBYTE WORK?

Firstly, there is a project that needs to be created in Django named CityByte. Then there are two apps named as info and search in the directory. The urls are set in the urls.py file. Both the apps use utils and helper functions which are used to call the api to fetch the real time data. The frontend logic is written using the JavaScript, HTML , CSS and Bootstrap in the templates directory. Most of the backend logic is written in the views.py file which uses utils and helpers to give the desired output. We will be talking about different endpoints which are rendered using functions in the views file. Hence this section of the documentation will further explain various functions written in the views file.

1. def main_page: Main page is used to render the HTML template which has some front-end logic written in javascript. It is used to run the first page of our website.
2. def info_page: Info page takes two request params namely city and country, which provides city and country respectively. The “weather info” variable includes the WeatherBitHelper function which uses WeatherUtilBase to get the data of city and country. The weather_info delivers the information of sunrise, sunset, and timezone of that particular city. The “dining info” variable takes the FourSquarePlacesHelper function that uses FourSquarePlacesUtilBase to get the dining information of that city. The variable “outdoor info” receives the information about places to visit outdoors from the FourSquarePlacesHelper function that uses FourSquarePlacesUtilBase. Similarly, “airport info” and “arts info” variable stores the information regarding airport and arts places respectively, from the FourSquarePlacesHelper function that uses FourSquarePlacesUtilBase. The “photo link” variable generates the photo of the entered city using the UnplashCityPhotoHelper function which uses PhotoUtilBase in the Unsplash class. All the following variables is passed to context using jinja templating.
3. def city_suggestions: City suggestion function receives the user city input, and request to the GenericDBSearchAutoCompleteHelper function that uses SearchAutoCompleteHelperBase class, which collects all the necessary information of that particular city and provide JSON response, which is reflected in the first page of our website.
4. def city_photo: The City photo function uses the “photo link” variable that receives the information from UnplashCityPhotoHelper, and returns the JSON response which includes the path of the photo link and not the photo itself.
5. def place_photo: The function place photo has the “photo link” variable that uses fsq_id unique ID for that particular place and renders the photo link.

The below screenshots give the glance of the working of our project.

![city 1](https://github.com/therealppk/CityByte/blob/main/docs/assets/City%201.png)

![city2](https://github.com/therealppk/CityByte/blob/main/docs/assets/City%202.png)

![city3](https://github.com/therealppk/CityByte/blob/main/docs/assets/City%203.png)

![city4](https://github.com/therealppk/CityByte/blob/main/docs/assets/City%204.png)

![city5](https://github.com/therealppk/CityByte/blob/main/docs/assets/City%205.png)

## FUNCTIONAL TESTING
For functional testing of the code, a separate testing script is written to validate the output generated by the CityBytes.
The scripts are written in 
CityByte\search\tests\test_photo.py
Initially there are four test cases that have been used for validation of the software.

Test Case 1: test_main_page is the first test case that renders the search.html template which runs the main page of our website.

Test Case 2: test_info_page is the second test case for the validation of user request fetching, when a user is entering a city, the test case would check whether the information in the request has been received. After that the information fetched is checked which includes the data regarding weather, time zone, dining information, outdoor information, airport details and arts & museum data. At the end it verifies the rendering of the request for all the given features: weather_info, dining_info, outdoor_info, airport_info, photo_link, & arts_link.

Test Case 3: test_photo is our third test case that checks the photo_link, and makes sure that the photo is not fetched instead of the url from the http request.

Test Case 4: test_cityphoto is the test case for testing the UnplashCityPhotoHelper which is redirected from photo_link to site, to get the header of the http request. This test case checks whether the content type is an image.

## FUTURE SCOPE

* Chasing results from API using Redis in order to improve the performance.
* Addition of search bar with category filter, that will help the user to search based on his/ her requirements.
* To run multiple API requests simultaneously, multithreading will be used.
* Various multiple features about cities can be added as per the user requirements and customer segmentation.
