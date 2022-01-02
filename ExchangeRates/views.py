from django.shortcuts import render
import bs4
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import openpyxl
from .models import Currency

def main(request):
	return render(request,'ExchangeRates/main.html')

def index(request):
	country=['USD','EUR','JPY','BGN','AUD','BRL','CAD','IDR','MYR','NZD']
	currencies=[]
	abbrs=[]
	for i in range(0,len(country)):
		r=requests.get('https://www.iban.com/currency-converter?from_currency=INR&to_currency='+ str(country[i])+'&amount=1')
		soup=bs4.BeautifulSoup(r.text,"xml")
		currencies.append(soup.find_all('strong')[1].text)
		abbrs.append(soup.find_all('tr')[1].find_all('td')[2].text)
		localtime=time.asctime(time.localtime(time.time()))
		i=i+1
	
	currency_rates=pd.DataFrame({'Currency_Name':abbrs,'curr':currencies,})
	localtime = time.asctime( time.localtime(time.time()) )

	df= pd.read_excel("dummy.xlsx")
	# print(df)

	# print("Currencies",currencies)
	df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
	df[localtime]=currencies
	df.to_excel("dummy.xlsx")

	df2 = pd.DataFrame(
        {
            localtime:currencies,
        })
	


	# df[localtime] = df2
	# df.to_excel("output.xlsx")
	# df1.to_csv('mydata1.csv')
	# a = pd.read_csv("mydata1.csv")

	return render(request,'ExchangeRates/index.html',context={'form':currency_rates})

def indextwo(request):
	country=['USD','EUR','JPY','BGN','AUD','BRL','CAD','IDR','MYR','NZD']
	currencies=[]
	abbrs=[]
	for i in range(0,len(country)):
		r=requests.get('https://www.x-rates.com/calculator/?from=INR&to='+str(country[i])+'&amount=1')
		soup=bs4.BeautifulSoup(r.text,"xml")
		currencies.append(soup.find_all('span',class_="ccOutputRslt")[0].text)
		abbrs.append(soup.find_all('span',class_="ccOutputCode")[0].text)
		localtime=time.asctime(time.localtime(time.time()))
		i=i+1
	
	currency_rates=pd.DataFrame({'Currency_Name':abbrs,'curr':currencies,})
	df= pd.read_excel("Book2.xlsx")
	print(df)

	print("Currencies",currencies)
	df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
	df[localtime]=currencies
	df.to_excel("Book2.xlsx")

	return render(request,'ExchangeRates/indextwo.html',context={'form':currency_rates})

def indexthree(request):
	country=['USD','EUR','JPY','BGN','AUD','BRL','CAD','IDR','MYR','NZD']
	currencies=[]
	abbrs=[]
	for i in range(0,len(country)):
		r=requests.get('https://transferwise.com/gb/currency-converter/inr-to-'+str(country[i])+'-rate?amount=1')
		soup=bs4.BeautifulSoup(r.text,"xml")
		currencies.append(soup.find_all('span',class_="text-success")[0].text)
		abbrs.append(soup.find_all('span')[0].text)
		localtime=time.asctime(time.localtime(time.time()))
		i=i+1
	
	currency_rates=pd.DataFrame({'Currency_Name':country,'curr':currencies,})
	df= pd.read_excel("Book3.xlsx")
	print(df)

	print("Currencies",currencies)
	df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
	df[localtime]=currencies
	df.to_excel("Book3.xlsx")

	return render(request,'ExchangeRates/indexthree.html',context={'form':currency_rates})




	
