import sublime
import sys,os
site_path="/usr/lib/python3/dist-packages"
if(site_path not in sys.path):
	sys.path.append(site_path)
import sublime_plugin
from bs4 import BeautifulSoup as bs
import requests
import re,ast 
import json,time
from .Header import header_login,header_submission,form_details


def URLmaker(self):
	target='http'
	content = self.view.substr(sublime.Region(0, self.view.size()))
	begin = content.find(target)
	if begin == -1:
		return
	target_url=self.view.substr(self.view.line(begin))
	target_url=target_url[2:]
	return target_url

def form_create(data,filename):
	with open(filename, 'r') as myfile:
		dt=myfile.read()
	form_problem ={'source':dt,'lang':'CPP','problem_slug' :str(data["problem_slug"]),'private_hash' :str(data["private_url_hash"]),'p_type':str(data["p_type_verbose"]),'problem_type':str(data["p_type_verbose"]),'p_type_h':str(data["p_type_verbose"]) }
	return form_problem

def format_result(data):
	dt=data.find("div",class_="result").find_all("span")
	for span in dt:
		print(span.text)
	print("")
	dt=data.find("div",class_="result-details").find_all("p")
	for span in dt:
		print(span.text)

def submit_sol(self,problem_url,type):
	s = requests.session()
	login = s.get('https://www.hackerearth.com/login')
	response = s.post('https://www.hackerearth.com/login', data=form_details,headers=header_login)
	login = s.get(problem_url)
	soup = bs(login.content)
	p = re.compile('var problem_code_editor_data = (.*);')        
	for script in soup.find_all("script", {"src":False}):
		if script:            
			m = p.search(script.string)
			if m!=None:
				jsonValue = '{%s}' % (m.group(0).split('{', 1)[1].rsplit('}', 1)[0],)
				value = json.loads(jsonValue)

	pg=s.post('https://www.hackerearth.com/'+type+'/AJAX/',data=form_create(value,self.view.file_name()),headers=header_submission,verify=False)
	time.sleep(7)
	print (pg.text)
	login =s.get('https://www.hackerearth.com'+ast.literal_eval(pg.text)['url'])
	soup =bs(login.text)
	print(login.url)
	format_result(soup)

class SubmitCommand(sublime_plugin.TextCommand):	
	def run(self, edit):
		url=URLmaker(self)
		print (url)
		if(url!=None):
			submit_sol(self,url,'submit')

class TestCommand(sublime_plugin.TextCommand):	
	def run(self, edit):
		url=URLmaker(self)
		print (url)
		if(url!=None):
			submit_sol(self,url,'dryrun')
		