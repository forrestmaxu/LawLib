from urllib.parse import urlencode
import postdata

data = {
    'a': 'test',
    'name': ' 中国'
}
print(urlencode(data))

print(postdata.postdata)