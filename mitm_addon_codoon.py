#coding:utf-8

import json
from mitmproxy import http

class Codoon():
	def request(self,flow: http.HTTPFlow):
		if "products/237" in flow.request.url:
			h = flow.request.headers
			d = {}
			for k,v in h.items():
				d[k] = v
			open('/sdcard/codoon.json','w').write(json.dumps(d))


addons = [Codoon()]
