# CRUD REST API DOCUMENTATION
This document provides detailed information about the **`CRUD`** (Create, Read, Update, Delete) **REST API**, which is designed to manage resources through *HTTP* requests. The **API** allows users to perform **`CRUD`** operations on a specific *resource*, and it follows the principles of **RESTful** architecture.

### Table of Content
1. [API Endpoints](#api-endpoints)
2. [Sample Usage](#sample-usage)
3. [Limitations / Assumptions](#limitationsassumptions)
4. [Deploying](#deploying-api)
5. [Contact Me](#contact)

## API ENDPOINTS
### Create (POST)
* Creates a new `person` with a *unique* name
* Endpoint: `/api`
* **Request body**:

    ```json
    {
        "name": "Obaloluwa"
    }
    ```
* **Response Format**:

    • `201 Created` status code on success:

    ```json
    {
        "id": 1,
        "name": "Obaloluwa"
    }
    ```
    • `400 Bad Request` if :

    • `name` aleady *exists* in the *database*:
    
    ```json
    {
        "detail": "Person already exists"
    }
    ```

    • `request` body is *invalid*:

    ```json
    {
        "detail": "Invalid request body"
    }
    ```

### Read (GET)
* Gets details of an existing `person`
* Endpoint: `/api/{id}`
* **Request Format**:
    
    You can get the details of a person either by their `id` or their unique `name`

    • By `id`: Pass the desired `id` in the endpoint

    • By `name`: Pass the desired `name` as a body (alongside a random id):

    ```json
    {
        "name": "Obaloluwa"
    }
    ```
* **Response Format**:
    
    • `200 OK` on success:

    ```json
    {
        "name": "Obaloluwa",
        "id": 1
    }
    ```
    • `404 Not Found` if the resource with the given `id` or `name` does not exist:

    ```json
    {
        "detail": "Person not found"
    }
    ```

### Update (PUT)
* Updates details of an existing `person`
* Endpoint: `/api/{id}`
* **Request Format** (with `id` = 1):

    ```json
    {
        "name": "o_O"
    }
    ```
* **Response Format**:

    • `200 OK` on success:
    ```json
    {
        "id": 1,
        "name": "o_O"
    }
    ```
    • `404 Not Found` if the resource with the given `id` does not exist:

    ```json
    {
        "detail": "Person not found"
    }
    ```
    • `400 Bad Request` if the request body is invalid:

    ```json
    {
        "detail": "Invalid request body"
    }
    ```

### Delete (DELETE)
* Deletes an existing `person`
* Endpoint: `/api/{id}`
* **Request Format**:
    
    You can get the details of a person either by their `id` or their unique `name`

    • By `id`: Pass the desired `id` in the endpoint

    • By `name`: Pass the desired `name` as a body (alongside a random id):

    ```json
    {
        "name": "o_O"
    }
    ```
* **Response Format**:

    • `204 No Content` on success

    • `404 Not Found` if the resource with the given `id` or `name` does not exist:

    ```json
    {
        "detail": "Person not found"
    }
    ```
    • `400 Bad Request` if the request body is invalid:

    ```json
    {
        "detail": "Invalid request body"
    }
    ```

## SAMPLE USAGE
* **Creating a person**:

    • *Request*:
    ```http
    POST /api
    Content-Type: application/json

    {
        "name": "Obaloluwa"
    }
    ```

    • *Response (201 created)*:
    ```json
    {
        "id": 1,
        "name": "Obaloluwa"
    }
    ```

* **Reading a person**:

    • *Requests* (random id when adding a body):
    ```http
    GET /api/4 
    Content-Type: application/json

    {
        "name": "Obaloluwa"
    }
    ```
    **OR**

    ```http
    GET /api/1
    ```

    • *Response (200 OK)*:
    ```json
    {
        "id": 1,
        "name": "Obaloluwa"
    }
    ```

* **Updating a person**:

    • *Request*:
    ```http
    PUT /api/1
    Content-Type: application/json

    {
        "name": "o_O"
    }
    ```

    • *Response (200 OK)*:
    ```json
    {
        "id": 1,
        "name": "o_O"
    }
    ```
* **Deleting a person**:

    • *Requests* (random id when adding a body):
    ```http
    DELETE /api/4
    Content-Type: application/json

    {
        "name": "Obaloluwa"
    }
    ```

    **OR**

    ```http
    DELETE /api/1
    ```
    • *Response (204 No Content)*: No response content

## LIMITATIONS/ASSUMPTIONS
* `GET`, `PUT` and `DELETE` requests must **always** take an `id` path parameter
* For `GET` and `DELETE` requests, if a body is passed, it is given precedence over the `id` passed.

## DEPLOYING API
* **Locally**: To deploy and use this API locally, check out the [README.md](/README.md)

* **Server**: To deploy on a server, follow these steps:
    • Set up a server environment (e.g render)

    • Deploy the API code from my repo ```https://github.com/datalordstephen/hngx-stage-2``` to your server.

    • Ensure the python environment is `3.10.0` or greater

    • Start the server with the command:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

### CONTACT
If you have any more questions, you can :
* Send me a dm on [X](https://twitter.com/datalordstephen) (formerly twitter)
* Send me an [email](mailto:obaadegbokun1@gmail.com)

