# JSON and APIs

## JSON

- ### Stands for: 
  - **JavaScript Object Notation**
- ### Used for:
  - **Storing and Transporting data.** 
  - It is commonly used to exchange data between a server
and a client in web applications.
  - Transferring data between systems.
- ### Written in: 
  - JSON is written in **text format** that is completely 
language independent. It is derived from JavaScript, but can be 
used with many other programming languages: Python, C++, Java, etc.
- ### JSON Data Types:
  - JSON can store and use the following data types:
    - **String:** A sequence of characters enclosed in double quotes. 
    - **Number:** An integer or floating-point number. 
    - **Boolean:** true or false. 
    - **Array:** An ordered list of values. 
    - **Object:** A collection of key/value pairs. 
    - **Null:** An empty value, represented by null.
- ### JSON Syntax:
  - **Name-value pairs:**
    - In JSON, data is represented in name/value pairs. Each pair consists 
of a field name (in double quotes), followed by a colon, and then the value.
    
      - ``` {"name": John}```
    
  - **Objects:**
    - A JSON object is a collection of name/value pairs enclosed in curly braces { }. 
Each pair is separated by a comma.
    
      - ``` {"name": "John", "age": 30, "isStudent": false}```
    
  - **Separating Data Objects:**
    - In JSON, objects within an array are separated by commas. Each object is enclosed in 
curly braces.
    
      - ``` {"name": "John", "age": 30}```
    
  - **JSON Arrays:**
    - A JSON array is an ordered list of values enclosed in square brackets [ ]. 
The values can be of any type, including objects, arrays, strings, numbers, booleans, or null.

      - ``` ["apple", "banana", "cherry"] ```
    - Arrays can also contain objects, providing a way to structure data in a hierarchical form.
      - ``` [{"name": "John", "age": 30},``` ```{"name": "Jane", "age": 25}]```


## APIs

APIs, or Application Programming Interfaces, are sets of rules and protocols that allow different 
software applications to communicate with each other. They define the methods and data formats that 
applications can use to request and exchange information.

### APIs are used in various ways:
- **Integration:** APIs allow different software systems to integrate with each other, enabling them 
to share data and functionalities. 
- **Development:** Developers use APIs to access the functionality of existing software systems and 
build new applications or services on top of them, saving time and effort. 
- **Automation:** APIs facilitate automation by providing a standardized way for different systems 
to interact programmatically, without requiring manual intervention. 
- **Extensibility:** APIs allow developers to extend the functionality of their applications by 
integrating with third-party services and libraries.


- APIs have become popular due to the increasing need for interoperability between different 
software systems and the rise of web-based applications and services. They offer a standardized 
way for applications to communicate, making it easier to build complex systems by combining existing components.

### How an API works:

![API Data Transfer Process](https://github.com/Eash17/JSON_and_APIs/blob/main/What-is-an-API.png?raw=true)

### Rest APIs: 
REST APIs (Representational State Transfer APIs) are a type of API that follows the principles of REST architecture. 
- A RESTful API is characterized by: 
  - **Statelessness:** Each request from a client to the server must contain all the information necessary to 
understand and process the request. The server should not rely on any client context stored on the server between requests. 
  - **Resource-based:** RESTful APIs are based on resources, which are identified by URIs (Uniform Resource Identifiers). 
Clients interact with these resources using standard HTTP methods (GET, POST, PUT, DELETE) and represent the state of the 
resource at any given point in time. 
  - **Representation:** Resources in a RESTful API can have multiple representations, such as JSON or XML, which the client 
can choose based on its requirements or preferences.


- Overall, REST architecture emphasizes simplicity, scalability, and modifiability, making it a popular choice for designing 
APIs and web services. It leverages existing standards like HTTP and URIs to create interoperable and efficient distributed systems.

### HTTP:
- HTTP (Hypertext Transfer Protocol) is the underlying protocol used for communication on the World Wide Web. 
- It defines how messages are formatted and transmitted, and how web servers and browsers should respond to various commands.

***HTTP Request Structure:***
![HTTP Request Structure](https://github.com/Eash17/JSON_and_APIs/blob/main/HTTP%20Request%20Structure.png?raw=true)

***HTTP Response Structure***
![HTTP Response Structure](https://github.com/Eash17/JSON_and_APIs/blob/main/HTTP%20Response%20Structure.png?raw=true)

### The 5 HTTP Verbs:
- **GET:** Retrieves data from the server specified by the URL. 
- **POST:** Submits data to be processed to the server specified by the URL. 
- **PUT:** Updates data on the server specified by the URL. 
- **DELETE:** Deletes data from the server specified by the URL. 
- **PATCH:** Applies partial modifications to a resource on the server specified by the URL.