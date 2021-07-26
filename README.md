# RateMySite

## Author  
  
>[Angela-Mutyota] 

##  Live Link 
 Click (https://inthel00p.herokuapp.com/)  to visit the site
  
# Description
This is a Django web application that allows its users to be in the loop about everything happening within the neighbourhood. Users are able to join a neighbourhood and can receive all the information they need such as businesses in the neighbourhood, posts by other members and contact information for the administration, health department and police.

# user stories

* a user can register and log in to start using the application
* a user is able to create aprofile containing information like their neighbourhood
* a user can join and leave a neighbourhood of their choice
* a user can post their business or make posts in their neighbourhood
* user can see the businesses and posts from their neighbourhood
* a user can view details of any neighbourhood

## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/Angelamutyota/intheloop.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Picture-Globe pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations neighbourhoodapp 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
``` 
##### Creating a super user
 ```bash
 python manage.py createsuperuser
 ``` 

##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8]
* [Django3.2.5] 
* [Heroku]  
  
## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug


## License
* *MIT License:*
* Copyright (c) 2021 **Angela Mbithe**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.