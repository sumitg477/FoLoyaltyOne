# FoLoyaltyOne
For doing LoyaltyOne exercises

Step 1: Hello world wide web
Create a ‘hello world’ web page that runs on a local application server.

Helpful tutorials are available here: http://www.w3schools.com/

Answer: Install Flask. Run app.py, using python.

Step 2: Build the back-end
Create a REST web service with a method that returns the text that is passed to it.

Create a few unit tests to verify your application. You may use any unit test framework.

Answer:

mirrorRestWebService.py contains the code for it. The file retireves the argument from the get url and returns it back. The format is http://127.0.0.1:5000/enterText?mirrorText=<Enter your text here>
  
Step 3: Connect your front and back ends
Create a web form that has a text box, and a ‘Done’ button. When ‘Done’ is clicked make AJAX call, passing the entered text to the web service you created in the previous step. Display the response from the web service call below the text box on the form.
Extend your tests to verify new components.

Answer:
Modified the python code to do render template of the web form, which recieves the variable and sends it to backend via ajax.

Step 4: Bring in the database
Extend your web service to add a method to store text passed from the form into the database using design patterns where appropriate. In addition to saving the text, store the date and time when the data was saved.

I installed postgres db on my mac and ran the below sql to create table:

CREATE TABLE table_user (
    id serial PRIMARY KEY,
    user_text text,
    ts timestamp without time zone default (now() at time zone 'edt')
);

Called the db to store records using psycopg2.

Step 5: Extend the form to capture the user name and a list of all the submissions by user. Add another method to the service to return all text submissions and display them at the bottom of the page.

I altered the user table to add a new column and added a user name field in the front end. 

I added backend functionality to save the username along with the text in the db. I also added a query to fetch all of the user_text and bring it to the frontend.

Step 6: Extend your solution from previous challenge to allow “responding” to already posted texts and display responses, indented, below the related text entry.
As always, extend your tests.

FrontEnd - Parsed the JSON output, formatted it and displayed it properly along with the ability to respond for each stored text message.

Step 7: Capture more data
Capture user’s location (user enters the city) on the form. For every post, include city, city’s latitude and longitude and current temperature. Display this information on the form, next to each post.

Make a new field in the frontend and db to store the city. Register with google maps and open weather map api and call it to get the co-ordinates and temperature. Format it appropriately, to display the co-ordinates and temperature on the page, along with the post.
