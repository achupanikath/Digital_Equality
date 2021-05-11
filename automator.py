import csv
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def installer():
	print("Hello! We are going to download some softwares for you to improve your base level security")
	antivirus = ""
	vpn = ""
	website = ""
	with open('CompanyData.csv') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0

	    for row in csv_reader:
	        if line_count == 0:
	            print(f'Column names are {", ".join(row)}')
	            line_count += 1
	        else:
	            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
	            website = row[6]
	            antivirus = row[4]
	            vpn = row[5]
	            line_count += 1
	    print(f'Processed {line_count} lines.')
	if antivirus != 'None':
		if antivirus == 'malwarebytes':
			url = 'https://downloads.malwarebytes.com/file/mb-windows'
			wget.download(url, '/Users/achup/DE_MBSetup.exe')
			print('Downloaded anitvirus. Please complete installation.')
		elif antivirus == 'panda':
			url = 'http://acs.pandasoftware.com/Panda2015/FREEAV/173653/FREEAV.exe'
			wget.download(url, 'Users/achup/DE_PandaSetup.exe')
			print('Downloaded anitvirus. Please complete installation.')
		elif antivius == 'kaspersky':
			url = 'https://aes.s.kaspersky-labs.com/administrationkit/ksc10/12.2.0.4376/english-US-5560019/3337393130367c44454c7c31/ksc_12.2_Console_en.exe'
			wget.download(url, 'Users/achup/DE_Kaspersky.exe')
			print('Downloaded anitvirus. Please complete installation.')
		elif antivirus == 'avira':
			url = 'https://www.avira.com/en/start-download/product/1129/RnZHNUpuemRxeTdRV2hiZ2NGaENQTFQzNy8yRHRwb0UxekZIaktpOG1Rb2JSdG5IK01Xc0wrY0J2dz09?utm_source=CS&utm_medium=KB'
			wget.download(url, 'Users/achup/DE_Avira.exe')
			print('Downloaded anitvirus. Please complete installation.')
	#ExpressVPN","Private InternetAccess", "IPVanish","CyberGhost"
	if vpn != 'None':
		if vpn == 'ExpressVPN':
			url = 'https://www.expressvpn.com/order'
			webbrowser.open(url, new=2)
			print('Opened vpn on website. Please complete installation.')

		elif vpn == 'Private InternetAccess':
			url = 'https://www.privateinternetaccess.com/'
			webbrowser.open(url, new=2)		
			print('Opened vpn on website. Please complete installation.')
		elif vpn == 'IPVanish':
			url = 'https://www.ipvanish.com/'
			webbrowser.open(url, new=2)
			print('Opened vpn on website. Please complete installation.')

		elif vpn == 'CyberGhost':
			url = 'https://www.cyberghostvpn.com/en_US/'
			webbrowser.open(url, new=2)
			print('Opened vpn on website. Please complete installation.')
	# print("response", response)
	return website

def web_checker(url):
	print("Checking the health of your website...")
	driver = webdriver.Firefox()
	driver.get("https://www.virustotal.com/gui/home/url")
	assert "VirusTotal" in driver.title
	driver.implicitly_wait(10)
	# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".omnibar")))
	elem = driver.switch_to.active_element
	elem.send_keys(url)
	elem.send_keys(Keys.RETURN)
	# '/div/div/div[1]'
	# '/vt-ui-generic-card/div[1]/div[1]/div/p'
	driver.implicitly_wait(100000)
	time.sleep(10)
	# myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.positives')))
	print("Page is ready!")
	driver.execute_script('window.print();')
	# except TimeoutException:
	# 	print("Loading took too much time!")
	driver.quit()
#implemetn dynamic scan

def companySecurity():
    # Use a breakpoint in the code line below to debug your script.
	companyName = input("Company Name: \n")
	name = input("Name: \n")
	pos = input("Company Position: \n")
	WFH = input("Do you work from home: \n")
	vpn = input("Do you use a vpn? \n")
	if not vpn:
		vpn = "None"
	url = input("Enter the url of your website: \n")
	if not url:
		url = "None"
	antiVirus = input("Current antivirus: \n")
	if not antiVirus:
		antiVirus = "None"
	with open('CompanyData.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([companyName])
		writer.writerow(["SN","Name", "Job position", "Where they work", "Antivirus","VPN", "Website"])
		writer.writerow([1, name, pos, WFH, antiVirus, vpn, url])

def sslChecker(url):
	#newsearchurlinput
	print("Checking the ssl security of your website...")
	driver = webdriver.Firefox()
	driver.get("https://ssltools.digicert.com/checker/views/checkInstallation.jsp")
	time.sleep(20)
	assert "Check Website Security | DigiCert SSLTools" in driver.title
	driver.implicitly_wait(10)
	elem = driver.switch_to.active_element
	elem.send_keys(url)
	elem.send_keys(Keys.RETURN)
	driver.implicitly_wait(10)
	time.sleep(30)
	driver.execute_script('window.print();')
	driver.quit()

def vulnerabilityTest(url):
	#https://sitecheck.sucuri.net/
	print("Checking the vulnerailities of the website...")
	driver = webdriver.Firefox()
	driver.get("https://sitecheck.sucuri.net/")
	time.sleep(10)
	assert "Sucuri SiteCheck - Free Website Security Check & Malware Scanner" in driver.title
	driver.implicitly_wait(10)
	elem = driver.switch_to.active_element
	elem.send_keys(url)
	elem.send_keys(Keys.RETURN)
	driver.implicitly_wait(10)
	time.sleep(10)
	driver.execute_script('window.print();')
	driver.quit()

def db_migration():
	print("Please complete the download of the following software to kick off DB migration for better asset management")
	url = 'https://studio3t.com/download/'
	webbrowser.open(url, new=2)

if __name__ == '__main__':
	companySecurity()
	website = installer()
	# website = 'itflux.com'
	web_checker(website)
	sslChecker(website)	
	vulnerabilityTest(website)
	#t3 download and instaLl
	db_migration()

