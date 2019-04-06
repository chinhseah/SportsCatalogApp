# SportsCatalogApp
## Description
Udacity Full Stack Web Developer Project to build an app for maintaining items for different sport categories with a backend database using sqlLite.

## Setup 
1. Install Git Bash if running Windows OS
2. Install VirtualBox

   Note: Currently (October 2017), the version of VirtualBox you should install is 5.1. Newer versions are not yet compatible with Vagrant.
   
3. Vagrant

   * After set up use 'vagrant up' to start up
   * Then 'vagrant ssh' to log in to your terminal and virtual machine, and you'll get a Linux shell prompt.
   * Change directory to catalog folder using 'cd vagrant\catalog'
   
4. Database setup

   * At Linux shell prompt, within catalog folder, run 'python model.py'
   * Populate database with sport categories, etc. using 'python data_setup.py'
   
5. Run web server

   At Linux shell prompt run 'python application.py'
   
6. Run app

  * Open web browser and use web address localhost:8000
  * Login using your Google account
  
## Usage
Home Screen: 'localhost:8000'
![Catalog App](https://github.com/chinhseah/SportsCatalogApp/blob/master/vagrant/catalog/images/Catalog%20App.png)

Category Items: 'localhost:8000/catalog/Snowboarding/items'
![Catalog App Category Items](https://github.com/chinhseah/SportsCatalogApp/blob/master/vagrant/catalog/images/Catalog%20App%20-%20Category%20Items.png)

New Item Screen: 'localhost:8000/catalog/new'
![Catalog App New Item](https://github.com/chinhseah/SportsCatalogApp/blob/master/vagrant/catalog/images/Catalog%20App%20-%20New%20Item.png)

Item Description: 'localhost:8000/catalog/Snowboarding/Stretchy%20Pants'
![Catalog App Item Details](https://github.com/chinhseah/SportsCatalogApp/blob/master/vagrant/catalog/images/Catalog%20App%20-%20Item%20Details.png)

### API End Points
1. localhost:8000/catalog.json
2. localhost:8000/categories.json
3. localhost:8000/5/items.json - where 5 is category identifier

## Dependencies
Below is also listed in requirements.txt. 
   **Use pip install  -r  requirements.txt**
* Python 3
* VirtualBox 5.1
* Vagrant 2.2.4
* Flask 1.0.2
* Flask-HTTPAuth 3.2.4
* Flask-SQLAlchemy 2.3.2
* google-api-python-client 1.7.8
* google-auth 1.6.3
* google-auth-httplib2 0.0.3
* httplib2 0.12.1
* Jinja2 2.10
* oauth2client 4.1.3
* requests 2.21.0
* SQLAlchemy 1.3.1
