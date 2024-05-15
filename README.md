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