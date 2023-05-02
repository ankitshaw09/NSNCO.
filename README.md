# NSNCO.
Assignment 
#explanation of  the API endpoints that i have created:

1. `GET /api/works`: This endpoint returns a list of all works in the database. Optionally, it allows filtering of works by work type using the `work_type` query parameter and searching for works by artist name using the `artist` query parameter. For example, to filter by work type, we can use the URL `GET /api/works?work_type=Youtube`. To search for works by artist name, we can use the URL `GET /api/works?artist=John`.

2. `POST /api/register`: This endpoint allows users to register by providing a username and password in the request body. Upon successful registration, it returns a message confirming that the user has been created.

Both these endpoints are implemented using Django's built-in `APIView` class and the `rest_framework.decorators.api_view` decorator. We have also used Django's built-in `User` model for handling user registration, and Django REST Framework's `serializers` module to serialize and deserialize model instances. 

Note that the endpoints are prefixed with `/api/` to distinguish them from regular views and to adhere to RESTful conventions.
