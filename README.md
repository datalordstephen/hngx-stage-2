# HNGX Stage Two Task
## CRUD REST API

For the stage `two` task, we were tasked to create a **REST** API capable of **CRUD** operations, and *dynamically* handling parameters.

I built this **API** with *python*, making use of the `fastapi` library and a *postgresql* database.

# Setup
The following steps are necessary to get the **API** up and running
* Ensure you have version 3.10.0 (or above) of [python]("https://www.python.org/downloads/release/python-3100/) installed. Locate the suitable file for your OS, download and install. When installing, ensure that you click the **add to PATH** option at the bottom left corner when installing.
* Clone this **repo** using this command:

    ```bash
    git clone https://github.com/datalordstephen/hngx-stage-2.git
    ```
* Change your `directory` into the cloned project and create a *virtual environment*

    ```bash
    cd hngx-stage-2
    ```

    ```bash
    py -m venv venv
    ```
* Enter into your *virtual environment*

    For `bash`:
    ```bash
    source venv/Scripts/activate
    ```

    For `powershell` and `command prompt`:
    ```shell
    venv\Scripts\activate.bat
    ```

* Download the **requirements**:
    ```bash
    pip install -r requirements.txt
    ```

* Start the **server**:
    ```bash
    uvicorn main:app
    ```

### That's it!
The server is now running locally at ```http://127.0.0.1:8000``` and can receive requests. Note that the database is hosted remotely, so an internet connection would be needed to successfully run queries.