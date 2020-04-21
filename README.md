## What is it?

This is an example App template for the outstanding REMI GUI framework created by Davide Rosa.

[REMI Website](https://www.remigui.com "REMI Homepage")

[REMI Github Repository](https://github.com/dddomodossola/remi "REMI Github Repository")

[REMI Documentation](https://remi.readthedocs.io/en/latest/)

[REMI Reddit Support Group](https://www.reddit.com/r/Python/comments/3rbvus/remi_gui_library_for_python/)

[REMI Gitter Chat Room](https://gitter.im/dddomodossola/remi#)

## See it in action

[REMI-App-Template running on 1 Core 512 MB RAM Ubuntu VServer](http://remi.kueken.de)


## Why making an App Template?

While REMI itself is great and the usage is very straight forward many users may find it a little hard to get
into it. Users are asking very often how to make a WebUI with different Views. That's where this repo comes in.

Furthermore in the Gitter Chat there are frequent questions about problem solutions and from time to time
the solution can easily be put into this repo in order to not forget about the solution.


## Getting started

Just clone the repo with 

`git clone https://github.com/cheak1974/remi-app-template.git`

If you want a completely empty App template without the example Views and example Models etc.
we hold a special branch which is called "empty" for you. Just clone the repo with the following command:

`git clone -b empty https://github.com/cheak1974/remi-app-template.git`

Change to the project folder 

`cd app-template-for-remi`

Install a virtual Environment inside the project folder 

`python -m venv .\venv`

If you don't have installed VirtualEnvironment on your Workstation you can do:

`pip install virtualenv`

Change to the Script folder of the virtual Environment 

`cd venv` 

`cd Scripts`

Activate the virtual Environment with `activate` (Linux) or `activate.bat` (Windows).  
Go back to the project's root folder with:

`cd ..`
`cd ..`

Then install the needed libraries with 

`pip install -r requirements.txt`

Start up the App with `python AppTemplate.py` file in the project's root.
The App should startup and open a local browser window with the Apps start page.


## Structure of the App Template

|Subfolder      | Content          |
|---------------|------------------|
|`config`       | Contains config.py which will be imported. Your project configuration lives here. `config/config.py` overwrites the default values in `core/globals.py` |
|`core`         | Contains the main program `webapp.py` and the `webapi.py` alongside with the global Dictionaries in `globals.py` for project wide data access.|
|`dialogs`      | You can create your own dialogs. These files go here.|
|`helpers`      | Code that fits nowhere else can be placed in helpers folder.|
|`models`       | If your views need data structures they can be placed here to follow the MVC paradigm.|
|`sslkeys`      | If you want Remi to work with SSL/TLS place your certificate and key files here.|
|`static`       | Static content like JS, CSS and binaries like Images, Videos etc.|
|`views`        | The views of your application.|
|`widgets`      | You can create custom Widgets too. These files should be placed here.|


## App Startup Process

It is important to understand, what happens when the App starts.

- `AppTemplate.py` does not much. It just calls the `startApp` method in `core/webapp.py`. You could easily
put the entire App in a subfolder of others of your projects to add a GUI to it. Just start the `startApp`
method as new Thread and it will run parallel to your normal App.
- When `webapp.py` is executed it it imports the default configuration `core/globals.py` and afterwards
the user configuration `config/config.py`. Basically there two Dictionaries created. The `core.globals.config`
Dictionary is for Configuration Data for the App. The `core.globals.UserData` is meant to store instances of
models that you need for your App and views. Of course you can organize things in a different way if you like.
- When a user connects REMI spawns a new App Instance of `WebApp` class.
- The main method of the webapp class creates some Containers, loads the Views in folder `views` dynamically
and imports the NavBar which creates the Menu Entries automatically. `views/start.py` will be set there as
the initial View of the App.
- The main method returns the Base Container which is crucial for REMI.


## Using REMIs graphical UI Editor to create Views easily

...
