# RESTful API Theory

## What is a request?

A request is a message sent from a client to a server to perform an action. In the context of RESTful APIs, a request is typically an HTTP request that contains information about the action to be performed on a resource. There are several types of HTTP requests. If we load a webpage in the browser, the browser sends a GET request to the server to retrieve a HTML file, this file is then rendered by the browser as a webpage. If we submit a form on a webpage, the browser sends a POST request to the server to submit the form data. Similarly, we have PUT and DELETE requests to update and delete resources, respectively.

## What is a response?

A response is a message sent from a server to a client in response to a request. In the context of RESTful APIs, a response is typically an HTTP response that contains information about the result of the action performed on a resource. The response can include data, status codes, headers, and other information that the client can use to process the response. For example, if we send a GET request to retrieve a list of users, the server will respond with a JSON object containing the user data. If we send a POST request to create a new user, the server will respond with a status code indicating the success or failure of the operation.

## What is a resource?

A resource is an object or entity that can be accessed and manipulated by a client through a RESTful API. Resources can be anything from users, products, orders, to blog posts, comments, and more. Each resource is identified by a unique URI (Uniform Resource Identifier) that the client can use to interact with the resource. For example, a user resource might have the URI `/users/{id}` where `{id}` is the unique identifier of the user. Resources can be created, read, updated, and deleted using standard HTTP methods like GET, POST, PUT, DELETE.

## Example:

Let's consider an example of a simple RESTful API for managing users. The API exposes the following resources:

- `/users`: A collection of users
- `/users/{id}`: A specific user identified by `{id}`

The API supports the following operations on users:

- `GET /users`: Retrieve a list of users (Read operation)
- `POST /users`: Create a new user (Create operation)
- `GET /users/{id}`: Retrieve a specific user (Read operation)
- `PUT /users/{id}`: Update a specific user (Update operation, Replace operation) - PUT replaces the entire resource
- `PATCH /users/{id}`: Update a specific user (Update operation, Modify operation) - PATCH modifies part of the resource
- `DELETE /users/{id}`: Delete a specific user (Delete operation)

Each operation corresponds to a CRUD (Create, Read, Update, Delete) operation on the user resource. The API uses standard HTTP methods to perform these operations and standard HTTP status codes to indicate the success or failure of the operations.

There are 3 types of resources in RESTful API:

- Collection resource: A collection of resources, e.g., `/users`
- Singleton resource: A single resource, e.g., `/users/{id}`
- Sub-resource: A resource that is part of another resource, e.g., `/users/{id}/posts`

And there are 3 ways data can be sent to the server:

- Request parameters: Data sent in the URL, e.g., `/users?sort=asc`
- Request headers: Data sent in the headers, e.g., `Authorization
- Request body: Data sent in the body of the request, e.g., JSON, XML, form data

## Request parameters

Request parameters are used to send additional information to the server as part of the URL. Parameters are typically used to filter, sort, paginate, or search for resources. For example, if we want to retrieve a list of users sorted in ascending order by their name, we can send a request like `/users?sort=asc`. The server can then use the `sort` parameter to sort the list of users before sending it back to the client.

Examples:

- `/users?sort=asc`: Retrieve a list of users sorted in ascending order
- `/users?limit=10&offset=0`: Retrieve the first 10 users
- `/users?search=john`: Search for users with the name "john"

## Request headers

Request headers are used to send additional information to the server as part of the HTTP headers. Headers are typically used to provide metadata about the request, such as the content type of the request body, the authorization token, or the preferred language of the response. For example, if we want to send an authorization token to the server to authenticate the request, we can include an `Authorization` header with the token value.

Examples:

- `Authorization Bearer <token>`: Authenticate the request using a Bearer token
- `Content-Type application/json`: Specify that the request body is in JSON format
- `Accept application/json`: Specify that the client accepts JSON responses

## Request body

Request body is used to send data to the server as part of the request body. The body can contain data in various formats such as JSON, XML, form data, or plain text. The body is typically used to send complex data structures or large amounts of data that cannot be sent as request parameters or headers. For example, if we want to create a new user with a name, email, and password, we can send a POST request with a JSON body containing the user data.

Examples:

- JSON body: `{ "name": "John Doe", "email": "john@doe.com", "password": "password" }`
- XML body: `<user><name>John Doe</name><email>john@doe.com</email><password>password</password></user>`
- Form data: `name=John+Doe&email=john%40doe.com&password=password`

## Response status codes

Response status codes are used to indicate the success or failure of an HTTP request. Status codes are divided into 5 categories:

- 1xx: Informational - Request received, continuing process
- 2xx: Success - The action was successfully received, understood, and accepted
- 3xx: Redirection - Further action must be taken to complete the request
- 4xx: Client Error - The request contains bad syntax or cannot be fulfilled
- 5xx: Server Error - The server failed to fulfill an apparently valid request

Some common status codes include:

- 200 OK: The request was successful
- 201 Created: The resource was successfully created
- 204 No Content: The request was successful, but there is no content to return
- 400 Bad Request: The request contains bad syntax or cannot be fulfilled
- 401 Unauthorized: The request requires user authentication
- 403 Forbidden: The server understood the request, but refuses to authorize it
- 404 Not Found: The requested resource was not found
- 500 Internal Server Error: The server encountered an unexpected condition

![RESTful API Example](images/restful-api-example.png)

## Summary

In this part, we covered the basic concepts of RESTful APIs, including requests, responses, resources, request parameters, headers, body, and response status codes. We also looked at an example of a simple RESTful API for managing users and how to perform CRUD operations on the user resource. Understanding these concepts is essential for building and consuming RESTful APIs effectively.

## Next Steps

Take a look at these resources to learn more about RESTful APIs:

- [Microsoft Learn - best practices for api design ](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)
- [RESTful API Tutorial](https://restfulapi.net/)
- [MDN Web Docs - HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
