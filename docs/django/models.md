# Some OOP words clearify.
<span style='font-size:24px;font-family:Segoe Print;background-color:gray;color:blue'>1. Instance</span>

<span style='font-size:24px;font-family:Segoe Print'>In model,when you define a class call `User`,and you create a user name `Cody`,than `Cody` will be an **instance** of class `User`.</span>

<span style='font-size:24px;font-family:Segoe Print;background-color:gray;color:blue'>2. Attribute</span>

<span style='font-size:24px;font-family:Segoe Print'>Information that attach on an instance,for example you create an instance `Cody` of class `User`,which have a `name` column(`User` has defined a `name` column),we assign the string `Cheng Wang` to it,than `name` is the **attribute**,and `Cheng Wang` is the **value** of that attribute.</span>



# What is Model?

- The following description you can find in [Django documentation](https://docs.djangoproject.com/en/6.0/topics/db/models/)
> <span style='font-size:25px;font-family:Segoe Print'>A model is the single,definitive source(最終依據) of information about your data.</span>

# What is Fields?

<span style='font-size:25px;font-family:Segoe Print'>It can be thought of as a 'declaration' in programming languages.Django has many types of field;when you define an attribute as a specific field,it will follow the rules defined by Django.</span>

## Field types


<span style='font-size:24px;background-color:gray;color:black'>The following code is an example</span>

```python
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50) # CharField is a type of field
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    release_date = models.DateField()  # DateField is a type of field
    num_stars = models.IntegerField()  # IntegerField is a type of field
```
<span style='font-size:24px;font-family:Segoe Print'>1. ```ForeignKey()``` should always on the "many" side</span>

<span style='font-size:24px;font-family:Segoe Print'>2. ```ondelete``` is a mechanism,it defines the behavior of child objects when the referenced parent object is deleted.</span>

|Their Rules||
|-|-|
|`CASCADE`|Delete together.|
|`SET_NULL`|The attribute will be NULL/|
|`PROTECT`|You can't delete the referenced parent objects.|

<span style='font-size:24px;font-family:Segoe Print'>3. `related_name` supply a name to let you search referenced child object</span>


# what is Relationships?

> <span style='font-size:24px;font-family:Segoe Print'>Django offers ways to define the three most common types of database relationships:</span>

**<span style='font-size:24px;background-color:yellow;color:black;font-family:Segoe Print'>many-to-many</span>**

**<span style='font-size:24px;background-color:yellow;color:black;font-family:Segoe Print'>many-to-one</span>**

**<span style='font-size:24px;background-color:yellow;color:black;font-family:Segoe Print'>one-to-one </span>**