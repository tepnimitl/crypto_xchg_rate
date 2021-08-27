import os
import json

crypt_bn_sym=[]
crypt_bk_sym=[]
crypt_st_sym=[]
xe_bk_list=[]
xe_st_list=[]
fee_bk_list=[]
fee_st_list=[]
URL_BN='https://api.binance.us/api/v3/ticker/price?symbol='
URL_BK='https://api.bitkub.com/api/market/ticker?sym='
URL_BNCOM='https://api.binance.com/api/v3/ticker/price?symbol=ETHBTC'
URL_ST='https://satangcorp.com/api/v3/ticker/24hr?symbol='

crypt_sym_bk=["ZIL", "XLM", "BAND", "BNB", "LTC", "BCH", "DOGE", "ETH", "USDT", "USDC", "BTC"]
crypt_sym_st=["XLM", "BAND", "BNB", "LTC", "BCH", "DOGE", "ETH", "USDT", "USDC", "BTC"]

FEE_bk=[0.0100,0.0100,0.0010,0.0010,0.0010,0.0010,50.0000,0.0030,14.0000,14.0000,0.0005]
FEE_st=[0.0100,0.0010,0.0010,0.0010,0.0010,50.0000,0.0030,14.0000,14.0000,0.0005]

print("")
print("============== BitKub/Binance Exchange Rate ==============")
#print(crypt_sym_bk)
#print("------------------------------------------")

for i in crypt_sym_bk:
  crypt_bn_sym.append(str(i)+'USD')
  crypt_bk_sym.append('THB_'+str(i))

#crypt_bn_sym=["BNBUSD", "LTCUSD", "BCHUSD", "ETHUSD", "BTCUSD"]
#crypt_bk_sym=["THB_BNB", "THB_LTC", "THB_BCH", "THB_ETH", "THB_BTC"]

if len(crypt_bn_sym) != len(crypt_bk_sym):
  exit()
for i in range(0,len(crypt_bn_sym)):
  crypt_bn=os.popen('curl -ls '+URL_BN+crypt_bn_sym[i]).read()
  crypt_bn=json.loads(crypt_bn)
  #print(crypt_bn['price'])
  price_bn=round(float(crypt_bn['price']),4)

  crypt_bk=os.popen('curl -ls '+URL_BK+crypt_bk_sym[i]).read()
  crypt_bk=json.loads(crypt_bk)
  #print(crypt_bk[crypt_bk_sym[i]]['last'])
  price_bk=float(crypt_bk[crypt_bk_sym[i]]['highestBid'])
  
  xe=price_bk/price_bn
  xe_bk_list.append(xe)

  fee=price_bn*FEE_bk[i]
  fee_bk_list.append(fee)

  print(crypt_sym_bk[i] + '\t' + str("%5.4f" %xe) + '\t' + str("%10.4f" %price_bn) + '\t' + str("%12.4f" %price_bk) + '\t' + str("%10.4f" %fee_bk_list[i]))

print("")
print("============== Satang/Binance Exchange Rate ==============")
#print(crypt_sym_st)
#print("------------------------------------------")

crypt_bn_sym=[]
for j in crypt_sym_st:
  crypt_bn_sym.append(str(j)+'USD')
  crypt_st_sym.append(str(j)+'_thb')

if len(crypt_bn_sym) != len(crypt_st_sym):
  exit()
for i in range(0,len(crypt_bn_sym)):
  crypt_bn=os.popen('curl -ls '+URL_BN+crypt_bn_sym[i]).read()
  crypt_bn=json.loads(crypt_bn)
  #print(crypt_bn['price'])
  price_bn=float(crypt_bn['price'])

  crypt_st=os.popen('curl -ls '+URL_ST+crypt_st_sym[i]).read()
  crypt_st=json.loads(crypt_st)
  #print(crypt_st['price'])
  price_st=float(crypt_st['bidPrice'])

  xe=price_st/price_bn
  xe_st_list.append(xe)

  fee=price_bn*FEE_st[i]
  fee_st_list.append(fee)

  print(crypt_sym_st[i] + '\t' + str("%5.4f" %xe) +'\t'+  str("%10.4f" %price_bn) + '\t' + str("%12.4f" %price_st) + '\t' + str("%10.4f" %fee_st_list[i]))




print("")
print("Coins" + "\t" + "  BK/BN  " + "\t" + "  ST/BN  " + "\t" + " Diff " + "\t" + "  Fee  ")
print("--------------------------------------------------------")
print(crypt_sym_bk[0] + "\t" + str("%8.4f" %xe_bk_list[0]) + "\t" + "  ------ NULL ------"  + "\t" + str("%8.4f" %fee_bk_list[0]))
for i in range(0,len(crypt_sym_st)):
  print(crypt_sym_st[i] + "\t" + str("%8.4f" %xe_bk_list[i+1]) + "\t" + str("%8.4f" %xe_st_list[i]) + "\t" + str("%5.2f" %(xe_bk_list[i+1]-xe_st_list[i])) + "\t" + str("%8.4f" %fee_st_list[i]))
print("")
print("========================================================")
