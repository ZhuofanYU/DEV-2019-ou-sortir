from urllib import request
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
        print('Data:', data_decode)
    return data_decode

# url = 'https://opendata.paris.fr/api/records/1.0/search/?dataset=que-faire-a-paris-&rows=10000&facet=category&facet=tags&facet=address_zipcode&facet=address_city&facet=pmr&facet=blind&facet=deaf&facet=access_type&facet=price_type'
# data = get_data_from_API_with_head(url)
