import requests
import json

_banner_ = '''
   +=+=+=+=+=+=+=+=+=+=+=+=+=+=+
  +++=== Check Nickname FF ===+++   
 ++== Tools Check Nickname FF ==++
+= Check Nickname Free Fire Via ID =+
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
# author : JC0D3(Juniel Damal)
# contact: @juniel_damal46
'''
id = raw_input('ID Game: ')
data = key
json = 

get = requests.post('https://validation.warriors-media.id/trueid/freefire/?id='+id+'&token=JC0D3','+data+','+json+')

up = get.content
pu = json.loads(up)
if "session_key" in up:
    print
    print _banner_
    print 'username:' + pu['identifier']
    print 'token:' + pu["access_token"]
    open(user+'-token.txt', 'a').write(pu["access_token"])
    print
    print 'saved file to '+user+'-token.txt'
else:
    print 'maaf username/password salah'
