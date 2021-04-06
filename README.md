# FlaskSite
Repository of my website on Flask

## Run environnement python to run Website
### Create an environnement
If you want to create an environnement you need to use Python.
In the folder of your project, you can create an environnment like this:
```
python3 -m venv venv
```
The second argument is the folder's name
### Activate your environnement
After to create your environnement, you need to activate it.
For this, you use this command:
```
. venv/bin/activate
```
venv is folder's name defined beyond this section.
## Launch your webServer !
To launch the server you need to export 2 global variables to Flask:
```
export FLASK_APP=project
export FLASK_ENV=development
```
The first one is the folder's name where all your project is.
The second one is the mod that you want launch. We are in devolpment so we can see all reports features form the bugs or problems.
