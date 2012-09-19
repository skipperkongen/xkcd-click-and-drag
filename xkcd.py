import urllib        
import sys                         

# Warning: This code is slow to complete, due to all the 404's. It also sucks in many other ways.
# Please look at xkcd2.py instead :-) 

for v in ['n','s']:
	for h in ['e','w']:
		for i in range(1,100):
			for j in range(1,100):                                     
				# http://imgs.xkcd.com/clickdrag/2n4e.png
				url = 'http://imgs.xkcd.com/clickdrag/%d%s%s%s.png' % (i,v,j,h)
				#print url
				conn = urllib.urlopen(url)  
				code = conn.code
				if code == 200:
					print url