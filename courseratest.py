from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

#driver = webdriver.Chrome("C:\\Users\\nayni\\Downloads\\chromedriver\\chromedriver.exe")

# {Subject name: Url of all courses from that subject}
subject_dict = {"machine learning":"https://www.coursera.org/search?query=machine+learning", 
"deep learning":"https://www.coursera.org/search?query=deep+learning", 
"cyber security":"https://www.coursera.org/search?query=cyber+security", 
"web development":"https://www.coursera.org/search?query=web+development", 
"frontend development":"https://www.coursera.org/search?query=frontend+development",
"backend development":"https://www.coursera.org/search?query=backend+development", 
"data science":"https://www.coursera.org/search?query=data+science",
"android":"https://www.coursera.org/search?query=android",
"artificial intelligence":"https://www.coursera.org/search?query=artificial+intelligence"}

url = subject_dict["machine learning"]

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
main_body = soup.find("div",class_= "tab-contents")
#print(main_body.text)
all_courses = main_body.find_all("div",class_= "vertical-box")

for course in all_courses:
    course_name = course.find("h2", class_ = "color-primary-text card-title headline-1-text")
    course_rating = course.find("span", class_ = "ratings-text")
    print(course_name.text)
    print(course_rating.text)


'''driver.get(url)

all_links = driver.find_element_by_class_name("tab-contents")
print(all_links)
driver.close()'''
