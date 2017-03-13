﻿import urllib.request
from bs4 import BeautifulSoup
import urllib.error

def getPowerRate(area,building,floor,room):
		#请求的链接
	url = "http://202.114.18.218/main.aspx"

	#请求的头信息
	head = {}
	head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'

	#请求所带的数据:

	data = {}
	# data['programId']='韵苑一期'
	# data['txtyq']='韵苑27栋'
	# data['txtld']='6层'
	# data['Txtroom']='604'
	
	data['programId']=area
	data['txtyq']=building
	data['txtld']=floor
	data['Txtroom']=room
	
	data['ImageButton1.x']='14'
	data['ImageButton1.y']='11'
	
	# data['TextBox2']=''
	# data['TextBox3']=''

	data['__EVENTTARGET']=''
	data['__EVENTARGUMENT']=''
	data['__LASTFOCUS']=''
	
	# 以下两段可以通过审查元素-main-formdata获得，不同区域对应不同code
	
	data['__EVENTVALIDATION']='/wEWJQLvrtPHDwLorceeCQLc1sToBgL+zqXMDgK50MfoBgKhi6GaBQLdnbOlBgLtuMzrDQLrwqHzBQKX+9a3BAK/j9m4DALWzqKWBQLWzrbxDALWzprcCwKXit7RAQLL5dCOCgKMofDMCwKhuJKnDgLG17QSAvvu1owKApCEy+cMArWT7dIGAprFqpEOAr/czAsClJSw2ggCg5T44w4CgpT44w4CgZT44w4CgJT44w4Ch5T44w4ChpT44w4Cj5S8ngIC+tXaqwYC0sKZ0wgC0sLV5AIC7NH22QwC7NGKtQU5kESRVPiwyswp+TtV+OuSCdxk4w=='

	data['__VIEWSTATE']='/wEPDwULLTEyNjgyMDA1OTgPZBYCAgMPZBYKAgEPEA8WBh4NRGF0YVRleHRGaWVsZAUM5qW85qCL5Yy65Z+fHg5EYXRhVmFsdWVGaWVsZAUM5qW85qCL5Yy65Z+fHgtfIURhdGFCb3VuZGdkEBUHBuS4nOWMugznlZnlrabnlJ/mpbwG6KW/5Yy6DOmfteiLkeS6jOacnwzpn7Xoi5HkuIDmnJ8G57Sr6I+YCy3or7fpgInmi6ktFQcG5Lic5Yy6DOeVmeWtpueUn+alvAbopb/ljLoM6Z+16IuR5LqM5pyfDOmfteiLkeS4gOacnwbntKvoj5gCLTEUKwMHZ2dnZ2dnZxYBAgRkAgUPEA8WBh8ABQbmpbzlj7cfAQUG5qW85Y+3HwJnZBAVDwnlraboi5HmpbwL6Z+16IuRMTDmoIsL6Z+16IuRMTHmoIsL6Z+16IuRMTLmoIsK6Z+16IuRMeagiwvpn7Xoi5EyN+agiwrpn7Xoi5Ey5qCLCumfteiLkTPmoIsK6Z+16IuRNOagiwrpn7Xoi5E15qCLCumfteiLkTbmoIsK6Z+16IuRN+agiwrpn7Xoi5E45qCLCumfteiLkTnmoIsLLeivt+mAieaLqS0VDwnlraboi5HmpbwL6Z+16IuRMTDmoIsL6Z+16IuRMTHmoIsL6Z+16IuRMTLmoIsK6Z+16IuRMeagiwvpn7Xoi5EyN+agiwrpn7Xoi5Ey5qCLCumfteiLkTPmoIsK6Z+16IuRNOagiwrpn7Xoi5E15qCLCumfteiLkTbmoIsK6Z+16IuRN+agiwrpn7Xoi5E45qCLCumfteiLkTnmoIsCLTEUKwMPZ2dnZ2dnZ2dnZ2dnZ2dnFgECBWQCCQ8QDxYGHwAFCealvOWxguWPtx8BBQnmpbzlsYLlj7cfAmdkEBUHBDHlsYIEMuWxggQz5bGCBDTlsYIENeWxggQ25bGCCy3or7fpgInmi6ktFQcEMeWxggQy5bGCBDPlsYIENOWxggQ15bGCBDblsYICLTEUKwMHZ2dnZ2dnZ2RkAhcPPCsADQBkAhkPPCsADQBkGAMFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBQxJbWFnZUJ1dHRvbjEFDEltYWdlQnV0dG9uMgUJR3JpZFZpZXcxD2dkBQlHcmlkVmlldzIPZ2T56y/jtUkVTAtj5OOymeljGnm1WQ=='

	#数据解析
	data = urllib.parse.urlencode(data).encode('utf-8')

	#生成请求
	req = urllib.request.Request(url,data,head)

	#获取并解析请求得到的回复
	try:
		response = urllib.request.urlopen(req)
	except urllib.error.URLError as e:
		print(e.reason)
	else:
		#对回复读取并解码
		html = response.read().decode('utf-8')

		#通过BeautifulSoup来解析html
		soup =BeautifulSoup(html,"html.parser")
		rest2 = soup.findAll('table',attrs={"rules" : "all"})
		r = rest2[0].findAll('td')
		result = r[1].string+' 剩余电量 '+r[0].string+'度'
		# print(result)
		return result

print(getPowerRate('韵苑一期','韵苑27栋','6层','604'))