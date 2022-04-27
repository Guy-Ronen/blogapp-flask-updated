# My Foundations Flask Application.

For my university module, I developed a small full stack Flask application as a blog site where you can register, log in , do all kinds of CRUD operations to the posts and even have an account page you can update and map posts by author.

This application runs on python in the backend and javascript on the front-end following the MVC structure (Model, View, Controller) and has a standard user flow where content can be displayedn only if a user is authenticated and authorised.

All pages and buttons on the navbar are dynamcially appeared based if the user is logged in or not. When a user makes a request (for examples registration), it sends a request to the back end where the application makes sure that the input follows the business rules and if its validated, it does the operation needed to the database and sends a response to the front end whether it was succsessful or not. This flow can can appear in many cases in the application.

# How to set up the local development:
1. Clone the repository
2. Download flask (`pip install flask`)
3. make sure that you also pip install the relevant flask packages
4. After there's no more import issue, enter in the terminal `FLASK_APP=run.py`
5. And then finally, enter  `python3 run.py` and it should work


# Deployed website
Here is a link to the deployed heroku website: https://still-caverns-60680.herokuapp.com/


Thank you for your time and have a great day :)
