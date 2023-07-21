# divar
Divar / Craigslist clone with django 4.2
this is a minimal django clone of divar / craigslist site

## authentication 🔐
a custom user model has been used 

users can login with google or github

when a new user signup a wellcome email is sent using signals

user email verifucation is optional

users can reset-password, change email and etc.

2 step verification is optional

## how does it work 🤔
first users should choose city and province and it will be saved in cache for 2h

Users can add advertisments and do  CRUD on them

only advertisment author can update or delete the advertisments

some pages are cached with **Redis**

User can Bookmark advertisments and see them in profile

author of a advertisment can promote it via purchasing a package

### user Profile
user can see the contact info in profile

 Bookmarked advertisement are visible in profile

 all the posted adv are showen in profile 

 users can see all the transactions and mange them in transaction management

 ### transactions
 unpaid or pending transactions can be paid in transaction management

 you can filter and search the transactions with provided filters 

 ### Advertisments

 filter and search for advertisments are available

 advertisment have images

 in advertisment list you can see title and image then you havo to click on it to see details

 in advertisment detail you see contact info and other informaitions

 you can bookmark advertisment in the detail view

 if user is the author of advertisment

 the Update / Delete / Promote will be showen

 

## How to use
1) create a psql DB and a local_cnf.py file
2) add your data base info to local_cnf.py
3) then run migrations

        python manage.py migrate

4) create a super user and login 





 
