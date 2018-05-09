from .Userdetails import username,password

header_login = {'Referer': 'https://www.hackerearth.com/login/','Host':'www.hackerearth.com','Upgrade-Insecure-Requests':'1','Connection':'keep-alive','Origin':'https://www.hackerearth.com','Cookie':'user_lang=en-us; __uvt=; HE_USER_EXISTS=True; he_user_homepage_228188=HE_COM; HE_UTS_ID=307dc280976d4183a181b8c44852492c6800330d46eb4e30b31ac46ae40aef1b; HE_UTS_ID_LP="/login/"; HE_UTS_ID_CL=f1d08820c31d491e8f7c4a68d95cc6286cba31db46054100b7d35459af3bcb03; _gat=1; page_lang=en-us; _ga=GA1.2.1352177548.1491475344; user_tz=Asia/Kolkata; lordoftherings="a5dr3g48ag2dg8s2b8r57gkil6ioip74:877ac72a8b89b59fe072d922303b5ada"; csrftoken=bEPmcYT1CrHOip9t193Vl5tnuWyk5kpe7Ig9qwrO0BoIDQ2aGkfpGvfNxsOtiPAE; __ar_v4=FEPHET2J7RHDNBQYLJDVN2%3A20170406%3A31%7COSPXJZLISJAAFPKSSJ6L7U%3A20170406%3A31%7COSWMOTVPPVH3RFCXJFQGQT%3A20170406%3A31; uvts=5rcoDZtKbVrBYXO6; mp_4c30b8635363027dfb780d5a61785112_mixpanel=%7B%22distinct_id%22%3A%20%2215b42dbc142137-0b3eedd97b865c-317d0258-100200-15b42dbc1439e1%22%2C%22url_path%22%3A%20%22%2Flogin%2F%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; mp_mixpanel__c=1','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Content-Type': 'application/x-www-form-urlencoded'}

header_submission = {
'Content-Type': 'application/x-www-form-urlencoded',
'X-Requested-With': 'XMLHttpRequest',
}

form_details={'signin': 'Log In', 'login': username, 'password': password, 'csrfmiddlewaretoken': '1VSQprXvNkmZlr8kUPc47QmlvavXlUMPXZjDDZvibu3TGS11z0oysg8LyGL6ypXf'}



	
