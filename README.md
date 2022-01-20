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
- [x] Array or List  
- [x] Loop  
- [x] Method  
- [x] Class  
- [x] Interface  
- [x] Encapsulation   
- [x] Abstraction  
- [ ] Comment  
- [x] Inheritance  
- [x] Polymorphism


## Plan
- [x] Create a basic architecture without external components (eg. Database)  
- [x] Create the business logic without external components  
- [x] Integrate with external components
- [x] Create the GUI

## For running tests and show coverage

````shell
# Install dependencies
python3 -m pip install -r requirements.txt
# Run tests using mongo datasource (73% coverage)
DATASOURCE=MONGO pytest --cov=media_library --cov-report term-missing tests/
# Run tests using in-memory datasource (81% coverage)
DATASOURCE=INMEMORY pytest --cov=media_library --cov-report term-missing tests/
````

## For running the GUI

````shell
python3 -m media_library.ports.gui
# go to  http://127.0.0.1:5000/
````
