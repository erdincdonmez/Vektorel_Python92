def anaekran():
   print("\033[1;32;40m") # bununla renk yapıyoruz
   # print("╔"+"═"*20+"╗")
   print("╔═════════════════════╗")
   # print("║\033[1;31;40m   VEKTOREL APP  \033[1;32;40m  ║")
   print("║    VEKTOREL APP     ║")
   print("║                     ║")
   print("║  1-Hesap makinesi   ║")
   print("║  2-Oyunlar          ║")
   print("║  3-Çizimler         ║")
   print("║  4-...              ║")
   print("║                     ║")
   print("║    Seçimiz nedir?   ║")
   print("╚═════════════════════╝")

   # input()
   # 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝╗
   # secim = input("Seçiminiz:")
   secim = input()
   if secim == "1" : 
       print("Hesap makinesini seçtiniz")
       anaekran()
   if secim == "2" : 
      print("Oyunlar seçtiniz")
      anaekran()
   if secim == "3" : 
       # print("Çizimler seçtiniz")
       import moduller.cizimler
       anaekran()
   
   if secim in ["1","2","3"]: pass
   else : print("1,2,3 dışında bir şey seçtiniz")

anaekran()