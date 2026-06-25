import matplotlib.pyplot as plt
import numpy as np
# x = [10,20,30,40,50]
# y =[1,2,3,7,8]

# plt.plot(x,y,color="red",marker='*',linestyle="dashed",linewidth=5,markersize=15)
# plt.show()

#----------multiple lline chart------------

# x = [2010,2015,2020,2025]
# y1 =[100,200,260,290]
# y2 = [150,185,195,300]

# plt.plot(x,y1,label = "jeans",color="red",linestyle="solid")
# plt.plot(x,y2,color="green", label ="shirt", linewidth = 5)
# plt.legend()
# plt.show()

x = ["jan","feb","mar","apr","may","jun"]
y = [150,155,152,163,160,168]
y1 = [120,118,125,122,130,135]
y2 = [180,290,115,78,342,350]
# plt.figure(figsize=(6,2))
# plt.plot(x,y ,marker = "." ,markersize = 14,label="Tech Corp Price($)",color="orange",linestyle="solid")
# plt.plot(x,y1 ,marker = "." ,markersize=14,label="Reyail inc Price($)",color="blue",linestyle="solid")
# plt.plot(x,y2)
# plt.legend()
# plt.grid(linestyle="dashed")
# plt.title("H1 2026 Stock Price Trend Analysis")
# plt.xlabel("Monthes")
# plt.ylabel("Stock Price ($)")
# plt.show()

x = np.array([100,200,300,400,500,600])
w = 0.40
plt.bar(x-w/2,y ,label="Tech Corp Price($)",color="orange",linestyle="solid")
plt.bar(x+w/2,y1,label="Reyail inc Price($)",color="blue",linestyle="solid")
#plt.plot(x,y2)
plt.legend()
#plt.grid(linestyle="dashed")
plt.title("H1 2026 Stock Price Trend Analysis")
plt.xlabel("Monthes")
plt.ylabel("Stock Price ($)")
plt.show()

