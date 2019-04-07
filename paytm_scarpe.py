import requests
from bs4 import BeautifulSoup
import pprint
import webbrowser
url="https://paytm.com/"
a_=requests.get(url)
# print(a_)
soup=BeautifulSoup(a_.text,"html.parser")
# print(soup)
main_div=soup.find("div",class_="mainContainer _1_Nn")
# print(main_div)
div_=main_div.find_all('div',class_="_3Idz")
list=[]
count=1
for i in div_:
	data_=(i.find('a').get("href"))
	# print(data_)
	list.append(data_)
# pprint.pprint(list)
	name=(i.find('a').text)
	print(count,name)
	count+=1
	# data_=(i.find('a').get("href"))
	# print(data_)
user=int(input("enter the number >>"))
print("             ")
link=list[user-1]
# print(link)
get_=requests.get(link)
# print(get_)
soup=BeautifulSoup(get_.text,"html.parser")
# print(soup)
main_=soup.find('div',class_="_3RA-")
div_=main_.find_all('div',class_="pCOS")
# print(div_)
count=1
for i in div_:
	k=(i.text)
	print(count,k)
	count+=1
print("                           ")
getall=main_.find_all('div',class_="_1fje")
link_list=[]
for i in getall:
	# print(i)
	f_=i.find_all('div',class_="_3WhJ")
	for j in f_:
		m=("https://paytmmall.com"+j.find('a').get('href'))
		link_list.append(m)
# print(link_list)
user1=int(input("enter the link of number >>"))
link_=link_list[user1-1]
# print(link_)

webbrowser.open_new_tab(link_)
	