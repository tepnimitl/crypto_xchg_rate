
import os
import json


crypt_bn_sym=[]
crypt_bk_sym=[]
xe_list=[]
URL_BN='https://api.binance.us/api/v3/ticker/price?symbol='
URL_BK='https://api.bitkub.com/api/market/ticker?sym='
crypt_sym=["BNB", "LTC", "XRP", "BCH", "ETH", "BTC"]

print("====== Binance-BitKub Exchange Rate ======")
print(crypt_sym)
print("==========================================")

for i in crypt_sym:
  crypt_bn_sym.append(str(i)+'USD')
  crypt_bk_sym.append('THB_'+str(i))

#crypt_bn_sym=["BNBUSD", "LTCUSD", "XRPUSD", "BCHUSD", "ETHUSD", "BTCUSD"]
#crypt_bk_sym=["THB_BNB", "THB_LTC", "THB_XRP", "THB_BCH", "THB_ETH", "THB_BTC"]

if len(crypt_bn_sym) != len(crypt_bk_sym):
  exit()

for i in range(0,len(crypt_bn_sym)):
  crypt_bn=os.popen('curl -ls '+URL_BN+crypt_bn_sym[i]).read()
  crypt_bn=json.loads(crypt_bn)
  #print(crypt_bn['price'])
  price_bn=float(crypt_bn['price'])

  crypt_bk=os.popen('curl -ls '+URL_BK+crypt_bk_sym[i]).read()
  crypt_bk=json.loads(crypt_bk)
  #print(crypt_bk[crypt_bk_sym[i]]['last'])
  price_bk=float(crypt_bk[crypt_bk_sym[i]]['last'])
  
  xe=price_bk/price_bn
  xe_list.append(xe)
  print(crypt_sym[i] + ',' + str(price_bn) + ',' + str(price_bk) + ',' + str(xe))

print("==========================================")
for i in range(0,len(crypt_sym)):
  print(crypt_sym[i] +' '+ str(xe_list[i]))
print("==========================================")
