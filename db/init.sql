
USE newecommerce;

CREATE TABLE product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    price DECIMAL(10,2)
);

INSERT INTO product (name, price) VALUES ('Sample Product', 19.99);
