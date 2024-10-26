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
3. Execute `app.py` to handle the data submitted from the frontend and save it to the SQL database.(`http://127.0.0.1:5000`)
```bash
python app.py
```
![images](https://github.com/GengYunTien/Database-System/blob/main/images/hw1_web.png)
4. SQL database synchronization update in progress.
### HW2 ER moddel + CRUD + Flask
Design an ER model for three entities. Perform CRUD operations on three tables and include at least one join in the final SELECT statement.  
[**HW2 demo video**](https://www.youtube.com/watch?v=dMZsB5H3GRw)  
1. Design a database and its ER diagram. This database includes `Player`, `Team` and `Batting statistics` tables.  
![images](https://github.com/GengYunTien/Database-System/blob/main/images/ERD.png)
## Final project
