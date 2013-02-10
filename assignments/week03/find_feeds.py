fh = open('C:\\Users\\Tyler\\bloglist.html')
from bs4 import BeautifulSoup

parsed = BeautifulSoup(fh)



''''

for e in entries:
    anchor = e.find('a')
    paragraph = e.find('p', 'discreet')
    title = anchor.text.strip()
    url = anchor.attrs['href']
    print title
    print url
    try:
        print paragraph.text.strip()
    except AttributeError:
        print 'Uncategorized'
    print
    '''
    
def my_function(parsed):
    '''parse out url and title of entry, add to list dependent on topic'''
    pgsql = []
    django = []
    other = []
    
    entries = parsed.find_all('div', class_='feedEntry')
    print len(entries), 'entries'
    
    for xx in entries:
        anchor = xx.find('a')
        url = anchor.attrs['href']
        title = anchor.attrs['title']
        paragraph = xx.find('p', 'discreet').text.strip()
        
        print type(paragraph)
        
        if 'Postgre' in paragraph:
            pgsql.append({'title':title, 'url':url})
        elif 'Django' in paragraph:
            django.append({'title':title, 'url':url})
        else: other.append({'title':title, 'url':url})
    
    return pgsql, django, other
    
    
a, b, c = my_function(parsed)
print a
print
print b
print 
print c