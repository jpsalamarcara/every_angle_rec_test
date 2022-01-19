# every_angle_rec_test

## Requirements

1. Build an application to allow users to curate their own media libraries.  
2. The users should be able to:  
Add, edit and remove media items   
Categorise media items  
View media items  
3. Must have a GUI or Web UI.  
4. Persistent storage is a must.  
5. Media types include:  
Movies   
Games  
Music  

## Required Techniques

At least one example or equivalent of each of the below: 
[x] Array or List  
[x] Loop  
[x] Method  
[x] Class  
[x] Interface  
[x] Encapsulation   
[x] Abstraction  
[-] Comment  
[x] Inheritance  
[-] Polymorphism


## Plan
1. Create a basic architecture without external components (eg. Database) [x] 
2. Create the business logic without external components [x] 
3. Integrate with external components [-] 
4. Create the GUI [-] 

## For running tests and show coverage

````shell
python3 -m pip install -r requirements.txt
pytest --cov=media_library --cov-report term-missing tests/
````