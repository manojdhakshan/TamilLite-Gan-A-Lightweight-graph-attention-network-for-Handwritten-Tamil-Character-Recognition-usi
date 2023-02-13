To complete this assignment, we can use a Python web framework such as Flask or Django to create an API server. we can then use a GraphQL library such as Graphene to handle the GraphQL calls at "/gql".

Here is an example implementation using Flask and Graphene:

Run API_server.py file

 we first import the required libraries and initialize a new Flask application.

Next, we define the Branch and Bank GraphQL object types using the graphene library. These object types correspond to the nodes in the branches data that we want to query.

We also define a Query object type that will serve as the root query for our GraphQL API. The resolve_branches method of the Query class is used to retrieve the branches data from the database and return it as a list of Branch objects.

Finally, we create a new graphene.Schema object using the Query class as the root query, and add a new URL rule to the Flask app for the "/gql" endpoint, which will be handled by the GraphQLView class provided by the flask_graphql library.

With these steps, we should have a basic Flask-based GraphQL API server set up, ready to be customized and extended as needed to support your specific requirements.

Run Test_case.py file

we use the requests library to make a POST request to the GraphQL endpoint at "/gql". The request body contains the GraphQL query that we want to execute. We then retrieve the response from the server and parse it into a Python dictionary using the json library.

Next, we use the assert statement to make various assertions about the response, such as checking the status code, the presence of the 'data' key in the response, the presence of the 'branches' key in the data, and the length of the branches list.

Finally, we loop over the branches in the response and make additional assertions about the data, such as checking the presence of the 'node' key, the 'branch' key, the 'bank' key, and the 'ifsc' key.

With these test cases in place, we can run the tests using the pytest command and verify that the API server is working as expected.

Finally by Heroku

Create a new Heroku account or log in to an existing one.

Install the Heroku CLI and run the heroku login command to log in to your account from the terminal.

Create a new Heroku app using the heroku create command. This will create a new remote repository for your app on the Heroku servers.

Commit your code to the local Git repository for your app and push it to the Heroku remote repository using the following commands:

csharp
Copy code
git init
git add .
git commit -m "Initial commit"
git push heroku master
Define the environment variables that your app needs in the Heroku environment. we can do this using the Heroku CLI with the heroku config:set command. For example:

python
Copy code
heroku config:set FLASK_APP=app.py
heroku config:set FLASK_ENV=production
Scale the number of dynos for your app to 1 using the heroku ps:scale command:

Copy code
heroku ps:scale web=1
Open the app in a web browser using the heroku open command or by visiting the URL of your app, which is displayed in the terminal after you run the heroku create command.

Verify that your API server is up and running by making a request to the GraphQL endpoint.

With these steps, we should have a working API server deployed on Heroku. Of course, there may be additional steps or modifications required depending on the specifics of your app and your requirements. But this should give you a good starting point.
