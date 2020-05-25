[![Build Status](https://travis-ci.org/3PU/2nd-paw.svg?branch=master)](https://travis-ci.org/3PU/2nd-paw)

# 2ndPaw

<br/>

## Table Of Contents

- General Information
- Demo
- Website Structure
- Wireframe Mockups
- Technologies
- UI
- UX
- Database
- Accessibility
- Challenges
- Features
- Defensive Design
- Testing
- Deployment
- Credits

<br/>

## General Information

### Code Institute Coding Bootcamp - Full Stack Frameworks with Django Milestone Project

This is my fourth milestone project created during my coding bootcamp at Code Institute.

The idea behind 2nd Paws is to support local cat & dog shelters by providing pet owners with online meeting portal to donate/exchange pet clothes, toys and supplies that they no longer need/use.

All profits generated on the 2nd Paws website go directly to the cat and dog shelters in Stockholm, supporting their fantastic work.

Visitors to the website are also presented with the option to make monetary donations that directly are forwarded to the cat and dog shelters that 2nd Paw's supports.

<br/>

## Demo

A live demo of the website can be found [here](https://codei-2nd-paws.herokuapp.com/).

<br/>

## Website Structure

<img src="https://github.com/3PU/2nd-paw/blob/master/wireframes/2nd_paw_website_structure.png" alt="Website Structure" style="width: 200px;"/>

## Wireframe Mockups

The wireframe mockups below have been created with [MockFlow](https://mockflow.com/) to illustrate the initial structure and idea for each page prior to production.

| Large Screens | Small Screens |
|--------------|--------------|
| ![Index - Large](https://github.com/3PU/2nd-paw/blob/master/wireframes/large_screens/2nd_paw_index_large_screen.png) | ![Index- Small](https://github.com/3PU/2nd-paw/blob/master/wireframes/small_screens/2nd_paw_index_small_screen.png) |
| ![About - Large](https://github.com/3PU/2nd-paw/blob/master/wireframes/large_screens/2nd_paw_about_large_screen.png) | ![About- Small](https://github.com/3PU/2nd-paw/blob/master/wireframes/small_screens/2nd_paw_about_small_screen.png) |
| ![FAQ - Large](https://github.com/3PU/2nd-paw/blob/master/wireframes/large_screens/2nd_paw_faq_large_screen.png) | ![FAQ- Small](https://github.com/3PU/2nd-paw/blob/master/wireframes/small_screens/2nd_paw_faq_small_screen.png) |
| ![Contact - Large](https://github.com/3PU/2nd-paw/blob/master/wireframes/large_screens/2nd_paw_contact_large_screen.png) | ![Contact- Small](https://github.com/3PU/2nd-paw/blob/master/wireframes/small_screens/2nd_paw_contact_small_screen.png) |
| ![Donate Product - Large](https://github.com/3PU/2nd-paw/blob/master/wireframes/large_screens/2nd_paw_donate_product_large_screen.png) | ![Donate Product- Small](https://github.com/3PU/2nd-paw/blob/master/wireframes/small_screens/2nd_paw_donate_product_small_screen.png) |
| ![Products - Large](https://github.com/3PU/2nd-paw/blob/master/wireframes/large_screens/2nd_paw_all_products_large_screen.png) | ![Products Page](https://github.com/3PU/2nd-paw/blob/master/wireframes/small_screens/2nd_paw_all_products_small_screen.png) |
| ![Product Detail - Large](https://github.com/3PU/2nd-paw/blob/master/wireframes/large_screens/2nd_paw_product_detail_large_screen.png) | ![Product Detail- Small](https://github.com/3PU/2nd-paw/blob/master/wireframes/small_screens/2nd_paw_product_detail_small_screen.png) |
| ![Create Blogpost - Large](https://github.com/3PU/2nd-paw/blob/master/wireframes/large_screens/2nd_paw_create_blogpost_large_screen.png) | ![Create Blogpost - Small](https://github.com/3PU/2nd-paw/blob/master/wireframes/small_screens/2nd_paw_create_blogpost_small_screen.png) |
| ![Blogposts - Large](https://github.com/3PU/2nd-paw/blob/master/wireframes/large_screens/2nd_paw_blogposts_large_screen.png) | ![Blogposts - Small](https://github.com/3PU/2nd-paw/blob/master/wireframes/small_screens/2nd_paw_blogposts_small_screen.png) |
| ![Registration - Large](https://github.com/3PU/2nd-paw/blob/master/wireframes/large_screens/2nd_paw_registratin_large_screen.png) | ![Registration - Small](https://github.com/3PU/2nd-paw/blob/master/wireframes/small_screens/2nd_paw_registratin_small_screen.png) |
| ![Login - Large](https://github.com/3PU/2nd-paw/blob/master/wireframes/large_screens/2nd_paw_login_large_screen.png) | ![Login - Small](https://github.com/3PU/2nd-paw/blob/master/wireframes/small_screens/2nd_paw_login_small_screen.png) |

<br/>

## Technologies

### Languages

- HTML5
- CSS3
- Javascript
- Python3

### Libraries, Frameworks & Tools

- Django
- Bootstrap CSS 4.4.1
- Bootstrap JS 4.4.1
- FontAwesome 4.7.0
- jQuery 3.4.1
- Google FontAwesome
- Stripe
- Psycopg2
- Gunicorn
- Sweetify
- AWS S3 Bucket
- Boto3
- Pillow
- Google Images
- Mockflow

### Databases

- SQLite3
- PostgresSQL

### Hosting

- Github
- Heroku

<br/>

## UI

### Colors

The following colors are used throughout the project:

- #fffff (Text)
- #00000 (Text, shadows and elements with various degrees of opacity)
- #c2c3c3 (Elements)
- #a2a2a2 (Element hover)
- #585454 (Buttons, borders and accordion)

### Fonts

Only sans serif fonts were used throughout the project.

Initially I thought about using two fonts, but after implementing Google Fonts 'Ubuntu' I realized it looked very good by itself across the site.

Font family used throughout the project: 'Google Fonts Ubuntu'
Font weight: '400', '500' & '700'

### Icons

Only fontawesome icons have been used on the page.

Icons used throughout the project:

- Navbar: `fas fa-paw` & `fas fa-shopping-cart`
- About: `fas fa-paw`
- FAQ: `far far fa-comment-dots` & `fas fa-paw`
- Support Us: `fas fa-hand-holding-usd`

### Layout

The idex page is kept very clean, using only a background image that fills up the entire first page. I decided to place a chevron icon at the bottom
of the page to naturally provoke users to scroll down where they can find the 'About' page. If users decide to browse to the about section via
the navbar instead, the page will scroll down (smooth scroll on chrome browsers only).

The navbar should provide users with an intuitive way to engage with the website and I therefore did not feel the need to add descriptive text to the index page,
a choice that has proven to be effective via testing from multiple first-time users.

### Responsiveness

The website has been built with a mobile-first approach and is highly responsive.

This is primarily achieved by using bootstrap and custom-written css (for more details see testing section).

<br/>

## UX

The overall goal of the website is to provide visitors with the ability to donate pet products they no longer need or use
or buy pet products at a discounted price, and by that financially support the local cat and dog shelters.

Visitors can also choose to make monetary donations or create a blogpost showing how their pet liked a product purchased
through the website.

<br/>

## User Stories

- As a user, I want to learn more about the company behind the website.
- As a user, I want to be able to find/get answers to my questions.
- As a user, I want to be able to contact the company behind the website.
- As a user, I want to be able to register and sign up for a free account.
- As a user, I want to be able to login, logout and reset my password if need be.
- As a user, I want to be able to browse through the database of available donated products.
- As a user, I want to be able to search the database of available donated products.
- As a user, I want to be able to buy donated products using a credit card.
- As a user, I want to be able to donate products.
- As a user, I want to be able to make a monetary donation.
- As a user, I want to be able to browse through all user blogposts.
- As a user, I want to be able to create a blogpost and share my story with the visitors of the website.

<br/>

## Pages & Functionality

### About

This section is divided into three sub-sections using a drowdown menu:

- 'About 2nd Paw' takes the user to the applicable section on the index page.
- 'FAQ' takes the user to the frequently asked questions page which uses a boostrap accordeon style to keep the page small.
By clicking on a question, the answer is revealed and clicking on another question collapses the prior div and expands the
next applicable answer.
- 'Contact us' takes the user to a simple contact form.

All three sections are available to all users, logged in or not.

### Browse Shop

This section is divided into 6 different sub-sections using a dropdown menu:

- 'All Products' displays all donated products available in the database.
- 'Cat Products' only displays the donated products suitable for cats.
- 'Dog Products' only displays the donated products suitable for dogs.
- 'Clothes' only displays the donated pet clothing products.
- 'Toys' only displays the donated pet toys.
- 'Supplies' only displays the donated pet supplies products.

*Only one products templates is used to render the above pages, but a filter function displays the applicable products based
on the user selection.

Below each product that is displayed there is one 'read more' and one 'buy' button. The read more button takes the
user to the product detail page where a more detailed description of the product is provided. The buy button adds
the applicable product to the shopping cart.

All sections are avilable to all users, logged in or not, but non-logged in users cannot add products to the shopping cart.
If a user clicks on the 'buy' button, the user is redirected to the login page, where the user can choose to log in or
sign up for a free account.

If no products are available in the database a text is displayed telling the user that no products have been found.

### Blog

This section is divided into 2 different sub-sections using a drop-down menu:

- 'View all blog posts' (visible to all users) renders the blog post templates and displays all available blog posts.
- 'Create Blog Post' (only available to logged in users) renders the create a blog post template with a form so the user can
publish a blog post.

*Only authenticated users are allowed to publish blog posts and the dropdown menu becomes available once a user is logged in.
For non-authenticated users, instead a simple 'Blog' link is displayed in the navbar that takes the user to the blog posts templates.

### Donate

This section is divided into 2 different sub-sections using a dropdown-menu:

- 'Donate Product' takes the user to the product donation form. Only authenticated users are able to access this page though. If
a non-authenticated user clicks on this link, the user is redirected to the login page, where the user can choose to log in or
sign up for a free account.
- 'Support us' takes the user to the monetary donation page where the user can add a pre-defined donation amount to the
shopping cart and therafter go through the checkout process to make a monetary donation.

The 'support us' section is available to bot authenticated and non-authenticated users as I want to allow any user to make a monetary
donation. Having to go through a sign up or login process might put a visitor off from making a donation even though the visitor
initially intended to make a monetary donation, something I want to avoid.

### Register

This link is available for non-authenticated users only and disappears once a user is logged in.

Clicking on this link renders the registration template and registration form.

### Login

This link is available for non-authenticated users only and disappears once a user is logged in.

Clicking on this link renders the login template.

On this page the user can log in or continue to the password reset or registration page via the links below the login button.

### Logout

This link is available for authenticated users only and disappears once a user is logged in.

### Search

This search field searches through the product database based on the product titles. If the search did not
yield any results a text is displayed telling the user that no products have been found.

### Shopping cart

The shopping cart icon is only displayed if any products have been added to the shopping cart.

### Checkout

The checkout page is only available via the checkout button the shopping cart page.

<br/>

## Database

Development Database: SQLite3
Production Database: PostgresSQL

The following tables and values are stored in both the development and production database:

Both databases contain and store the following tables and values:

| Table | Value 1 | Value 2 | Value 3 | Value 4 | Value 5 | Value 6 | Value 7 |
|-------|---------|---------|---------|---------|---------|---------|---------|
| auth_user | username | email | first_name | last_name | `n/a` | `n/a` | `n/a` |
| blogpost | title | author | animal_name | content | published_date | image | `n/a` |
| product | title | category | animal | condition | description | price | image |

<br/>

## Accessibility

To increase accessibility of the website, ALT attributes have been added to all static images and hidden screenreader
utilities (sr-only) to the shopping cart icon.

<br/>

## Challenges

My overall experience when creating this application was smooth and straight forward once I had a good understanding of
all the concepts.

Two of the biggest challenges I encountered were related to the design and even though they were simplistic in nature,
they proved difficult to solve.

The first challenge was the footer which I wanted to stick to the bottom of the page at all times. Normally, this
is easy to solve, but since I used a fullscreen and fixed background image on the index page, fixating the footer
to the bottom of the page using `position:fixed` and `bottom:0` resulted in the footer sticking to the bottom of
the index background div instead of the bottom of the entire page height. Using `position:relative` made the footer
work on the index page, but instead left the footer floating in the middle of the page on all other pages, regardless
of the bottom-margin I uses. The way I solved this problem was to create two different footers, one relative and one
fixed. The relative footer is used on the index page and the relative footer is used on all other pages.

The second challenge was the actual background image on the index page. For some reason, when testing the website on
phones specifically, none of the phones used did scale the image, leaving it in its original size. To solve this,
I created a smaller version that replaces the larger image on screen sizes below 768px.

<br/>

## Mistakes

One uninentional mistake I made towards the end of the project was to accidentially upload the coverage html folder
to my github repository. The intention was to share the total coverage report and percentage of my automates tests,
but instead of only uploading the summary, the entire folder was uploaded.

Something that I was not aware of was that the html coverage report contained a copy of each file in the entire
application including files that were included in my `.gitignore` file. But I quickly noticed my mistake and deleted
the folder again. Unfortunately, the commit history still contains a copy of those files so I had to change all
the secret variables and keys after this incident to make sure no one could

<br/>>

## Features

### Feature Overview

- Users can learn more about the company behind the website.
- Users can find answers to the most commonly asked questions.
- Users can reach out and contact the company behind the website.
- Users can register and sign up for a free account.
- Users can login, logout and reset their password if need be.
- Users can browse through the database of available donated products.
- Users can search the database of available donated products.
- Users can buy donated products using a credit card.
- Users can donate products.
- Users can make monetary donations.
- Users can browse through all user blogposts.
- Users can create a blogpost and share their story with the visitors of the website.

### Feature 1 - Learn more about the company

**User story: "As a user, I want to learn more about the company behind the website."**

Users can learn more about the company by scrolling down to the about section on the
index page or by clicking on the 'About' -> 'About us' link in the navbar.

### Feature 2 - Find answers to the most commonly asked questions

**User story: "As a user, I want to be able to easily find/get answers to my questions."**

Users can find answers to the most commonly asked questions on the FAQ page by clicking
on the 'About' -> 'FAQ' link the navbar. If the users question is not answered via the
FAQ page, users can reach out to the company directly via the contact page by clicking
on the 'About' -> 'Contact us' link in the navbar and ask their question using the
contact form.

### Feature 3 - Contact the company

**User story: "As a user, I want to be able to contact the company behind the website."**

Users can reach out to the company directly via the contact page by clicking
on the 'About' -> 'Contact us' link in the navbar and ask their question using the
contact form.

### Feature 4 - Register and sign up for free account

**User story: "As a user, I want to be able to register and sign up for a free account."**

Users can register for a free account on the registration page by clicking on 'Register'
in the navbar and fill out the required registration form. The registration page can
also be reached via a link on the login page below the login button.

### Feature 5 - Login, Logout & Reset Password

**User story: "As a user, I want to be able to login, logout and reset my password if need be."**

Users can login by browsing to the login page by clicking on the 'Login' link in the navbar,
and click on login after entering their login credentials. Users can logout by clicking on
the 'Logout' link in the navbar. Users can reset their password by clicking on the 'forgot
password' link on the login page.

NOTE: The login link in the navbar is only visible for non-authenticated users whilst the logout
link in the navbar only is visible for authenticated users.

### Feature 6 - View products in database

**User story: "As a user, I want to be able to browse through the database of available donated products."**

Users can browse through all products by clicking on the 'Browse shop' link in the navbar,
followed by choosing a category. Each category links to the same template but filters out
the applicable choice of products and only displays the ones matching the users choice.
Each product in the product summary is displayed with an image, a title, a animal category,
the condition of the product and the price. Users can click on the 'Read more' button which
renders the product detail page. The product detail page displays the same information of the
product + a more detailed description of the product.

### Feature 7 - Search for products in database

**User story: "As a user, I want to be able to search the database of available donated products."**

Users can search through the product database by entering a search word into the search bar in
the navbar and clicking on the 'search' button. The search renders the products.html page and
only displays the products that match the search criterias based on the product title.

### Feature 8 - Buy products

**User story: "As a user, I want to be able to buy donated products using a credit card."**

Users can buy any product available in the database by clickion on the 'Buy' button on the
product overview or product detail page which adds the chosen product to the shopping cart.
Once the product has been added to the shopping cart, the user can proceed to the checkout
page by clicking on the 'Checkout' button on the shopping cart page. This takes the user
to the checkout page and to finalize the purchase, the user needs to complete the checkout
form and click on 'Submit Payment'.

### Feature 9 - Donate products

**User story: "As a user, I want to be able to donate products."**

Users can donate products via the donate products page which they can reach by clicking on
the 'Donate' -> 'Donate Product' link in the navbar. To finalize the donatin process on 
the donate product page, the user needs to fill out the applicable form and click the
'Donate' button to submit the necessary information and add the product to the database.

### Feature 10 - Make a monetary donation

**User story: "As a user, I want to be able to make a monetary donation."**

Users can make monetary donations on the 'Support Us' page that can be reached by clicking
on the 'Donate' -> 'Support Us' link in the navbar. Users can choose between 3 fixed amounts
to donate, 10€, 50€ & 100€. Clicking on the applicable amount button adds the donation to
the shopping cart. Multiple amounts can be stacked on top of each other if a user wants to
donate a specific amount or a higher amount than the available fixed amounts. Once the monetary
donation has been added to the shopping cart, the user can proceed to the checkout page by
clicking on the 'Checkout' button on the shopping cart page. This takes the user to the
checkout page and to finalize the purchase, the user needs to complete the checkout form
and click on 'Submit Payment'.

### Feature 11 - View user blogposts in database

**User story: "As a user, I want to be able to browse through all user blogposts."**

Non-authenticated users can browse through all user blog posts by clicking on the 'Blog' link
in the navbar which takes the user to the blog posts page. Authenticated users need to click
on the 'Blog' -> 'View All Blog Posts' link in the navbar to get to the blog posts page.
Each blog posts contains an image, a title, a description, author, pet name and published date.

### Feature 12 - Create a blogpost

**User story: "As a user, I want to be able to create a blogpost and share my story with the**
**visitors of the website."**

Only authenticated users can create blog posts. Authenticated users can create blog posts by
clicking on the 'Blog' -> 'Create Blogpost' link in the navbar and then fill out and submit
the applicable form displayed on the create blogpost page.

<br/>

## Defensive Design

<br/>

## Testing

### Manual Testing

Below is a list of manual testing that has been performed. The order of the tests follows the structure of the links in the navbar from left to right.

| Test | Result |
|------|--------|
| Clicking on the navbar logo and 'Home' navigation link in the navbar should navigate to the home page. | Tested on all pages. No errrors. Works as intended. |
| Clicking on the chevron icon at the bottom of the index page should scroll down to the about section. | Tested on all pages. No errrors. Works as intended. |
| Clicking on the 'About 2nd Paw' link in the navbar when on the index page should scroll down to the applicable section. | Tested on the index page. No errrors. Works as intended. |
| Clicking on the 'About 2nd Paw' link in the navbar when on any other page than the index page should navigate to the index page and scroll down to the applicable section. | Tested on the index page. No errrors. Works as intended. |
| Clicking on the 'FAQ' link in the navbar should navigate to the FAQ page. | Tested on all pages. No errrors. Works as intended. |
| Clicking on each question on the FAQ page should expand the applicable accordean section and collapse all other sections that are open. | Tested on all pages. No errrors. Works as intended. |
| Clicking on the 'Contact Us' link in the navbar should navigate to the contact page. | Tested on all pages. No errrors. Works as intended. |
| A user must enter a valid email address into the contact form 'email' field. | Tested. Error message is displayed if user tries to enter invalid email address. |
| A user should not be able to enter more than 50 characters into the contact form 'subject' field. | Tested. Field is restricted to 50 characters. |
| A user should not be able to enter more than 500 characters into the contact form 'subject' field. | Tested. Field is restricted to 500 characters. |
| Clicking on any of the links in the 'browse shop' drop down menu in the navbar should navigate to the products page and display the chosen catogory of products. | Tested on all pages. No errors. Works as intended. |
| Clicking on the 'Read More' button on a product card should navigate to the product detail page. | Tested on all product pages and products. No errrors. Works as intended. |
| Clicking on the 'Add to cart' button on a product card when not logged in should navigate to the login page. | Tested on all product pages and products. No errrors. Works as intended. |
| Clicking on the 'Add to cart' button on a product card when logged in should place the product into the shopping cart, reveal the shopping cart button in the navbar and navigate to the shopping cart page. | Tested. No errors. Works as intended.|
| Clicking on the 'Blog' link in the navbar when not logged in should navigate to the blogposts page. | Tested on all pages. No errors. Works as intended.
| Clicking on the 'View All Blog Posts' link in the navbar when logged in should navigate to the blogposts page. | Tested on all pages. No errrors. Works as intended. |
| Clicking on the 'Create Blog Post' link in the navbar when logged inshould navigate to the create blogpost page/form. | Tested on all pages. No errrors. Works as intended. |
| On the create blog post page, a user should not be able to exceed the max # of characters in each formfield (title = 75, animal name = 100, content = 500). | Tested. Field restrictions work as intended.
| Clicking on the 'Donate Product' link in the navbar when not logged in should navigate to the login page. | Tested on all pages. No errrors. Works as intended. |
| Clicking on the 'Donate Product' link in the navbar when logged in should navigate to the product donation page/form. | Tested on all pages. No errrors. Works as intended. |
| On the donate product page, a user should not be able to exceed the max # of characters in each formfield (title = 75, category = 100, animal = 20, condition = 20, description = 500). | Tested. Field restrictions work as intended.
| Clicking on the 'Donate' button on the donate product page after completing all formfields correctly should add the product to the database, display a confirmation alert message and navigate to the products page | Tested. No errors. Works as intended.
| Clicking on the 'Support Us' link in the navbar should navigate to the monetary donation page. | Tested on all pages. No errrors. Works as intended. |
| Clicking on the 'Donate X€' buttons on the support us page (logged in or not) should place the doanations into the shopping cart, reveal the shopping cart button in the navbar and navigate to the shopping cart page. | Tested. No errors. Works as intended.|
| Clicking on the 'My Page' link in the navbar should navigate to the monetary donation page. | Tested on all pages. No errrors. Works as intended. |
| Clicking on the 'Register' link in the navbar when not logged in should navigate to the registration page/form. | Tested on all pages. No errrors. Works as intended. |
| Clicking on the 'Login' link in the navbar when not logged in should navigate to the login page/form. | Tested on all pages. No errrors. Works as intended. |
| Clicking on the 'click here' links on the login page should navigate to the registration and/or password reset page. | Tested. No errors. Works as intended. |
| Entering the correct login credentials on the login page and clicking 'Login' should log the user in, navigate to the index page and display a confirmation alert. | Tested. No errors. Works as intended. |
| When logging in, the 'Create Blog Post', 'Register' and 'Login' links in the navbar should disappear and be replaced with a 'logout' link instead. | Tested. No errors. Works as intended. |
| Clicking on the 'Logout' link in the navbar when logged in should log out the user, navigate to the index page and display a confirmation alert. | Tested on all pages. No errrors. Works as intended. |
| When logging out, the 'Logout' link in the navbar should disappear and the 'Create Blog Post', 'Register' and 'Login' links should reapear. | Tested. No errors. Works as intended. |
| Entering a search string and clicking on the search button in the navbar should search the database, navigate to the products page and display all applicable products that match the search. If no products match the search string, the page should display a messge that no products were found. | Tested. No errors. Works as intended. |

### Automated Testing

In total, I created 50 automated tests of forms, models, views and urls for each app in the project.

Total coverage is 83%.

The full report of the automated tests performed can be accessed [here](https://github.com/3PU/2nd-paw/blob/master/testing/automated_testing_report.pdf).

### Code Validation

Filename                    | Code      | Validator                             | Outcome | Comments |
----------------------------|-----------|---------------------------------------|---------|----------|
| static/css/custom.css | CSS | https://jigsaw.w3.org/css-validator/validator | First test passed with 0 errors | n/a |
| accounts/templates/login.html | HTML5 | https://validator.w3.org/ | First test passed with 0 errors | n/a |
| accounts/templates/profile.html | HTML5 | https://validator.w3.org/ | First test passed with 0 errors | n/a |
| accounts/templates/registration.html | HTML5 | https://validator.w3.org/ | First test passed with 0 errors | n/a |
| accounts/backends.py | Python3 | http://pep8online.com/ | First test passed with 5 errors. Second test passed with 0 errors. | 2 lines with whitespace. 1 line missing blank line. 2 lines exceeded 79 characters. |
| accounts/forms.py | Python3 | http://pep8online.com/ | First test passed with 5 errors. Second test passed with 0 errors. | 2 missing blank lines, 2 lines contained white space, 1 line exceeded 79 characters. |
| accounts/test_urls.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| accounts/test_views.py | Python3 | http://pep8online.com/ | First test passed with 3 errors. Second test passed with 0 errors. | 3 lines underindented. |
| accounts/url_reset.py | Python3 | http://pep8online.com/ | First test passed with 1 errors. Second test passed with 0 errors. | 1 line exceeded 79 characters. |
| accounts/urls.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| accounts/views.py | Python3 | http://pep8online.com/ | First test passed with 4 errors. Second test passed with 0 errors. | 2 lines exceeded 79 characters. 2 missing blank lines. |
| blog/templates/blogposts.html | HTML5 | https://validator.w3.org/ | First test passed with 2 HTML errors. Second test passed with 0 errors. | 1 stray end tag `</h6>`. 1 unclosed div. |
| blog/templates/create_blogpost.html | HTML5 | https://validator.w3.org/ | First test passed with 0 errors | n/a |
| blog/forms.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| blog/models.py | Python3 | http://pep8online.com/ | First test passed with 2 errors. Second test passed with 0 errors. | 2 missing whitespaces around operators. |
| blog/test_forms.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| blog/test_models.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| blog/test_urls.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| blog/test_views.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| blog/urls.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| blog/views.py | Python3 | http://pep8online.com/ | First test passed with 2 errors. Second test passed with 0 errors. | Closing bracket not matching visual indentation and trailing whitespace. |
| cart/templates/cart.html | HTML5 | https://validator.w3.org/ | First test passed with 0 errors | n/a |
| cart/contexts.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| cart/test_views.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| cart/urls.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| cart/views.py | Python3 | http://pep8online.com/ | First test passed with 3 errors. Second test passed with 0 errors. | 3 trailing whitespaces. |
| checkout/templates/cart.html| HTML5 | https://validator.w3.org/ | First test passed with 0 errors | n/a |
| checkout/admin.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| checkout/forms.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| checkout/models.py | Python3 | http://pep8online.com/ | First test passed with 2 errors. Second test passed with 0 errors. | 1 unexpected space around keyword/parameter. 1 line too long. |
| checkout/test_urls.py | Python3 | http://pep8online.com/ | First test passed with 1 errors. Second test passed with 0 errors. | 1 expected indented block. |
| checkout/test_views.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| checkout/urls.py| Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| home/templates/contact.html | HTML5 | https://validator.w3.org/ | First test passed with 0 errors | n/a |
| home/templates/faq.html | HTML5 | https://validator.w3.org/ | First test passed with 11 HTML errors. Second test passed with 0 errors. | Multiple quotes missing and multiple aria-labelledby pointed to same element id. |
| home/templates/index.html | HTML5 | https://validator.w3.org/ | First test passed with 0 errors | n/a |
| home/forms.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| home/test_views.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| home/views.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| products/templates/create_product.html | HTML5 | https://validator.w3.org/ | First test passed with 0 errors | n/a |
| products/templates/donation.html| HTML5 | https://validator.w3.org/ | First test passed with 1 HTML errors. Second test passed with 0 errors. | 1 stray end tag `</i>` found. |
| products/templates/product_detail.html | HTML5 | https://validator.w3.org/ | First test passed with 1 HTML errors. Second test passed with 0 errors. | 1 no space between attributes found. |
| products/templates/products.html | HTML5 | https://validator.w3.org/ | First test passed with 0 errors | n/a |
| products/forms.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| products/models.py | Python3 | http://pep8online.com/ | First test passed with 1 error. Second test passed with 1 errors (unable to rectify). | 1 line too long, unable to rectify. |
| products/test_urls.py | Python3 | http://pep8online.com/ | First test passed with 1 error. Second test passed with 0 errors. | 1 line too long. |
| products/test_views.py| Python3 | http://pep8online.com/ | First test passed with 1 error. Second test passed with 0 errors. | 1 line too long. |
| products/test.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| products/urls.py | Python3 | http://pep8online.com/ | First test passed with 1 error. Second test passed with 0 errors. | 1 line too long. |
| products/views.py | Python3 | http://pep8online.com/ | First test passed with 3 errors. Second test passed with 0 errors. | 3 blank lines contained whitespace. |
| search/test_views.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| search/urls.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |
| search/views.py | Python3 | http://pep8online.com/ | First test passed with 0 errors. | n/a |

### Responsive Design

The application has been build with a mobile-first approach and throughout the development process, chrome developer tools, multiple PC's and mobile devices
where used to ensure responsiveness across all screen resolutions.

The application was also tested by friends and family across multiple devices and browsers.

For final testing [Responsinator](https://www.responsinator.com/) was used to test the application across multiple devices.

The biggest challenge in terms of responsive design for this project was the variable of users being able to upload images with a variety of formats.

To ensure the images are not distorted and displayed as good as possible, i did not specify a fixed height or width, but instead set the image
background-size to `cover` and defined a `max-width` and `max-height` so the image is represented as intended by the user.

### Screen Size Testing/Compability

Screen Size         | Size              | Comments
--------------------|-------------------|---------
X-Small             | <768px            | Left/right padding of `.card` class was too big which compressed the product and blogposts too much. Decreased left/right padding on screens below <768px by implementing a media query. |
Small               | >=768px           | Passed, no changes needed. |
Medium              | >=992px           | Passed, no changes needed. |
Large               | >=1200px          | Passed, no changes needed. |

### Browser Compability

Browser             | Version           | Comments
--------------------|-------------------|---------
Firefox             | 72.0.2 (64-bit)   | No errors observed |
Edge                | 44.18362.449.0    | Correct color was not applied to the background of the expandable accordion answers nor the links due to a color code not compatible with this browser. Color code adjusted which rectified the issue. |
Chrome              | 80.0.3987.122     | No errors observed |
Opera               | 67.0.3575.31      | No errors observed |

### Navigation

Navigation was kept simple with a fixed navbar at the page top in order to give the body as much real estate as possible.

To not clutter the navbar with too many links, drop-down menus are used for the about, browse shop, blog and donate sections.

On screens bewow 768px the navigation links are replaced by a nav-toggler to adjust for the lesser screen space available.

The navbar brand logo is located in a classic top left corner location. When clicked the user will be returned to the homepage.

<br/>

## Deployment

The project is stored in a GitHub  [repository](https://github.com/3PU/2nd-paw) and hosted on [Heroku](https://codei-2nd-paws.herokuapp.com/).

**How to clone this repository and run the code locally on your machine:**

1. When logged into GitHub, navigate to the repository you want to clone. For this project, click [here](https://github.com/3PU/2nd-paw).
2. Click on the **'Clone or download'** button which should be displayed above and to the right of the repository files.
3. You are presented with a HTTPs address. Copy this address by pressing the button to the right of the address.
4. From your preferred IDE, open your terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type **'git clone https://github.com/username/filename'**.
7. Install all required modules / packages with the command **'pip3 -r requirements.txt'**.
8. If youa re using AWS Cloud9 or GitPod, create a new file in the root directory called `env.py` and add the following variables to
the file:

```
import os

os.environ["SECRET_KEY"] = "enter key here"
os.environ["STRIPE_PUBLISHABLE"] = "enter key here"
os.environ["STRIPE_SECRET"] = "enter key here"
os.environ["AWS_ACCESS_KEY_ID"] = "enter key here"
os.environ["AWS_SECRET_ACCESS_KEY"] = "enter key here"
os.environ.setdefault("EMAIL_USER",'enter email details here')
os.environ.setdefault("EMAIL_PASS",'enter key details here')
os.environ["DEVELOPMENT"] = "1"

```
9. Make migrations and migrate to create the database by using the terminal command `python3 manage.py makemigrations` and `python3 manage.py migrate`.
10. Create a superuser by using the terminal command `python3 manage.py createsuperuser` and follow the instructions prompted in the terminal window.
11. If you are not using S3 bucket to host the static and media files, update the static and media links in the `settings.py` file to the folder links
that you are using for your static and media files.
12. The app can now be run locally using the terminal command `python3 manage.py` runserver.

**How to deploy to Heroku using GitPod:**

1. Created a new application using the Heroku dashboard.
2. Go to settings tab, click on 'reveal config vars' and add the following config vars from your `env.py`file:

| Key | Value |
|-----|-------|
| SECRET_KEY | Secret key value |
| STRIPE_PUBLISHABLE | Secret key value |
| STRIPE_SECRET | Secret key value |
| DATABASE_URL | Postgres url link |
| AWS_ACCESS_KEY_ID | Secret key value |
| AWS_SECRET_ACCESS_KEY | Secret key value |

3. Install Heroku via the terminal using `npm install -g Heroku`.
4. Log into Heroku via the terminal using `heroku login` and follow the on screen instructions to log in.
5. Create a requirements.txt via the terminal using `pip3 freeze > requirements.txt`.
6. Create a Procfile via the terminal using `echo web: python app.py > Procfile`.
7. Connect GitHub to Heroku via the terminal using `heroku git:remote a appname`, in this example `heroku git:remote a codei-2nd-paws`.
8. Commit all files in your project via the terminalole using `git add .' and 'git commit -m "Message"`.
9. Push and deploy all files to github and Heroku using the terminal command `gith push && gith push heroku master`.
10. Enter the heroku postgres database url to the settings.py file.
11. Make migrations and migrate to create the database by using the terminal command `python3 manage.py makemigrations` and `python3 manage.py migrate`.
12. Create a superuser in your new database by using the terminal command `python3 manage.py createsuperuser` and follow the instructions prompted in the terminal window.
13. After setting up the database and the build on Heroku is complete, click on the heroku link or 'view app' button to run the application via Heroku.

<br/>

## Credits

### Content

All of the text content on the website has been written by me.

### Media

The static images used accross the page were obtained from [Pexels](https://www.pexels.com/) and [Google Images](https://images.google.com/).s

### Acknowledgements

A very big thank you goes to my Code Institute Mentor Brian M. for his invaluable support and guidance throughout all my coding projects including this one.

### Disclaimer

The content of this website is for educational purposes only.