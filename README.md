# Database-System
Name: 田庚昀
Student ID: R11945043
Department and Grade: 臺大生醫電資所碩三
## Assignment
### HW1 Flask + SQL
Create a table in SQL, and after entering data in the frontend, the input data can be recorded simultaneously in the table within the backend database.  
[HW1 demo video](https://www.youtube.com/watch?v=dMZsB5H3GRw)  
1. I want to record which MLB team and player the registrants support, so I first created a table in test database.
```sql
USE test;

CREATE TABLE mlb (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    team VARCHAR(50) NOT NULL,
    player VARCHAR(50) NOT NULL
);
```
2. Frontend was created to let user enter the data
!
## Final project
