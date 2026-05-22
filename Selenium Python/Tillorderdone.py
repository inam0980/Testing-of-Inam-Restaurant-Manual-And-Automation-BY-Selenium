from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://inam0980.pythonanywhere.com/login/")
driver.maximize_window()
time.sleep(2)


try:
    driver.find_element(By.NAME, "username").send_keys("inam0980")
    driver.find_element(By.NAME, "password").send_keys("inam0980")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    time.sleep(3)
    print("✅ Login successful")
except Exception as e:
    print("❌ Login error:", e)

# Step 2: Open Biryani section
try:
    driver.find_element(By.XPATH, "//h2[contains(text(),'Biryani')]").click()
    time.sleep(3)
    print("✅ Biryani section opened")
except Exception as e:
    print("❌ Biryani Open Error:", e)

# Step 3: Add Hyderabadi Biryani to cart
try:
    driver.find_element(By.CSS_SELECTOR, "a[href='/add-to-cart/1/']").click()
    time.sleep(3)
    print("✅ Hyderabadi Biryani added to cart!")
except Exception as e:
    print("❌ Error adding to cart:", e)

# Step 4: Go to Cart page
try:
    driver.find_element(By.LINK_TEXT, "🛒 Cart").click()
    time.sleep(3)
    print("✅ Navigated to Cart page")
except Exception as e:
    print("❌ Error navigating to cart:", e)

# Step 5: Click Proceed to Checkout
try:
    driver.find_element(By.XPATH, "//a[contains(@href, '/checkout/')]").click()
    time.sleep(3)
    print("✅ Navigated to Checkout page")
except Exception as e:
    print("❌ Error navigating to checkout:", e)

# Step 6: Select Cash on Delivery (COD)
try:
    # COD radio button is already checked by default, but let's ensure it's selected
    cod_radio = driver.find_element(By.XPATH, "//input[@value='COD']")
    if not cod_radio.is_selected():
        cod_radio.click()
        time.sleep(1)
    print("✅ Cash on Delivery selected")
except Exception as e:
    print("❌ Error selecting COD:", e)

# Step 7: Place the order
try:
    place_order_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Confirm & Place Order')]")
    place_order_btn.click()
    time.sleep(3)
    print("✅ Order placed successfully!")
except Exception as e:
    print("❌ Error placing order:", e)

# Verify order confirmation
try:
    # Check for success message
    success_msg = driver.find_element(By.XPATH, "//*[contains(text(),'Order placed') or contains(text(),'successfully') or contains(text(),'confirmed')]")
    print("✅ Order confirmation received!")
except:
    print("⚠️ Check manually if order was placed")

# Keep browser open to see result
input("\nPress Enter to close browser...")
driver.quit()