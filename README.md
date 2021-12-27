# Video Site
![image](https://user-images.githubusercontent.com/42610577/147454332-cfa39d3b-02c8-4f07-a584-5b8442bc0edb.png)[Video Site - View The Live Deployed Website](https://ms3-videosite.herokuapp.com/)

# Table of Contents
- [Video Site](#video-site)
- [Table of Contents](#table-of-contents)
  * [Author](#author)
  * [Project Overview](#project-overview)
  * [HOW TO USE](#how-to-use)
    + [Unauthenticated User](#unauthenticated-user)
    + [Standard User](#standard-user)
    + [Admin User](#admin-user)
  * [UX](#ux)
    + [Strategy](#strategy)
    + [Project Goals](#project-goals)
      - [User Goals](#user-goals)
      - [Developer Goals](#developer-goals)
      - [Website Owner Goals](#website-owner-goals)
    + [User Stories](#user-stories)
    + [Design Choices](#design-choices)
      - [Colors](#colors)
      - [Typography](#typography)
      - [Images](#images)
      - [Design Elements](#design-elements)
      - [Custom Javascript](#custom-javascript)
    + [Wireframes](#wireframes)
    + [Features](#features)
      - [Future Features](#future-features)
- [Information Architecture](#information-architecture)
  * [Database Choice](#database-choice)
    + [Data Models](#data-models)
- [Technologies Used](#technologies-used)
  * [Programming Languages](#programming-languages)
  * [Fonts](#fonts)
  * [Tools](#tools)
  * [APIs](#apis)
- [Defensive Programming](#defensive-programming)
    + [Access Controls](#access-controls)
    + [Permission Roles](#permission-roles)
  * [Testing](#testing)
    + [Penetration Testing](#penetration-testing)
      - [Testing Authenticated Routes](#testing-authenticated-routes)
      - [Result](#result)
      - [Testing Role Based Permissions](#testing-role-based-permissions)
      - [Result](#result-1)
    + [Validation Testing](#validation-testing)
    + [Cross Browser and Cross Device Testing](#cross-browser-and-cross-device-testing)
    + [Automated Testing](#automated-testing)
    + [Manual Testing](#manual-testing)
      - [1. Newsletter form:](#1-newsletter-form-)
        * [Results](#results)
      - [2. Contact form:](#2-contact-form-)
        * [Results](#results-1)
      - [3. Registration Page:](#3-registration-page-)
        * [Results](#results-2)
      - [4. Login Page:](#4-login-page-)
        * [Results](#results-3)
      - [5. Dashboard Page:](#5-dashboard-page-)
        * [Results](#results-4)
      - [6. Post Edit Functionality:](#6-post-edit-functionality-)
        * [Results](#results-5)
      - [7. Post Delete Functionality:](#7-post-delete-functionality-)
        * [Results](#results-6)
      - [8. Logout Functionality:](#8-logout-functionality-)
        * [Results](#results-7)
      - [9. Conditional Rendering:](#9-conditional-rendering-)
        * [Results](#results-8)
    + [Defect Tracking](#defect-tracking)
    + [Defects of Note](#defects-of-note)
  * [Deployment](#deployment)
    + [Deploy Locally](#deploy-locally)
    + [Deploy To Heroku](#deploy-to-heroku)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Acknowledgments](#acknowledgments)

## Author
Sam Mc Nally


## Project Overview
This site is design with a landing page for lead capturing as well as a user message board for authenticated users. Users can create an account, login, post messages on the message board, edit and delete this messages as well as being able to sign up for newsletter updates and sumbit queries through a contact form. 

## HOW TO USE
To use this website the steps are as follows.

- Step 1: Login users login by navigating to the "/login" route, if user does not have an account they can login by clicking the "Click here to register" link on the login form.\
- Step 2: Once logged in a a success message will flash to say that they have logged in.\
- Step 3: Admin ssers can create posts by filling this the create post form. .\
- Step 4: Admin uers can edit or delete their posts by cicking on the edit or delete buttons that show up on in the videos section of the Admin dashbaord.\

### Unauthenticated User
Unauthenticated Users can access the landing page, login page and registration page.

- A login admin Flask decorator is used to check that if the session object does not contain the property of logged in and or admin, the user will be redirected to a login page.

``` #Login Required Decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash("You must be logged in to access", "bg-red-400")
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

#Admin Required Decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session['user']:
            flash("You must be an admon in to access", "bg-red-400")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function
```

### Standard User
- A standard user can acces the site content

### Admin User
- An Admin user can create, update and delete content on the site
- 
## UX
As this is a CRUD based application the key UX features for this site are clear and defined input for accessability. Examples of this can be seen on the edit and delete buttons for posts.\

### Strategy
The strategy behind this website is to use of for a video display websie.

### Project Goals
The goal of this project is to deliver a simple, user friendly and intuitive application that allows user to create, read, update and delete video postings.

#### User Goals
As a user I want to have a clear and intuitive experience through out the application with consisten visual feedback in the form of flashed messages as I interact with the website.

#### Developer Goals
As a developer I aim to produce an CRUD application with User Authentication as well as a defensive programming design strategy to ensure that user's data is protected.

#### Website Owner Goals
As a product owner I aim to have a piece of software that is built with clean foundational architecture that provides for the ability to add more directly monetisable features like premium membership content a payment integrations into the site in the near future.


### User Stories
As a User I want to be able to access video content in a clear and structured manner.


### Design Choices
The most prominent design choices in this application are to be found in the visual feedback of the alert messages with Green being used for success messages, Yellow for standard operations like post editing and Red for error messages.


#### Colors
The colours used in this project are simple Greys and Black for structual elements of the pages and Green, Yellow and Red for visual feedback in the alert messages depening on the nature of the interaction.

#### Typography
The typography used is Helvetica.

#### Images
The images used are all relating to the activities of the company. They are mostly high quality JPEGs.

#### Custom Javascript
There is a timeout function on the alert messages so that the dissapear after 5 seconds.
``` 
<script>
  window.setTimeout(
    "document.getElementById('alert').style.display='none';",
    5000
  );
</script>
 ```

### Wireframes

I built full mobile and desktop mockups using Adobe XD.\
![image](https://user-images.githubusercontent.com/42610577/147460634-b7cb6d72-a7f5-47a9-96ba-cfd17e29f6f2.png)


#### Future Features

In the future I want to integrate payment for premium membership options.


# Information Architecture

## Database Choice
MongoDB Atlas was user for both production and local development.

PyMongo was used to connect to the MongoDB database.

```
# Database
client = pymongo.MongoClient(os.environ.get("MONGO_URI"))
db = client[str(os.environ.get("DB_NAME"))] 
```

### Data Models
The two data models are User and Post

User:
``` 
user = {
        "_id": uuid.uuid4().hex,
        "name": form.name.data,
        "email": form.email.data,
        "password": form.password.data,
        "admin:": true
        }
```

Post:
``` 
post = {
            "_id": uuid.uuid4().hex,
            "created_at": datetime.now(),
            "title": form.title.data,
            "description": form.description.data,
            "url": form.url.data,
            "thumbnail": set_thumbnail(form.url.data),
            "category": form.category.data,
            "difficulty": form.difficulty.data,
            "section": form.section.data
        }
```

The models inputs are validated through WTForms.

# Technologies Used

- A variety of different technologies were user:
  - [Tailwind CSS](https://tailwindcss.com/) - A utility first CSS Framework
  - [Alpine JS](https://alpinejs.dev/) - A lightweight Javascript Framework
  - [MongoDB](https://www.mongodb.com/cloud/atlas)- a fully-managed cloud database used to store manage and query data sets
  

## Programming Languages

- [CSS3](https://www.w3schools.com/w3css/default.asp) - used to style DOM appearance. 
- [HTML5](https://www.w3schools.com/html/default.asp) -  used to define DOM elements. 
- [JavaScript](https://www.javascript.com/)  -  used to help handle challenge member entry.
- [Python](https://www.python.org/) the project back-end functions are written using Python. Django and Python is used to build route functions.
- [Flask](https://flask-doc.readthedocs.io/en/latest/) - python based templating language
- [Markdown](https://www.markdownguide.org/) Documentation within the readme was generated using markdown

## Fonts
 - [Helvtica](https://fonts.google.com/?query=helvetica)

## Tools
 - [Adobe XD](https://www.adobe.com/ie/products/xd.html)
 - [VS Code](https://code.visualstudio.com/)

## APIs
 - [Vimeo](https://developer.vimeo.com/)


# Defensive Programming
The app is built with defensive programming in mind.

Some of the key features are built for access controls and permission roles.

### Access Controls
Unauthenticated Users can access the landing page, login page and registration page. The site is built with access controls to stop non admin users from accessing the admin dashboard as well as posting, post editing and post deleting functionality.
- A login Flask decorator is used to check that if the session object does not contain the property of logged in, the user will be redirected to a login page.

``` #Login Required Decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash("You must be logged in to access", "bg-red-400")
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

#Admin Required Decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session['user']:
            flash("You must be an admon in to access", "bg-red-400")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function
```

## Testing

### Penetration Testing
Baic penetration testing was done to ensure that unauthenticated users can't access authenticated content and that permissionless users can't edit role based permission functions.

#### Testing Authenticated Routes
    1. Without logging in attempt to access the url "/admin/video/"
    2. Using Postman try to send a POST request to the endpoint "/videos/post/"
    3. Try to access the route "/posts/edit/<id of any post>"
    
#### Result
User is redirected to the login page with the dashboard url set as the value of the "next" paramater in the current url - ***passed*** \
A response telling the user the log in is returned - ***passed*** \
A response telling the user the log in is returned - ***passed*** 

#### Testing Role Based Permissions
    1. Using the post ID of a post not owned the current non admin user by try to access "/posts/edit/<id of post not owned by current user>"
    2. Using the post ID of a post not owned the current non admin user by try to access "/posts/delete/<id of post not owned by current user>"
  
#### Result
User is redirected to Index and message saying permission denied is displayed - ***passed*** \
User is redirected to Index and message saying permission denied is displayed - ***passed*** 

### Validation Testing

- [CSS Validator](https://jigsaw.w3.org/css-validator/) 
- [HTML Validator](https://validator.w3.org/) Note, because Alpine JS manipulate html element by placing aditional attributes on them such as "x-data" or ":class", there are returned as errors by the validator.
- [PEP8 Validator](https://www.pythonchecker.com/)

### Cross Browser and Cross Device Testing

| TOOL / Device                 | BROWSER     | OS         | SCREEN WIDTH  |
|-------------------------------|-------------|------------|---------------|
| real phone: iPhone 6          | chrome      | iOs        | XS 360 x 640  |
| dev tools emulator: iPhone5s  | chrome      | iOs        | XS 320 x 568  |
| dev tools emulator: pixel 2   | chrome      | android    | SM 411 x 731  |
| dev tools emulator: iPhone 8  | chrome      | iOs        | SM 411 x 731  |
| dev tools emulator: iPad      | chrome      | iOs        | MD 768 x 1024 |
| dev tools emulator: Surface   | chrome      | android    | MD 540 x 720  |
| dev tools emulator: iPad Pro  | chrome      | iOs        | LG 1024 x 1366|
| real computer: mac book pro   | safari      | Catalina   | XL 1400 x 766 |
| real computer: mac book pro   | chrome      | Catalina   | XL 1400 x 766 |

### Automated Testing
Due to the fact that there are only two data models and a relatively simple frontend, I did not find situations where automated testing such as integration testing was neccessary as the the app is generally not complex enough to have majorly conflicitng elements or many change breaking features.

### Manual Testing
Much of the app has been tested manually as follows:


#### 1. Registration Page:
    1. Go to the Registration page.
    2. Try to submit the empty form and verify that an error message about the required fields appears.
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears.
    4. Try to submit form with mismatched passwords and verify mismatched password message.
    5. Try to submit the form with all inputs valid and verify that a success message appears.

##### Results
* Registration Page loads - ***passed***
* Form return visual feedback for required fields - ***passed***
* Form requests email address with '@' sybmol be entered - ***passed***
* Form returns message that passowords do not match - ***passed***
* From returns success message and logs user in - ***passed***

#### 2. Login Page:
    1. Go to the Login page.
    2. Try to submit the empty form and verify that an error message about the required fields appears.
    4. Try to submit form with invalid credentials and verify error shows.
    5. Try to submit the form with all inputs valid and verify that a success message appears.

##### Results
* Login Page loads - ***passed***
* Form return visual feedback for required fields - ***passed***
* Message is displayed that credentials are invalid - ***passed***
* Form returns success message - ***passed***

#### 3. Admin Dashboard Page:
    1. Go to Admin Dashboard.
    2. Try to submit the empty form and verify that an error message about the required fields appears.
    3. Try to Edit a post and verify you are directed to the edit page with the correct post.
    4. Try to Delete a post.

##### Results
* Dashboard Page loads - ***passed***
* Form return visual feedback for required fields - ***passed***
* Button brings you to the edit page with the post content prefilled in the form - ***passed***
* Form returns success message that post was deleted - ***passed***

#### 6. Post Edit Functionality:
    1. Go to the Post Edit page.
    2. Try to submit the empty form and verify that an error message about the required fields appears.
    3. Try to submit the form with too many characters that a relevant error message appears.
    5. Try to submit the form with all inputs valid and verify that a success message appears.

##### Results
* Post Edit Loads - ***passed***
* Form return visual feedback for required fields - ***passed***
* Form requests message saying character limit is 180 charaters - ***passed***
* Form returns success message - ***passed***

#### 7. Post Delete Functionality:
    1. Go to the Dashboard page.
    2. Try to Delete a post

##### Results
* Dashboard Page loads - ***passed***
* Page returns message stating that post was deleted - ***passed***

#### 8. Logout Functionality:
    1. Click logout button.
  
##### Results
* User is redirected to index page and is logged out - ***passed***

#### 9. Conditional Rendering:
    1. As an unauthenitaced user check that navbar only displays Log In Button.
    2. As an authenitaced user check that navbar  displays Dashboard and Log Out Button.
    3. Only an Admin can see Edit and Delete buttons on the Admin dashboard
 
##### Results
* Log In Button appears in navbar but not Dashboard or Log Out Buttons - ***passed***
* Dashboard and Log Out Buttons appears in navbar but not Log In Button - ***passed***
* Admin can only access Edit and Delete buttons for Admin Dashboard - ***passed***

### Defect Tracking

### Defects of Note
The absolute position of the image on index, form on login and register can overlap the div below if the screen height is very small or push by other browser elements on mobile.

## Deployment

### Deploy Locally

To deploy locally:

1. In the terminal run the command
``` 
git clone https://github.com/slammer1870/ms3-videosite.git 
```
2. In the root directory create your virtual environment and run
```
pip install -r requirements.txt
```
3. Create a .env file with the environemnt variables:\
> |        Variable       	|   Setting  	|
>|:---------------------:	|:----------:	|
>| MONGO_URI                | YOUR_KEY   	|
>| DB_NAME            	    | YOUR_KEY   	|
>| SECRET_KEY        	    | YOUR_KEY   	|

4. Run
```
python app.py
```

### Deploy To Heroku
To deploy to Heroku:

1. In the terminal run the command
``` 
git clone https://github.com/slammer1870/ms3-videosite.git 
```
2. Login to Heroku and set up a new app
3. Under the Settings tab, click Reveal Config Vars
4. Set the config variables to be:
> |        Variable       	|   Setting  	|
>|:---------------------:	|:----------:	|
>| MONGO_URI                | YOUR_KEY   	|
>| DB_NAME            	    | YOUR_KEY   	|
>| SECRET_KEY        	    | YOUR_KEY   	|

5. Log in to Heroku, you can do this by running
```
heroku login
```
6. Clone the heroku repository
```
heroku git:clone -a 'your_app_name'
```
7. Add your files, commit and push to Heorku main:
```bash
$ git add .
$ git commit -am "initial heroku commit" 
$ git push heroku main
```

## Credits
The footer component was bootstrapped from [tailblocks.cc](https://tailblocks.cc/)

### Content
All of the copy on the website is written by me

### Media
All of the media is owned by ExecBJJ Ltd.

### Acknowledgments
I'd like to thank my mentor Malia for helping me!
