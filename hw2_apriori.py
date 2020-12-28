from apyori import apriori

data = [['banana', 'apple', 'milk', 'onion', 'hotdog', 'juice', 'pizza', 'eggs'],
       ['onion', 'hotdog', 'xojam', 'water', 'video', 'chicken', 'tea', 'eggs'],
       ['pizza'],
       ['apple', 'xojam', 'bread', 'onion', 'seafood'],
       ['eggs', 'apple', 'xojam', 'pizza', 'onion', 'tea', 'pizza'],
       ['bread', 'banana', 'beef', 'eggs', 'milk', 'chocolate'],
       ['chicken', 'beef', 'milk', 'banana', 'eggs', 'seafood'],
       ['bread', 'banana', 'xojam', 'beef', 'water', 'pointCard', 'tea', 'watermelon', 'chocolate'],
       ['onion', 'bread', 'banana', 'milk', 'pointCard', 'watermelon', 'chocolate'],
       ['pizza', 'chicken', 'beef', 'banana', 'eggs', 'hotdog', 'milk', 'tea', 'watermelon']]
'''
data = [['Beer', 'Nuts', 'Diaper'],
        ['Beer', 'Coffee', 'Diaper'],
        ['Beer', 'Diaper', 'Eggs'],
        ['Nuts', 'Eggs', 'milk'],
        ['Nuts', 'Coffee', 'Diaper', 'Eggs', 'Milk']]
'9''
data = [['r', 'z', 'h', 'j', 'p'],
       ['z', 'j', 'y', 'x', 'w', 'v', 'u', 't', 's'],
       ['z'],
       ['r', 'x', 'n', 'o', 's'],
       ['y', 'r', 'x', 'z', 'q', 't', 'p'],
       ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
'''
association_rules = apriori(data, min_support=0.4, min_confidence=0.4, max_length=2) 
#apriori(資料, min_support=0.1, min_confidence=0.1, min_lift=2, max_length=集合內要有幾個元素)
test1 = apriori(data, max_length=2)
test2 = list(test1)
#print(test1, test2)

for item in test2:
   print(item)
   pair = item[0]
   items = [x for x in pair]
#   print("Rule: " + items[0] + " -> " + items[1])
   print("Support: " + str(item[1]))
   print("Confidence: " + str(item[2][0][2]))
   print("Lift: " + str(item[2][0][3]))

association_results = list(association_rules)
for item in association_results:
    pair = item[0]
    if(len(pair) == 2):
        items = [x for x in pair]
        print("Rule: " + items[0] + " -> " + items[1])
        print("Support: " + str(item[1]))
        print("Confidence: " + str(item[2][0][2]))
#        print("Lift: " + str(item[2][0][3]))
        print("=====================================")
print("Rule: b -> a")
print("Support: 這個組合出現的次數 / a在幾個set出現的次數")
print("Confidence: 有 a 的時候, 出現 b 的機率")
print("Lift: set數量 / 組合出現次數")


