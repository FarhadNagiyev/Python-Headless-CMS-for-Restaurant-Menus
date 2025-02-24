import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from product__management import Ui_MainWindow

class ProductApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_imageURL.setMaxLength(1000)
        

        self.ui.pushButton_create.clicked.connect(self.save_to_database)

    def save_to_database(self):
      
        product_name = self.ui.lineEdit_producName.text()
        price = self.ui.doubleSpinBox_price.value()
        image_url = self.ui.lineEdit_imageURL.text()
        description = self.ui.textEdit_description.toPlainText()


        try:
            connection = mysql.connector.connect(
                host="", 
                user="", 
                password="", 
                database=""  
            )
            cursor = connection.cursor()

    
            insert_query = """
                INSERT INTO products (product_name, price, image_url, description)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (product_name, price, image_url, description))
            connection.commit()


            QMessageBox.information(self, "Success", "Product added successfully!")

     
            self.ui.lineEdit_producName.clear()
            self.ui.doubleSpinBox_price.setValue(0.0)
            self.ui.lineEdit_imageURL.clear()
            self.ui.textEdit_description.clear()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductApp()
    window.show()
    sys.exit(app.exec_())
