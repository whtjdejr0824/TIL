from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1000")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser/detect/what-is-my-user-agent"
browser.get(url)