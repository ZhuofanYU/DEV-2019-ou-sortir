from urllib import request
import json
def get_data_from_API(url):
    with request.urlopen(url) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        # for k, v in f.getheaders():
        #     print('%s: %s' % (k, v))
        data_decoded = data.decode('utf-8')
        print('Data:',data_decoded)
    return data_decoded

def get_data_from_API_with_head(url):
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0')
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        # for k, v in f.getheaders():
        #     print('%s: %s' % (k, v))
        data_decode = f.read().decode('utf-8')
        data_decode = json.loads(data_decode)
        print(type(data_decode), data_decode)
    return data_decode

def data_clean(raw_data):
    events = raw_data['records']
    cleaned_data = {}
    for event in events:
        cleaned_data[event['recordid']] = {}
        label_list = [('event_id','id'),('title','title'),('category','categoty'),('price','price_detail'),('description','description'),('link','access_link'),('telephone','access_phone'),('cover_letter','cover_credit')]
        for a,b in label_list:
            try:
                cleaned_data[event['recordid']][a] = event['fields'][b]
            except KeyError:
                print('KeyError in', a)
            finally:
                cleaned_data[event['recordid']][a] = "unknown"
    return cleaned_data
url = 'https://opendata.paris.fr/api/records/1.0/search/?dataset=que-faire-a-paris-&rows=10&facet=category&facet=tags&facet=address_zipcode&facet=address_city&facet=pmr&facet=blind&facet=deaf&facet=access_type&facet=price_type'
data = get_data_from_API_with_head(url)
cleaned_data = data_clean(data)
print(cleaned_data)
