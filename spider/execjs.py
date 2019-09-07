
# import js2py
# context = js2py.EvalJs()
# context.t = 'ddd'
# context.execute("""
#     var sign = t
#     function add(x, y) {
#       return x + y;
#     }
# """)
# sign = context.sign
# res = context.add(1, 2)

# print(sign)
# print(res)

import execjs
res=execjs.eval("'red yellow blue'.split(' ')")
print(res)