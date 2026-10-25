# Python Server

## Project Information

- Project: Python Lab 1 - Webserver
- Name: Carlos Gutierrez
- Email: cgutierrez44833@ucumberlands.edu
- Course: MSCS-631-B01 Advanced Computer Networks

This is a small server to understand how the server works on python, to serve a
simple html page.

## Usage

The project is working with `python 3.15.0` If there is issues because of the
python versions on you enviroment, run the commands:

```sh
python3 -m venv .venv
sourc .venv/bin/activate
```

Run these commands from the repository root. Start the server first in one
terminal; it listens on the fixed port `5005` and must remain running:

```sh
python src/server.py
```

In a second terminal, request a file using the positional arguments `host port 
filename`:

```sh
python src/client.py localhost 5005  helloWorld.html
```

The requested file must be available relative to the server process's working
directory.

if you are requesting a page is not on the project, a 404 page will be returned.

### Notes

you dont need to run the `client.py`, only open any browser and type:

```
http://localhost:5005/helloWorld.html
```
