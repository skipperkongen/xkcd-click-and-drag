import urllib        
import sys
     
# http://imgs.xkcd.com/clickdrag/1n1e.png       

root = XkcdNode(0,0)
visited = {}
stack = []

stack.append(root)
while len(stack) > 0:
	node = stack.pop()
	explore(node)

create_image(root)
	
class XkcdNode():
	def __init__(self, x, y):
		self.coord = coord
		self.status = None
		self.image = None
		self.n = None
		self.s = None
		self.e = None
		self.w = None
 




#				conn = urllib.urlopen(url)  
#				code = conn.code
#				if code == 200:
