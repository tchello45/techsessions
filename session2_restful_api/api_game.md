# Solution API Game
## Introduction
In this section, we will "hack" a simple RESTful API. The API is built using Flask, a popular web framework for Python. With the Postman tool, we will interact with the API to perform CRUD (Create, Read, Update, Delete) operations on a resource. The resource in this case is a collection of users. We will send HTTP requests to the API to create new users, retrieve a list of users, retrieve a specific user, update a user, and delete a user. We will also learn how to handle errors and exceptions in the API.

## Objectives
- Retrieve the flag from `/secret` endpoint

## Prerequisites
Start the API server by running the following command in the terminal:
```bash
python api_game.py
```
The API server will start running on `http://127.0.0.1:5000/`.

## Available Endpoints
- `/users`: Retrieve a list of users
    - `?detailed=1`: Retrieve a list of users with additional details
    - `?user_level=admin`: Retrieve a list of users with the user level set to "admin"
    - `?clear_password=1`: Retrieve a list of users with visible passwords
- `/security`: Retrieve the security information
- `/login`: Login to the API
- `/secret`: Retrieve the secret flag

:) Good luck!

## Step by Step Solution
1. **Retrieve a list of users**
    - Send a GET request to `/users` to retrieve a list of users. -> Only the first 10 users are displayed.
    - Send a GET request to `/users?detailed=1` to retrieve a list of users with additional details. -> Only the first 10 users  (with additional details) are displayed. -> You can now see the user level
    - Send a GET request to `/users?user_level=admin` to retrieve a list of users with the user level set to "admin". -> Filter out the unwanted users
    - Send a GET request to `/users?clear_password=1` to retrieve a list of users with visible passwords. -> *ERROR: You are not authorized to view this resource!*
2. **Retrieve the security information**
    - Send a GET request to `/security` to retrieve the security information. -> You can see the security information `{"clear_passwords_via_api_enabled": false, ...}`
    - Send a PATCH request to `/security` with the data `{"clear_passwords_via_api_enabled": true}` to enable the clear passwords via the API. 
    - Send a GET request to `/security` to verify that the clear passwords via the API is enabled. -> You can see the security information `{"clear_passwords_via_api_enabled": true, ...}`
3. **Retrieve the admin password**
    - Send a GET request to `/users?clear_password=1?user_level=admin` to retrieve the list of users with visible passwords and user level set to "admin". -> *This now works!*
4. **Login to the API**
    - Send a POST request to `/login` with the data `{"username": "<admin_username>", "password": "<admin_password>"}` to login to the API. -> You will receive a token in the response.
5. **Retrieve the secret flag**
    - Send a GET request to `/secret` with the token in the headers to retrieve the secret flag. -> You will receive the secret flag `CTF{fl4sk_1s_aw3s0m3}`.
Congratulations! You have successfully retrieved the flag from the `/secret` endpoint.

