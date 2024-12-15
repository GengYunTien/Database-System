# Database-System
Name: 田庚昀  
Student ID: R11945043  
Department and Grade: 臺大生醫電資所碩三  
## Assignment
### HW1 Flask + SQL
Create a table in SQL, and after entering data in the frontend, the input data can be recorded simultaneously in the table within the backend database.  
[**HW1 demo video**](https://www.youtube.com/watch?v=dMZsB5H3GRw)  
1. I want to record which MLB team and player the registrants support, so I first created a table in the SQL database.
```sql
USE test;

CREATE TABLE mlb (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    team VARCHAR(50) NOT NULL,
    player VARCHAR(50) NOT NULL
);
```
2. `index.html` and `styles.css` build the frontend.
3. Execute `app.py` to handle the data submitted from the frontend and save it to the SQL database.  
```bash
python app.py
```
![images](https://github.com/GengYunTien/Database-System/blob/main/images/hw1_web.png)
4. SQL database synchronization update in progress.
### HW2 ER model + CRUD + Flask
Design an ER model for three entities. Perform CRUD operations on three tables and include at least one join in the final SELECT statement.  
[**HW2 demo video**](https://youtu.be/e3vzn5QgC_8)  
1. Create a `Baseball` database and its ER diagram. This database includes `Player`, `Team` and `Batting statistics` tables for building baseball player management system.  
![images](https://github.com/GengYunTien/Database-System/blob/main/images/ERD.png)  
2. `create.py`, `read.py`, `update.py` and `delete.py` for CRUD operation.  
3. `join.py` for SQL JOIN and SELECT queries.  
4. Execute `app.py` to handle the CRUD, JOIN and SELECT queries.
```bash
python app.py
```
![images](https://github.com/GengYunTien/Database-System/blob/main/images/hw2_web_1.png)  
![images](https://github.com/GengYunTien/Database-System/blob/main/images/hw2_web_2.png)  
![images](https://github.com/GengYunTien/Database-System/blob/main/images/hw2_web_3.png)  
![images](https://github.com/GengYunTien/Database-System/blob/main/images/hw2_web_4.png)  
5. SQL database synchronization update in progress.
### HW3 MongoDB + Flask
First, use MongoDB Compass to show the content in the database. Then, switch to the front-end web app to demonstrate the create operation. Finally, switch back to MongoDB Compass to display the newly inserted data.  
[**HW3 demo video**](https://www.youtube.com/watch?v=-epHmxeMLyc)  
1. Design a `Baseball` database in MongoDB.
2. `index.html` and `styles.css` build the frontend to provide the service that offer the baseball game spectator to record their game viewing reflections.
3. Execute `app.py` to handle the data submitted from the frontend and save it to the MongoDB.  
```bash
python app.py
```
![images](https://github.com/GengYunTien/Database-System/blob/main/images/hw3_web_1.png)
4. MongoDB synchronization update in progress.
### HW4 MongoDB + CRUD + Flask
First, use MongoDB Compass to show the content in the database. Then, perform a CRUD operation in the frontend web.  
[**HW4 demo video**](https://youtu.be/TOfzC6-55Lk)  
1. Design a `Baseball` database in MongoDB.
2. `index.html`, `view.html`, `edit.html` and `styles.css` build the frontend to provide the service that offer the baseball game spectator to record their game viewing reflections.
3. Execute `app.py` to handle the CRUD.
```bash
python app.py
```
![images](https://github.com/GengYunTien/Database-System/blob/main/images/hw4_web_1.png)  
![images](https://github.com/GengYunTien/Database-System/blob/main/images/hw4_web_2.png)  
![images](https://github.com/GengYunTien/Database-System/blob/main/images/hw4_web_3.png)  
4. MongoDB synchronization update in progress.
## Final project
[**Final project demo video**](https://youtu.be/TOfzC6-55Lk)  
1. Design a `Tourist spots` database in MongoDB.
2. `index.html`, `view.html`, `edit.html` and `styles.css` build the frontend to provide the service that offer the tourists to record their travel experience .
3. Execute `app.py` to handle the CRUD.
```bash
python app.py
```
![images](https://github.com/GengYunTien/Database-System/blob/main/images/final_project_web_1.png)  
4. MongoDB synchronization update in progress.
