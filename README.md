# Peach House - Web application
Peach House is a personal web application developed using Django Rest framework which allows customers to book table using API's and also render sample HTML content
## Tech Stack
* Python
* Django
* Django Rest Framework
* HTML
* CSS
* Javascript (Vanilla)

## Project Requirement
Building the fullstack web application for a imaginary restaurant* "`Peach House`"

### The Web application should consist of the following
* Complete functioning web application
    * Header
        * Home
        * Menu
        * Book
        * About
    * Footer
## Project Structure
* Project folder: PeachHouseProject
    * urls.py
    * settings.py
> `Note: above mentioned are the part of those files which had changes included as part of the project`
* Project App: PeachHouseApp
    * urls.py
    * settings.py
    * views.py
    * models.py
    * templates
    * static
> `Note: above mentioned are the part of those files which had changes included as part of the app`

## Functional Design
* `Header` and `Footer` should get displayed on all the pages of the application
> ### Header
> > Header page consists of the following components
> > * Home page:
> > * * Displays the Hero section with Chef's special dishe url
> > * * Displays thumbnail of Signature dish with information related to restaurant's Menu with a navigation link
> > * * Displays thumbnail of a dish's image which provides an option to book table
> > * * Displays the restaurant's working hours
> > * About page:
> > * * Not developed
> > * Menu page:
> > * * Not developed
> > * Book Page:
> > * * Not developed
> ### Footer
> > Footer page consists of the following components
> > * Copy right information

# Technical Design
### Libraries
> Python V3.12.3

> > Pipenv (virtual environment)

> >  Djoser V 2.2.3

> >  Django V5.0.7
> >   * Djangorestframework V3.15.2

> >  mysqlclient V 2.2.4

### Database:
> MySQL

## Code Flow:
### Processing Logic:
* Following outlines the code and functionality of web application and api

<table>
  <tr>
    <td><h2>Use Case</h2></td>
    <td><h2>Details</h2></td>
    <td><h2>Screenshot</h2></td>
  </tr>
  <tr>
    <td>1</td>
    <td>Does the web application use Django to serve static HTML content?</td>
    <td>HTML of Home page is developed to show that template is getting rendered</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-FullStack/blob/34ff70b61d483cb5ad0f4aac0d1f7d276bbaefbb/Snapshots/settings.JPG"/></td>
  </tr>
  <tr>
    <td>2</td>
    <td>Has the learner committed the project to a Git repository?</td>
    <td>Project details are in Git hub <a href="https://github.com/vish4life/PeachHouse-Fullstack">GitHub</a></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-FullStack/blob/34ff70b61d483cb5ad0f4aac0d1f7d276bbaefbb/Snapshots/dbsettings.JPG"/></td>
  </tr>
  <tr>
    <td>3</td>
    <td>Does the application connect the backend to a MySQL database?</td>
    <td>Yes, database configuration to MySQL is setup</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-FullStack/blob/34ff70b61d483cb5ad0f4aac0d1f7d276bbaefbb/Snapshots/migrations.JPG"/></td>
  </tr>
  <tr>
    <td>4</td>
    <td>Are the menu and table booking APIs implemented?</td>
    <td>Class based and Function based views are coded to implement the API's</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-FullStack/blob/34ff70b61d483cb5ad0f4aac0d1f7d276bbaefbb/Snapshots/booking1.JPG"/></td>
  </tr>
  <tr>
    <td>5</td>
    <td>Is the application set up with user registration and authentication?</td>
    <td>Djoser library is used for authentication</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-FullStack/blob/34ff70b61d483cb5ad0f4aac0d1f7d276bbaefbb/Snapshots/dateselector.JPG"/></td>
  </tr>
  <tr>
    <td>6</td>
    <td>Does the application contain unit tests?</td>
    <td>Yes two unit test cases are written one for each api model</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-FullStack/blob/34ff70b61d483cb5ad0f4aac0d1f7d276bbaefbb/Snapshots/allreservations.JPG"/></td>
  </tr>
  <tr>
    <td>7</td>
    <td>Can the Booking API be tested with the Insomnia REST client?</td>
    <td>Yes</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-FullStack/blob/34ff70b61d483cb5ad0f4aac0d1f7d276bbaefbb/Snapshots/noduplicate.JPG"/></td>
  </tr>
  <tr>
    <td>8</td>
    <td>Can the Menu API be tested with the Insomnia REST client?</td>
    <td>Yes</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-FullStack/blob/34ff70b61d483cb5ad0f4aac0d1f7d276bbaefbb/Snapshots/datechangerefresh.JPG"/></td>
  </tr>
</table>

`Note 01: Project name: PeachHouseProject and App name: PeachHouseApp`

`Note 02: Templates provided as the base code needs enhancement to correctly function`