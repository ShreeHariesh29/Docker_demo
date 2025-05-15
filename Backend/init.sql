CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    description TEXT
);

INSERT INTO products (name, price, description) VALUES
('Product1', 19.99, 'Description of product 1'),
('Product2', 29.99, 'Description of product 2');