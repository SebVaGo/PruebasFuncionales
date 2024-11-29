import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner  # Asegúrate de instalar esta librería: pip install html-testRunner

class AgroWebTests(unittest.TestCase):

    def setUp(self):
        """Configura el navegador antes de cada prueba."""
        self.driver = webdriver.Chrome()  # Asegúrate de tener el ChromeDriver instalado
        self.driver.implicitly_wait(10)
        self.driver.get("https://agro-front-v2.vercel.app/")

    def test_homepage_title(self):
        """Verificar que el título de la página sea 'AgroWeb'."""
        title_element = self.driver.find_element(By.CLASS_NAME, "text-5xl")
        self.assertEqual(title_element.text, "AgroWeb", "El título no coincide.")

    def test_invalid_login(self):
        """Probar el login con credenciales incorrectas."""
        driver = self.driver

        # Localizar los campos
        correo_input = driver.find_element(By.ID, "correo")
        clave_input = driver.find_element(By.ID, "clave")
        login_button = driver.find_element(By.XPATH, "//button[text()='Login']")

        # Ingresar credenciales incorrectas
        correo_input.send_keys("correo@invalido.com")
        clave_input.send_keys("claveIncorrecta")
        login_button.click()

        # Esperar hasta que el mensaje de error sea visible
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'text-red-600')]"))
        )

        # Validar que el texto del mensaje es el esperado
        self.assertEqual(error_message.text, "Fallo en el inicio de sesión.", "El mensaje de error no es el esperado.")

    def test_redirect_to_register(self):
        """Verificar que el enlace 'Regístrate aquí' redirige a la página correcta."""
        register_link = self.driver.find_element(By.LINK_TEXT, "Regístrate aquí.")
        register_link.click()
        self.assertEqual(self.driver.current_url, "https://agro-front-v2.vercel.app/register", "La redirección falló.")

    def tearDown(self):
        """Cierra el navegador después de cada prueba."""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='reportes')  # Carpeta para guardar los reportes
    )
