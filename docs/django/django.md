<span style='font-size:24px;font-family:Segoe Print'>

# How Django Executes Code (Big Picture)


This document explains **when and how Django uses
the code we write**, especially for beginners who are confused
by declarative components like Models and Views.
</span>

---

# 1. Django Is Not a Script Runner.

Unlike simple scripts, Django does not execute code line by line.

Instead, Django works as a **framework**:
- We define rules and structures.
- **Django calls our code at specific moments.**

Most classes in Django are **not called directly by us.**


---

# 2. What Happens When Django Starts ?

When running:

```bash
python manage.py runserver
```
- Django performs:
    1. Load settings.
    2. Discover installed **apps**.
        - App means a independent function module.For example,you are working at a supermarket website,you seperate the task to products app,oreders app,users app...
        - Django will go to check all the modules in your `INSTALLED_APPS` at `setting.py` and load them. 
    3. Import models,views,and other modules.
    4. Register them internally(內部地)
        - **rigister** means telling Django to add this class(data structure) to their list,so the following demand can be done.
        - After this step,Django can identify the class you created.
- At this stage:
    - Models are registered to the ORM.
        - **ORM** is called **Object-Relational Mapping**,its your translator between Python code and SQL.
    - Views are registered as callable endpoints.
        - **endpoints** mostly means URL,in web developement we say "This is a API endpoint" means this is a url that you can access through browser or cellphone app.
        - **Views are registered as a callable endpoints** means Django bind your view funciton to a url,when somebody visit the url,Django will call your view function to handle the task.
    - Nothing is "running" yet.

---

# 3. Where Execution Acatually Starts ? 
Execution begins only when:

1. An HTTP request is received
2. Django matches the URL
3. Django calls the corresponding View method

Only Views are executed directly.

Models and Serializers are used by Views,but they do not run on their own.


# 4. Why Models Do Not Executes ? 

Models define:
- Database schema
- Relationships
- ORM behavior

Django uses them when database operations are requested.

# 5. Why Serializers Do Not Executes ? 

Serializers define:
- Input/output data rules
- Validation logic

They are triggered only when a View calls `serializer.is_valid()` or `serializer.save()`

# 6. The Role of Views ?

**Views are the entry point of execution.**

A View:

    - Receives a request
    - Coordinates serializers and models
    - Returns a response

Without a View,nothing happens.

# 7. URL Routing ?

URLs in Django act as **routing rules**,not logic handlers.

- What is **routing**: A list mapping every url to their handler.In Django,it usually means your `urls.py`.  

# 8. What Happens on a request ? 

1. Django receives an HTTP request.
2. Django resolves the request path using `urls.py`.
3. The matched View is called via `as_view()`.
4. The View method (ex. `post`) executes.

URLs only connect a request to a View.

# 9. Why `as_view()` is required ?

Class-based Views must be converted into callable funcitons using `as_view()` so Django can execute them.


# Summary:
- Models define data structure
- Serializers validate and transform input data.
- Views orchestrate request handling.
- URLs map HTTP requests to views.

Each layer is passive until called by the upper layer

</span>