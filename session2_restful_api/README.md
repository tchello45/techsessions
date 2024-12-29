# Tech Session 2 - Introduction to RESTful APIs
## What is a RESTful API?
A RESTful API is an API that follows the principles of REST. REST is an architectural style that defines a set of constraints for creating web services. RESTful APIs are designed to be simple, lightweight, and scalable, making them ideal for building web applications. RESTful APIs use standard HTTP methods like GET, POST, PUT, DELETE to perform CRUD (Create, Read, Update, Delete) operations on resources. RESTful APIs use standard HTTP status codes to indicate the success or failure of an operation.

## Features of RESTful APIs
- **Resource-based**: RESTful APIs are resource-based, meaning that they expose resources (e.g., users, products, orders) that can be accessed and manipulated using standard HTTP methods.
- **Stateless**: RESTful APIs are stateless, meaning that each request from a client to the server must contain all the information necessary to process the request. The server does not store any client state between requests.
- **Uniform interface**: RESTful APIs use a uniform interface, meaning that they use standard HTTP methods (GET, POST, PUT, DELETE) and status codes to interact with resources.
- **Self-descriptive messages**: RESTful APIs use self-descriptive messages, meaning that each response from the server contains information about how to process the response.
- **Layered system**: RESTful APIs are layered, meaning that the client interacts with a server without knowing the underlying implementation details.

For our tech session, we will be using Flask, a lightweight WSGI web application framework, to create a simple RESTful API. If you are new to Flask, you can refer to the [Introduction to Flask Part 1](../session1_flask/README.md#contents) for more information.

## Contents
- **Part 1**: RESTful API Theory