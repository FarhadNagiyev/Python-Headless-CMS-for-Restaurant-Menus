# Setting Up the Database

## Step 1: Open MySQL and Create a Database
First, ensure that MySQL is installed and running on your system. Open MySQL and create a new database using the following command:

```sql
CREATE DATABASE your_database_name;
```

## Step 2: Create a Table
Within the newly created database, create a table to store product information. Use the following SQL command:

```sql
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    image_url TEXT,
    description TEXT
);
```

This table consists of:
- `id` → A unique identifier for each product.
- `product_name` → The name of the product (required).
- `price` → The price of the product, stored as a decimal value.
- `image_url` → The URL or path to the product image.
- `description` → A text field to describe the product.

## Step 3: Configure the Database Connection in `main.py`
To connect your Python application to the MySQL database, update the following lines in `main.py` with your database credentials:

```python
import mysql.connector

connection = mysql.connector.connect(
    host="your_host",  # e.g., 'localhost' or an external MySQL server
    user="your_username",  # Your MySQL username
    password="your_password",  # Your MySQL password
    database="your_database_name"  # The name of the database you created
)
```

## Additional Notes:
- Ensure that you have the `mysql-connector-python` package installed. If not, install it using:
  ```bash
  pip install mysql-connector-python
  ```
- Make sure MySQL is running before executing the script.
- If you are connecting to a remote database, ensure that your firewall and MySQL settings allow external connections.

