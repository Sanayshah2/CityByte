# CityByte 


[![DOI](https://zenodo.org/badge/541612969.svg)](https://zenodo.org/badge/latestdoi/541612969) ![](https://img.shields.io/github/license/therealppk/CityByte) ![](https://img.shields.io/github/issues/therealppk/CityByte?style=plastic) ![](https://img.shields.io/github/issues-closed-raw/therealppk/CityByte?style=plastic) ![](https://img.shields.io/github/languages/code-size/therealppk/CityByte?style=plastic) ![](https://img.shields.io/github/contributors/therealppk/CityByte?style=plastic) [![Django CI](https://github.com/therealppk/CityByte/actions/workflows/django.yml/badge.svg)](https://github.com/therealppk/CityByte/actions/workflows/django.yml)
[![Code Coverage](https://codecov.io/gh/Sanayshah2/CityByte/branch/main/graphs/badge.svg)](https://codecov.io/gh/Sanayshah2/CityByte/branch/main)



<p align="center">
  <img src="https://github.com/therealppk/citybytesrough/blob/main/CityBytes.gif" alt="animated" />
</p>

## Introduction
Moving to a new location can be a daunting endeavor, especially when you have the entire world to choose from. Finding a new home from scratch while prioritizing certain aspects might be very challenging given the variety of nations and cities. However, with the advancement of technology, information from earlier times can now be leveraged to offer a number of vital insights about a certain location. Our project succeeds in one of those objectives. We seek to present that information in our project because there are many other elements that are taken into consideration when choosing a place to reside, such as weather, temperature, entertainment options, landmark locations, education, and many more. The project is totally created using a variety of technologies, including some of the accessible APIs that are utilized to fetch real-time data.

Although this project is still in its early phases of development, it can be expanded up even further by including multiple features that can benefit society in a variety of different ways. This article offers a critical viewpoint that users can use to comprehend the project, adopt it as open source software, and add further features before releasing it to the market. The document also serves as a starting point for the project and helps developers understand the code.

The technologies listed below were used to build the entire project, and it is advised that the group of developers who take on this project in the future retain these tools on hand:

* Python3
* Django
* Pytest
* HTML
* CSS
* JavaScript
* BootStrap

Although we have used HTML, CSS and Bootstrap for the frontend logic the user can use any technologies and combine it with backend such as Angular, React etc.


## Video
<a href="https://youtu.be/5A2mUY-ouJ8">
<img src="https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/NY1%20(1).png" width="400" height="200"></a>
[Click on the image above to play, click here if that does not work](https://youtu.be/5A2mUY-ouJ8)

## Result
The below screenshots give the glance of the working of our project:

![](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/IS1.png)
![](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/IS2.png)
![](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/IS3.png) 
![](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/IS4.png)
![](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/IS5.png)
![](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/IS6.png)





## SCALABILITY
1. New Features:
* Previously, the information that CityByte provided were limited to top rated dinning spots, top rated entertainment spots, landmark spots, artistic spots, and airports.
* Now, we have added some exciting new features to this website to make it more comprehensive. Newly added features include organization, events, health, travel, sports, and community which is clearly visible in the results.

2. Caching
* In order to reduce the time it takes to respond, we implemented caching using Redis.
* When a http request was made in the past, the response was always provided by using APIs each time the user entered in the city. Now that the project has been scaled, a database has been created that stores city information when the API is first called.
* Hence, when a user types the same city the database is called several times to provide the response. Due to the time saved from not calling the APIs, this has improved performance when there are numerous requests coming in for a some city.
* We developed a debug toolbar for the website to show information about the caching time in order to display this functionality. 
* Below is the screenshot of the debug toolbar which gets request from the API. It also displays the CPU time and request comes from "set" method before implementing caching.
![](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/API.png)
* After implementing the caching, the following screenshot gives information of the "get" requests coming from caching instead of "set" requests. Also, the difference between the CPU time is visible.
![](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/cache.png)


3. Multiprocessing:
* Initially, the project consisted of various APIs being called serially, one after another to provide the desired response. This resulted in a lot of time being occupied for getting the results from APIs. 
* So, the concept of Multiprocessing in which two or more processors in a computer simultaneously process two or more different portions of the same program (set of instructions) was implemented.

The below screenshots gives the glance of the new features that we added in the project.

![city 1](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/NY1%20(1).png)

![city2](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/NY2.png)

![city3](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/NY1%20(2).png)

![city4](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/NY1%20(3).png)

![city5](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/NY1%20(4).png)

![](https://github.com/Sanayshah2/CityByte/blob/main/docs/assets/NY1%20(5).png)

## Code Coverage
[![codecov](https://codecov.io/gh/therealppk/CityByte/branch/main/graph/badge.svg?token=HRK9X7OI2J)](https://codecov.io/gh/therealppk/CityByte)

![](https://github.com/therealppk/CityByte/blob/main/docs/assets/code_coverage.png)


## FUTURE SCOPE

* Addition of search bar with category filter, that will help the user to search based on his/ her requirements.
* Since REDIS is being used, if this website is being used by many people, RAM will run into storage problems. So, to further enhance the functionality of this website, storage in a cloud can be used.

## Contributors

#### Project 1
* Nirav Shah - nshah28
* Vishwa Gandhi - vgandhi
* Pradyumna Khawas - ppkhawas
* Vrushanki Patel - vpatel25
* Priya Saroj - pbsaroj

#### Project 2
* Elizabeth Lin - etlin
* Neel Shah - npshah6
* Sanay Shah - sshah34
* Shaival Shah - sshah35
* Shivesh Jha - sjha7
