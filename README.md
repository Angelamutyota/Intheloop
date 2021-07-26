# RateMySite

## Author  
  
>[Angela-Mutyota] 

##  Live Link 
 Click ()  to visit the site
  
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
  
  