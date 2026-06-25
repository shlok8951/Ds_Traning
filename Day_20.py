import matplotlib.pyplot as plt

year1 = [2010,2015,2020,2025]
dairy = [100,520,630,400]


year = [1990,2000,2005,2010]
farming = [300,200,250,100]

# fig,aux = plt.subplots(1,2)
# aux[0].plot(year1,dairy)
# aux[0].set_xlabel("Year")
# aux[0].set_ylabel("Dairy")
# aux[0].set_title("Dairy production graph")
# aux[1].bar(year,farming)
# aux[1].set_xlabel("Year")
# aux[1].set_ylabel("Farming")
# aux[1].set_title("Farming Produnction graph")

college = [10,20,30,50]

transport =[50,75,100,150]
fig,aux = plt.subplots(2,2)
aux[0][0].plot(year,college)
aux[0][1].bar(year,transport)
aux[1][0].pie(farming,labels = farming)
aux[1][1].hist(dairy)


# plt.gcf().canvas.get_supported_filetypes()
# plt.savefig("subplot.jpg")
plt.show()