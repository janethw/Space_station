# Quick Catch-up
### README to capture reference material, development plans, and a journal of progress, things tried and ideas to try 
out.

## Project Planning. 
GitHub projects used for project planning. Link: 
[Space_station_project_plan](https://github.com/users/janethw/projects/1)

## References:
All references saved into local bookmarks.
Relevant headings: 
- Flask
- OOP
- Logging

# Design

## Flask
The Flask framework is used for building server-side applications and uses the Web Server Gateway Interface 
(pronounced 'Whiskey') toolkit. This interface is commonly used between web servers and web application.

Space_station is a Flask web app, with a MySQL database. Intent is to use Flask Blueprints and a standard
Model-View-Controller, MVC, architecture.

## __init__.py
When you have a number of Python files that you want to treat as a package, you can drop in a __init__.py file and
Python will recognize that directory as a package. Even an empty __init__.py file is sufficient - it the package's 
way of saying, "I'm ready to be used". When the code is run, Python automatically looks for the __init__.py and treats
the directory as a package. Think of it as the blueprint for your package. It means that any file outside the directory
can import the greetings module and use the functions within it. 

Article on Why use __init__.py is here: 
https://sarangsurve.medium.com/python-basics-why-use-init-py-c88589e44c91#:~:text=__init__.py%20allows,foundation%20for%20your%20packages'%20functionality.

## Config file
Configuration handling in Flask is explained here: 
https://flask.palletsprojects.com/en/3.0.x/config/

Flask is designed to normally require the config to be available at startup (eg toggling of debug mode, setting secret
key, other environment specifications). Flask has a config object that can hold the loaded configuration values; this 
is the config attribute of the Flask object

## Logging