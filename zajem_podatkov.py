import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

opts = Options()
opts.add_argument("--headless=new")  # Selenium ne odpira browswer okna
driver = webdriver.Chrome(options=opts)  # Selenium izbire Chrome kot browser
try:
	for leto in range(2019, 2026): # Leta tekmovanj ki nas zanimajo
		data_url = f"https://www.worldcubeassociation.org/competitions/SlovenianNationals{leto}/results/all?event=333" # Url template za Slovenian Nationals, 3x3x3 event
		try:
			driver.get(data_url)
			
			# V primeru da Seleniumu ne uspe dostopati do podatkov v 5 sekundah naredimo exception (npr za leta ko tekmovanja ni bilo ali podatki niso dostopni)
			WebDriverWait(driver, 5).until(
				lambda d: "results-data" in d.page_source
			)
			print(f"Pridobivanje podatkov uspešno za {data_url}")
			
			# Shranimo podatke, da ni potrebno vsakič znova pobirati podatke, ko želimo dostopati do njih
			results_file_url = f"datoteke/html/SlovenianNationals{leto}.html"
			competition_html = driver.page_source
			with open(results_file_url, "w", encoding="utf-8") as file:
				file.write(competition_html)
				print(f"SlovenianNationals{leto} shranjeno")
			time.sleep(1.0)	# Čakamo sekundo, da nas spletna stran ne začne blokirati
			
        # Exception če nam podatkov za določeno leto ni uspelo dobiti
		except TimeoutException:
			print(f"Pridobivanje podatkov neuspešno za {data_url}")
			pass
finally:
	driver.quit()
	print("Podatki pridobljeni.")