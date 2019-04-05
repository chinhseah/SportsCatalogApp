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
  
7. End points to get JSON data are:

## Dependencies
* Python 2.7
* VirtualBox 5.1
* Vagrant
* sqlLite
* sqlAlchemy
* Flask