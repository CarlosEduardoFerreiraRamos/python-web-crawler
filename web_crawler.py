import requests
from bs4 import BeautifulSoup

def web(page,elem,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        i = 0
        array = s.findAll('li', {'id':elem});

        if not array:
            print(elem,'ESSE DANONE') 
        for link in array:
            tet = link.get('id', None)
            if not tet:
                print(i,elem, 'ESSE DANONE')
            print(i,elem)
            i += 1
            # print(tet)

# web(1, 'a','http://www.amazon.in/s/ref=s9_acss_bw_cts_VodooFS_T4_w?rh=i%3Aelectronics%2Cn%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_98%3A10440597031%2Cp_36%3A1500000-99999999&bbn=1805560031&rw_html_to_wsrp=1&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=2EKZMFFDEXJ5HE8RVV6E&pf_rd_t=101&pf_rd_p=c92c2f88-469b-4b56-936e-0e65f92eebac&pf_rd_i=1389432031')

list = [
    'CA888CL45KPAMOB'
];

for sku in list:
    web(1,sku,'http://www.mobly.com.br/catalog/?m=' + sku + '&is_sku=1&is_simples=0');



if __name__ == '__main__':
	print('MAIN');