facebook = True 
twitter = False 
instagram = False 

if (facebook and twitter or instagram and twitter or instagram and facebook) == True:
    print("A person can be a good influencer!")
else: 
    print("A person can't be a good influencer!")