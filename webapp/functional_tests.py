from selenium import webdriver

server_url = 'http://localhost:8000'
browser = webdriver.Firefox()
browser.get(server_url)

assert 'Django' in browser.title