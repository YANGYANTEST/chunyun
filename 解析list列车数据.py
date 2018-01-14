

info="车次 出发站 到达站 出发时间 到达时间 历时	商务座 特等座	一等座	二等座	高级 软卧 软卧 动卧	硬卧 软座 硬座 无座	其他 备注"


#解析第一条数据
traininfo1="E%2BuuvZDLskx1i0T32rG2L0gpci8AIiVTkTQ6QG42w1d%2Buxc1qW5VpEJQkfEPmo4yrgR0SIh9nAfW%0Afvu7BL5fu8CERc7O9zLi7IZcR9tZGPgw7aTnIt%2B4GfajmR2Voxt66NgqBVKtxTwfntkcPLyjQVkE%0AzkZDF%2FaW%2FgUlkMDPIKsqP2Z9C2jZyb%2F8K%2F8FB2Bv1p0TJ%2Bnw%2B4%2B5mCO3LJ4Vf%2Bi2kV8dKkpBJSb7%0AHXkbSln4C8GLC4tgjnzNSwnESXWvZYH%2FpA%3D%3D|预订|240000G1010D|G101|VNP|AOH|VNP|AOH|06:43|12:39|05:56|Y|QDRlHRXcjGMJOd1rldam%2BHz1egluEogy%2BaAl6aLck3bKVHB6|20180111|3|P2|01|11|1|0|||||||||||无|有|14||O0M090|OM9|0"
trainlist=traininfo1.split('|')
print(trainlist)
print("---------------------------------------")

for index,value in enumerate(trainlist):
    print(index,"========>",value)

trainrow=[]
trainrow.extend(trainlist[3:6])
trainlist[4]=stations.getCityName(trainlist[4])
trainlist[5]=stations.getCityName(trainlist[5])
# print(trainlist[4],trainlist[5])
trainrow.append(trainlist[3])
trainrow.append(trainlist[4])
trainrow.append(trainlist[5])
trainrow.extend(trainlist[8:11])
trainrow.extend(trainlist[32:21:-1])
# print(info)
# print(trainrow)



#解析第二条数据
traininfo2="rA774AD5wliq%2F9jraTGG3XCKfEWxF%2BDHfk%2F%2BzeBtckn538rAZPvA4BxwLrydgzcbLk1LsoWUsF8x%0AiMQpXZzLecccJzhG25lb8n%2BechvkAXld7ikFmyS%2BB7q6k3lTeIDcG5uburXywQ3a0CdRvWCo2u5c%0AR9wbPlbfhHHS97Q7DV5WKcb%2Fy4%2BndNv%2BVU8647Y9F7H6%2F2ZISNt52zg89RfcoziCteENNYAuo2iE%0A8ma%2Br9koAgZVzwn0gXV9JsRH1CKj|预订|24000000G503|G5|VNP|AOH|VNP|AOH|07:00|11:34|04:34|Y|OwWGlKxfnPfPYGOuhjVhioA2r3kj2krs0zxNVD04%2BIDhPhfc|20180111|3|P2|01|05|1|0|||||||||||无|1|无||O0M090|OM9|0"
trainlist2=traininfo2.split("|")
print(trainlist2)

for index,value in enumerate(trainlist2):
    print(index,"========>",value)

trainrow1=[]
trainrow1.extend(trainlist2[3:7])
trainrow1.extend(trainlist2[8:11])
trainrow1.extend(trainlist2[32:20:-1])
print(trainrow1)