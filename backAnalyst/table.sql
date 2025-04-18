CREATE DATABASE IF NOT EXISTS arqui;
USE arqui;
CREATE TABLE IF NOT EXISTS Product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    amount INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Notification (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    time TIME NOT NULL,
    product_id INT NOT NULL
);

INSERT INTO Product (name, amount) VALUES ("Producto A", 15);
INSERT INTO Product (name, amount) VALUES ("Producto B", 20);
INSERT INTO Product (name, amount) VALUES ("Producto C", 25);
INSERT INTO Product (name, amount) VALUES ("Producto D", 13);
INSERT INTO Product (name, amount) VALUES ("Producto E", 30);