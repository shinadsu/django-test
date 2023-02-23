# django-test

1.  Install Python
Django is a Python web framework, thus requiring Python to be installed on your machine. At the time of writing, Python 3.8 is the latest version.

To install Python on your machine go to https://www.python.org/downloads/. The website should offer you a download button for the latest Python version. Download the executable installer and run it. Check the boxes next to “Install launcher for all users (recommended)” then click “Install Now”.

After installation, open the command prompt and check that the Python version matches the version you installed by executing:

...\> py --version


2. Setting up a virtual environment¶
It is best practice to provide a dedicated environment for each Django project you create. There are many options to manage environments and packages within the Python ecosystem, some of which are recommended in the Python documentation. Python itself comes with venv for managing environments which we will use for this guide.

To create a virtual environment for your project, open a new command prompt, navigate to the folder where you want to create your project and then enter the following:

...\> py -m venv project-name
This will create a folder called ‘project-name’ if it does not already exist and set up the virtual environment. To activate the environment, run:

...\> project-name\Scripts\activate.bat
The virtual environment will be activated and you’ll see “(project-name)” next to the command prompt to designate that. Each time you start a new command prompt, you’ll need to activate the environment again.

3. Than you need to activate all requirements from  {requirements.txt}
use pip install requiremets.txt in your terminal to  install all necessary modules

4. Then you have to go to the main catologist where the file {manage.py} is stored to enable the local server. 
python manage.py runserver
