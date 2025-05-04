not1 = int(input("Ortalaman kaç?"))

if not1<=100 and not1>=0: 
    if not1>90 : print("Süper 5 almışsın.")
    elif not1>85 : print("5 aldın")
    elif not1>70 : print("4 aldın")
    elif not1>=50 : print("3 aldın")
    if not1<50 : print("Kaldın")
else:
    print("Doğru not değeri girmediniz.")