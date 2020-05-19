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

### Colors, Fonts & Layout

The following colors are used throughout the project:

- #fffff (Text)
- #00000 (Text, shadows and elements with various degrees of opacity)
- #c2c3c3 (Elements)
- #a2a2a2 (Element hover)
- #585454 (Buttons & borders)
- #110b0bb3 (Accordion)

In terms of fonts, initially I thought about using two fonts, but after implementing Google Fonts 'Ubuntu' I realized it looked very good by itself across the site.

The idex page is kept very clean, using only a background image that fills up the entire first page. I decided to place a chevron icon at the bottom
of the page to naturally provoke users to scroll down where they can find the 'About' page. If users decide to browse to the about section via
the navbar instead, the page will scroll down (smooth scroll on chrome browsers only).

The navbar should provide users with an intuitive way to engage with the website and I therefore did not feel the need to add descriptive text to the index page,
a choice that has proven to be effective via testing from multiple first-time users.

### Responsiveness

The website has been built with a mobile-first approach and is highly responsive.

This is primarily achieved by using bootstrap and custom-written css (for more details see testing section).

## UX

The overall goal of the website is to provide visitors with the ability to donate pet products they no longer need or use
or buy pet products at a discounted price, and by that financially support the local cat and dog shelters.

Visitors can also choose to make monetary donations or create a blogpost showing how their pet liked a product purchased
through the website.

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