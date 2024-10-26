CREATE DATABASE Baseball;
USE Baseball;

CREATE TABLE Team(
    team_ID INT,
    team_name VARCHAR(30),
    PRIMARY KEY(team_ID)
);

CREATE TABLE BattingStatistics(
    stats_ID INT AUTO_INCREMENT,
    AVG DECIMAL(4,3),
    Hits INT,
    HR INT,
    RBI INT,
    PRIMARY KEY(stats_ID)
);

CREATE TABLE Player(
    ID INT AUTO_INCREMENT,
    player_ID INT,
    player_name VARCHAR(30),
    birth_date DATE,
    birth_place VARCHAR(30),
    team_ID INT,
    stats_ID INT,
    PRIMARY KEY(ID),
    FOREIGN KEY (team_ID) REFERENCES Team(team_ID) ON DELETE SET NULL,
    FOREIGN KEY (stats_ID) REFERENCES BattingStatistics(stats_ID) ON DELETE SET NULL
);

INSERT INTO Team (team_ID, team_name) VALUES
(1, 'Los Angeles Dodgers'),
(2, 'San Diego Padres'),
(3, 'New York Yankees'),
(4, 'Arizona Diamondbacks'),
(5, 'San Francisco Giants'),
(6, 'Chicago Cubs'),
(7, 'St. Louis Cardinals'),
(8, 'Boston Red Sox'),
(9, 'Houston Astros'),
(10, 'Atlanta Braves'),
(11, 'Cincinnati Reds'),
(12, 'Cleveland Guardians'),
(13, 'Philadelphia Phillies'),
(14, 'New York Mets'),
(15, 'Washington Nationals'),
(16, 'Miami Marlins'),
(17, 'Milwaukee Brewers'),
(18, 'Pittsburgh Pirates'),
(19, 'Baltimore Orioles'),
(20, 'Toronto Blue Jays'),
(21, 'Tampa Bay Rays'),
(22, 'Chicago White Sox'),
(23, 'Minnesota Twins'),
(24, 'Detroit Tigers'),
(25, 'Kansas City Royals'),
(26, 'Seattle Mariners'),
(27, 'Texas Rangers'),
(28, 'Los Angeles Angels'),
(29, 'Oakland Athletics'),
(30, 'Colorado Rockies');

INSERT INTO BattingStatistics (stats_ID, AVG, Hits, HR, RBI) VALUES
(1, 0.328, 185, 45, 104),
(2, 0.292, 160, 30, 99),
(3, 0.310, 170, 22, 89),
(4, 0.285, 140, 34, 95),
(5, 0.273, 130, 40, 105),
(6, 0.333, 200, 10, 85),
(7, 0.299, 150, 25, 92),
(8, 0.278, 155, 35, 98),
(9, 0.301, 180, 18, 90),
(10, 0.250, 110, 44, 110),
(11, 0.260, 120, 41, 108),
(12, 0.276, 145, 27, 84),
(13, 0.289, 155, 20, 75),
(14, 0.315, 190, 12, 78),
(15, 0.325, 195, 15, 83),
(16, 0.285, 140, 31, 89),
(17, 0.270, 135, 28, 87),
(18, 0.294, 160, 26, 94),
(19, 0.311, 175, 14, 76),
(20, 0.253, 115, 38, 99),
(21, 0.298, 155, 22, 81),
(22, 0.287, 145, 36, 93),
(23, 0.263, 125, 33, 97),
(24, 0.279, 150, 29, 90),
(25, 0.308, 180, 17, 88);

INSERT INTO Player (player_ID, player_name, birth_date, birth_place, team_ID, stats_ID) VALUES
(1, 'Shohei Ohtani', '1994-07-05', 'Japan', 1, 15),
(2, 'Yu Darvish', '1986-08-16', 'Japan', 2, 23),
(3, 'Aaron Judge', '1992-04-26', 'USA', 3, 5),
(4, 'Chien-Ming Wang', '1980-03-31', 'Taiwan', 3, 12),
(5, 'Corbin Carroll', '2000-08-21', 'USA', 4, 19),
(6, 'Mookie Betts', '1992-10-07', 'USA', 1, 7),
(7, 'Mike Trout', '1991-08-07', 'USA', 28, 1),
(8, 'Clayton Kershaw', '1988-03-19', 'USA', 1, 21),
(9, 'Fernando Tatis Jr.', '1999-01-02', 'Dominican Republic', 2, 9),
(10, 'Bryce Harper', '1992-10-16', 'USA', 13, 17),
(11, 'Juan Soto', '1998-10-25', 'Dominican Republic', 15, 4),
(12, 'Ronald Acuña Jr.', '1997-12-18', 'Venezuela', 10, 25),
(13, 'Max Scherzer', '1984-07-27', 'USA', 14, 8),
(14, 'Jacob deGrom', '1988-06-19', 'USA', 27, 13),
(15, 'Freddie Freeman', '1989-09-12', 'USA', 1, 6),
(16, 'Manny Machado', '1992-07-06', 'USA', 2, 18),
(17, 'Jose Altuve', '1990-05-06', 'Venezuela', 9, 3),
(18, 'Nolan Arenado', '1991-04-16', 'USA', 17, 10),
(19, 'Paul Goldschmidt', '1987-09-10', 'USA', 7, 2),
(20, 'George Springer', '1989-09-19', 'USA', 20, 24),
(21, 'J.T. Realmuto', '1991-03-18', 'USA', 13, 11),
(22, 'Francisco Lindor', '1993-11-14', 'Puerto Rico', 14, 20),
(23, 'Yadier Molina', '1982-07-13', 'Puerto Rico', 7, 14),
(24, 'Chris Sale', '1989-03-30', 'USA', 8, 16),
(25, 'Gerrit Cole', '1990-09-08', 'USA', 3, 22);
