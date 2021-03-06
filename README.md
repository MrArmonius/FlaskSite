# FlaskSite
Repository of my website on Flask

The default user is:
email: a@be
password: a

The function to register works well.

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
The second one is the mod that you want launch. We are in development so we can see all reports features from the bugs or problems.
Now we need to launch the webserver.
```
flask run
```
## Connect to your webSite
You can use any web browser.
The address IP is your localhost and the port is 5000. The option `--host=0.0.0.0` allows all ip adress in your LAN to have an acces on your webserver.
You can connect at your WebServer via a browser with this address: `https://{local address IP of your webserver}:5000`
```
flask run
```
So for example, you need to write on your web browser this address:
```
https://127.0.0.1:5000/
```
If you wish to change port, there are 2 differents way to do it.
The first is the easy one, you just need to launch flask like this
```
flask run -h localhost -p 4999
```
The second is more reliable because you need to change \_init_app() and indicate the port with this line:
```python
from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
```

## Open your dev at your network

Dev server flask isn't secure, so don't open it at the world. Only private network wellknown from you.
You need to use the option `--host=0.0.0.0`, `0.0.0.0` is a special value which allows all computers on your network to accede at your server.
So when you launch Flask:
```
flask run --host=0.0.0.0
```
