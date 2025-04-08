from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialisation du navigateur (assurez-vous d'avoir le pilote du navigateur installé)
driver = webdriver.Chrome()

# Ouverture du site web
driver.get("https://")

# Test de la page de connexion
def test_login():
    # Sélection de l'élément "Nom d'utilisateur" et saisie des informations
    username_input = driver.find_element(By.ID, "email")
    username_input.send_keys("cherifsouhail@gmail.com")

    # Sélection de l'élément "Mot de passe" et saisie des informations
    password_input = driver.find_element(By.ID, "pass")
    password_input.send_keys("55488755")

    # Clic sur le bouton "Connexion"
    wait = WebDriverWait(driver, 100)
    login_button = wait.until(EC.presence_of_element_located((By.NAME, "login")))
    login_button.click()

    # Vérification du succès de la connexion (vous devrez adapter cela à votre site web spécifique)
    assert "Bienvenue" in driver.page_source
    driver.quit()

# Test de l'inscription
def test_signup():
    # Clic sur le lien "S'inscrire"
    wait = WebDriverWait(driver, 10)
    signup_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Créer un compte')]")))
    signup_link.click()

    # Sélection de l'élément "Nom d'utilisateur" et saisie des informations
    username_input = driver.find_element(By.NAME, "firstname")
    username_input.send_keys("Souhail")

    # Sélection de l'élément "Prénom d'utilisateur" et saisie des informations
    usersurname_input = driver.find_element(By.NAME, "lastname")
    usersurname_input.send_keys("Cherif")

    # Sélection de l'élément "email" et saisie des informations
    username_input = driver.find_element(By.NAME, "reg_email__")
    username_input.send_keys("cherifsouhail30@gmail.com")

    # Sélection de l'élément "Mot de passe" et saisie des informations
    password_input = driver.find_element(By.NAME, "reg_passwd__")
    password_input.send_keys("123456789Souhail")

    # Clic sur le bouton "S'inscrire"
    signup_button = driver.find_element(By.NAME, "websubmit")
    signup_button.click()

    # Vérification du succès de l'inscription (vous devrez adapter cela à votre site web spécifique)
    assert "Bienvenue, nouvel_utilisateur" in driver.page_source
    driver.quit()

# Test de clic sur un bouton (exemple)
def test_button_click():
    # Clic sur un bouton (vous devrez adapter cela à votre site web spécifique)
    button_element = driver.find_element(By.ID, "bouton-id")
    button_element.click()

    # Vérification de l'effet du clic (vous devrez adapter cela à votre site web spécifique)
    assert "Action réussie" in driver.page_source

# Exécution des tests
test_login()
test_signup()
#test_button_click()

# Fermeture du navigateur
driver.quit()
