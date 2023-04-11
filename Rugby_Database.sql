USE Rugby_Database;

CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE Team (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    mascot VARCHAR(100) NOT NULL,
    logo_url VARCHAR(255) NOT NULL
);

CREATE TABLE Player (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birthday DATE NOT NULL,
    position VARCHAR(100) NOT NULL,
    grade VARCHAR(100) NOT NULL,
    hometown VARCHAR(100) NOT NULL,
    team_id INT NOT NULL,
    FOREIGN KEY (team_id) REFERENCES Team(id)
);

CREATE TABLE TeamStats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    team_id INT NOT NULL,
    wins INT NOT NULL,
    losses INT NOT NULL,
    points_for INT NOT NULL,
    points_against INT NOT NULL,
    year INT NOT NULL,
    FOREIGN KEY (team_id) REFERENCES Team(id)
);

CREATE TABLE PlayerStats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    games_played INT NOT NULL,
    tries INT NOT NULL,
    conversions INT NOT NULL,
    penalty_kicks INT NOT NULL,
    drop_kicks INT NOT NULL,
    year INT NOT NULL,
    FOREIGN KEY (player_id) REFERENCES Player(id)
);
