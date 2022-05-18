############ xattr -d com.apple.quarantine chromedriver 

import time
import selenium
from selenium import webdriver
import re


def CheckAbuseIpDb(line):
    ip = line
    url = "https://www.abuseipdb.com/check/"+ip
    driver = webdriver.Chrome('/Users/alit/Desktop/CTI/Tools/chromedriver')
    driver.get(url)
    labels = driver.find_elements_by_tag_name("p")
    for label in labels:
        if re.search('Confidence of Abuse is',label.text):
            securityScore = label.text.split(" ")[-1]
            securityScore = securityScore.split("%")[0]
            break

    driver.close()

    try:
        if int(securityScore) >= 50:
            with open("abuseips.txt","a") as file:
                data = str(securityScore)+','+str(ip)
                file.write(data)
                file.write("\n")

    except UnboundLocalError:
        securityScore = 0

                    
if __name__ == "__main__":
    with open("ips.txt") as file:
        i = 1
        for line in file:
            if not line.strip():
                i = i +1
                continue
            else:
                CheckAbuseIpDb(line)
                print(i,line)
                i = i + 1
