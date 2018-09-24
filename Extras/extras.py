#THIS COMMENTED CODE IS FOR SPREADSHEETS
#scope = ['https://spreadsheets.google.com/feeds']
#creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
#client = gspread.authorize(creds)

#sheet = client.open('HQTRIV').sheet1
#row = [question, a, b, c]
#index = 1
#sheet.insert_row(row, index)
#pp = pprint.PrettyPrinter()
#qa = sheet.get_all_records()
#pp.pprint(qa)


#def google_search(search_term, api_key, cse_id, **kwargs):
   # service = build("customsearch", "v1", developerKey=api_key)
   # res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
   # return res['items']    

#results = google_search(
   # (question + " " + a), my_api_key, my_cse_id, num=10)
#for result in results:
    #pprint.pprint(result)
