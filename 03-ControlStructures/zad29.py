washing_product = "shoes" 
rinse = True 
spin = False 
czas = 0


if rinse == True:
    czas += 15
if spin == True:
    czas += 9
if washing_product == "shoes":
    czas += 20
if washing_product == "underwear":
    czas += 70
if washing_product == "jacket":
    czas += 40

print(f"Total washing time: {czas} minutes")
