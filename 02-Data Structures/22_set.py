#sets dont take duplicate values and it is unordered and unindexed


nepal = {"Kathmandu", "Pokhara","Itahari","Biratnagar","Hetauda","Biratnagar" }
bagmati = {"Makwanpur","Hetauda","Chitlang","Chitawan","Dhading","Kathmandu"}



nepal.add("Dakxinkali")
bagmati.add("Chandragiri")

nepal.update(bagmati)


for i in nepal:
    print(i)
print("")

for j in bagmati:
    print(j)

