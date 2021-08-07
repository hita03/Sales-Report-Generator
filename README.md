# Sales-Report-Generator
This is a project about building a sales data report generator web application using Django and JavaScript, to visualize the sales data, and upload sales records from csv files &amp; generate pdfs.

>A short demo can be found here: <https://youtu.be/Q-AQYTOnpYs>

### Contents of the directory
`src` folder contains source code, `Data.csv` is the file that we will upload, through which sales objects will be created. They will reflect in the dates we select (on the Home page) to generate a report.
`requirements.txt` contains all the packages/libraries used, that have to be installed in order to run this project.

### Contents of the src (source code) directory

This Django project is called `reports_proj` and has 5 applications, `customers`,`profiles`,`reports`,`products` and `sales`.
`customers` gets and creates customers from the data files uploaded. Optionally, a picture for the customer can also be provided. Customer's profile image defaults to `no_picture.png` in the `media` folder. Although it has no urls, it's required as a Foreign Key because we have associate every customer with their transactions, and the products they purchase.

`products` is an application where objects of products are created. A product name, selling price, and optional picture is provided. This application can be potentially used to provide details of every product, and a log file of the number of units and demand of each product in the market. But I have used it's model as a Foreign Key in almost every application, because the foundation of this project lies in the sale of various products.

`sales` is the main application, it has 3 models, `Sale`, `Csvs` and `Positions`. They are used to store the customer, product, quantity, total price, transaction id, associated salesman for every instance. `Csvs` is used to created a csv object of the file uploaded (using a FileField), a name, and created date.

`reports` application deals with the creating objects that store the chart image (Line,Bar,Donut), the name and remarks associated with the report, and the author. Using this, one can generate visual charts b/w desired dates to analyze data.

`profiles` is the description of the salesman/author here, who is recording and adding reports in his/her company. This was an additional 'top on' to add some personality to the employee(salesman). The user's profile is automatically created when they register,and they can add their profile pictures and a short introduction that they can update anytime.ModelForms was used to implement this.

`templates` folder houses the base and navbar html files that all other html files are extended from.
`media` houses `csvs` folder where uploaded files are stored, `customers` folder stores images of the customer(can refer Customer model from `customers` app), `reports` folder stores images of all the reports added by salesman, `avatars` folder stores pictures of all users profile(can refer avatar Profile model from `profiles`app) and a default "no_picture.png" for every image field in a model.

### Installation

`cd` to the directory where requirements.txt is located.

Create and activate your virtual environment:
`virtualenv venv`
`venv\Scripts\Activate`

Run `pip install -r requirements.txt` in your shell.
This installs the required packages to run the application.

`cd` to src directory.
Run `python manage.py makemigrations` followed by `python manage.py migrate`
Create a superuser that has access to Django Admin: `python manage.py createsuperuser`
Start the development server with `python manage.py runserver` and login with the superuser's credentials

### Specifications

#### Upload

>Click on `Upload` in the navigation bar. A drag and drop framed web page opens.
>Start by uploading your sales report called Data.csv, by dragging and dropping it onto the bordered frame.
>A success alert denotes successful upload of the file.
>Duplicate files cannot be uploaded. Only `.csv` files can be uploaded.
>Respective alerts are displayed to handle these exceptions.

We're grabbing a file and based on this file we are creating a csv object.
On uploading, sales objects of the product and sales are created,as well as getting or creating customers from the data.Now we can generate a report of this data in tabular form and charts.

#### Home

>Click on `Home` in the navigation bar.
>Fill in to and from dates, the chart type, and how you want results to be grouped by(transation or sales data).>Click Search.

Dataframes are generated and displayed in a tabular column, along with a visual representaion (Bar chart, Line chart, Donut/Pie chart).
Us, being the salesman, can add a report of this data. Click on `Add Report` and fill in the required fields. This part was implmented using bootstrap Modals.

#### Reports

>To view the reports added, click on `Reports` in the navigation bar.

All reports added previously by salesman are displayed in reverse chronological order. Clicking on `Details` displays additional information, and `Generate PDF` allows us to view and save as `.pdf` form of the same report. So one can actually store their report locally instead of accessing the website for it repeatedly.

#### Sales

>To view the sales info, click on `Sales` in the navigation bar.

All transaction id's are displayed, that hyperlink to information about that transaction such as the salesman who brought that transaction through, the customer company name and logo, their purchases items,quantity and total price, all in a tabular format. This way, navigating to the transaction id displays all information one could ever need about that purchase.

#### Profiles

>When you create an account, your profile is automaticallu created. Click on the top-right dropdown, `Profile`.

You can add your profile image, as well as a short introduction(Bio). `Update` saves your changes.

#### Logout

>Logout from the top-right dropdown. Access to navbar is not allowed once you logout.

#### Distinctiveness and Complexity

This projects draws upon the fields of marketing, analyzing sales data & generating reports. As the CS50W projects focus on social media, profile building, e-commerce and mailing, I believe this project is sufficiently distinct from those subject matters.
This project is based on **Django** for backend and **JavaScript**,**HTML**,**CSS** as frontend. 
It also renders templates such that they shrink or fit the layout of that of a mobile.

Working with Dataframes(pandas), generating charts and creating images was totally new (can refer `utils.py` of `sales` application), I believe it made the project more complex. There are so many ways to implement plotting graphs and so many methods, attributes that can be added, I learned so much by reading the pandas and matplotlib docs in order to make changes to charts the way I wanted them to be. 

Dropzone JS, a javascript library, is popularly used as it's an easy way to upload multiple files and supports drag and drop uploads. Since this appliation is primarily useful on the web, accessed on a computer, Drpozone JS was the most convenient way to upload files.Their docs were comprehensive, provided a thorough understanding of various methods.

I came across a lot of Bootstrap tags and elements, such as **Modals**, **Cards**, **Alerts**, **Dropdowns** and **Tables** that I experimented with in this project, which I did not/was not required in completing the other CS50W Projects' requirements.
