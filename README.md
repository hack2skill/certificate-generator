# certificate
Provided with a template image and a CSV containing participants details it will create certificates for each individual and mail them.

Tech Stack- Python

How to run it?

`git clone {url}`

`cd certificate`

`pip install -r requirements.txt`

`python certficate.py`

What will it do?

#### 1st Draft
- an image (template) and a CSV would be provided 
    - -> a webpage to ask for an image and a csv
- an api to loop through the excel and replace the variable (like photoshop)
    - -> to wite a function which does this
- and naming and saving the certificate (like Images in aws/2.0)
    - -> a schema to store images on db

##### Further Features
- to mail their certificate links to individuals
    - > basically forward them the links of aws after shortning
