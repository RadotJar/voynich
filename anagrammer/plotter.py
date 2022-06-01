import matplotlib.pyplot as plt

UN_English_characters = ['1','2','m','f','o','r','n','d','a','i']
UN_English_values = [8.0,7.6923076923076925,4.3478260869565215,2.690582959641256,1.5580736543909348,0.9884678747940692,0.7163323782234957,0.6309148264984227,0.2985074626865672,0.28735632183908044]
UN_Italian_characters = ['l','d','a','2','1','f','e','r']
UN_Italian_values = [15.128593040847202,10.576923076923077,10.062240663900415,7.6923076923076925,7.142857142857142,4.761904761904762,2.56198347107438,0.603318250377074]
UN_German_characters = ['2','1','s','i','e','n']
UN_German_values = [7.4074074074074066,6.896551724137931,3.0837004405286343,1.8396846254927726,1.6203703703703702,1.3295346628679963]

ax = plt.figure(figsize=(9,5))
ax.suptitle("Anagram Frequency Analysis on UNDHR")
ax.supxlabel("Character", va='bottom')
ax.supylabel("Percentage Occurence in Valid Anagram")

ax1 = plt.subplot(131)
ax1.bar(UN_English_characters, UN_English_values)
ax1.set_ylim([0,100])
ax2 = plt.subplot(132)
ax2.bar(UN_Italian_characters, UN_Italian_values)
ax2.set_ylim([0,100])
ax3 = plt.subplot(133)
ax3.bar(UN_German_characters, UN_German_values)
ax3.set_ylim([0,100])
plt.savefig('UN_anagrams.png')

Medicinal_Plants_characters = ['1','7','2','9','4','6','8','3','0','5','%','s']
Medicinal_Plants_Values = [61.26013724267,54.4973544973545,52.96411856474259,50.62344139650873,41.56028368794326,38.59275053304904,36.49193548387097,35.26448362720403,30.98712446351931,19.58650707290533,11.11111111111111,7.195616883116883]
Species_Plantarum_characters = ['2','3','5','1','4','9','8','6','7','0','_','.','-','S']
Species_Plantarum_Values = [82.2529224229543,73.91841779975277,68.90243902439023,65.22662889518413,65.09598603839441,59.80392156862745,58.048780487804876,55.76036866359447,53.96825396825397,45.0,18.170391061452516,17.0439414114514,10.0,6.746626686656672]
Die_epiphystiche_characters = ['8',']','7','*','1','4','3','6','2','9','5','i']
Die_epiphystiche_values = [40.909090909090914,33.33333333333333,27.102803738317753,26.582278481012654,18.610421836228287,16.037735849056602,14.285714285714285,13.114754098360656,9.770114942528735,5.714285714285714,4.716981132075472,4.673075092795279]

ax = plt.figure(figsize=(9,5))
ax.suptitle("Anagram Frequency Analysis on Botanical Texts")
ax.supxlabel("Character", va='bottom')
ax.supylabel("Percentage Occurence in Valid Anagram")

ax1 = plt.subplot(131)
ax1.bar(Medicinal_Plants_characters, Medicinal_Plants_Values)
ax1.set_ylim([0,100])
ax2 = plt.subplot(132)
ax2.bar(Species_Plantarum_characters, Species_Plantarum_Values)
ax2.set_ylim([0,100])
ax3 = plt.subplot(133)
ax3.bar(Die_epiphystiche_characters, Die_epiphystiche_values)
ax3.set_ylim([0,100])
plt.savefig('Botanical_anagrams.png')

EAP_characters = ['3','w','2','s','*','r','f','1','o','a']
EAP_values = [25.0,22.33810888252149,15.686274509803921,14.615003619461273,14.457831325301203,13.131676869523467,11.611096051323756,11.428571428571429,9.859422492401215,9.037113464631446]
Le_Systeme_Solaire_characters = ['T','7','4','5','1','_','2','6','8','n']
Le_Systeme_Solaire_values = [34.48275862068966,33.33333333333333,28.57142857142857,18.181818181818183,10.714285714285714,8.80281690140845,8.0,7.6923076923076925,7.4074074074074066,7.0744288872512895]
La_Navigation_characters = ['7','3','4','6','5','1','8','2','9',')',']',':','0','n']
La_Navigation_values = [57.818930041152264,47.386759581881535,45.776566757493185,41.6403785488959,41.41689373297003,40.83414161008729,40.58898847631242,38.17427385892116,29.207920792079207,19.485294117647058,18.412698412698415,18.045112781954884,15.461847389558233,12.035579010086394]

ax = plt.figure(figsize=(9,5))
ax.suptitle("Anagram Frequency Analysis on Further Texts")
ax.supxlabel("Character", va='bottom')
ax.supylabel("Percentage Occurence in Valid Anagram")

ax1 = plt.subplot(131)
ax1.bar(EAP_characters, EAP_values)
ax1.set_ylim([0,100])
ax2 = plt.subplot(132)
ax2.bar(Le_Systeme_Solaire_characters, Le_Systeme_Solaire_values)
ax2.set_ylim([0,100])
ax3 = plt.subplot(133)
ax3.bar(La_Navigation_characters, La_Navigation_values)
ax3.set_ylim([0,100])
plt.savefig('other_anagrams.png')

verification_characters = ['g', 'd', 'o', 'f', 'e', 'r']
verification_values = [66.66666666666666,40.0,40.0,40.0,33.33333333333333,16.666666666666664]

ax = plt.figure(figsize=(9,5))
ax.suptitle("Anagram Frequency Analysis on Verification Text")
ax.supxlabel("Character", va='bottom')
ax.supylabel("Percentage Occurence in Valid Anagram")

ax1 = plt.subplot(111)
ax1.bar(verification_characters, verification_values)
ax1.set_ylim([0,100])
plt.savefig('verification_anagrams.png')