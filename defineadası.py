print(r""")

                   ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
              
              """)

print("Define adasına hoşgeldiniz.")
print("Göreviniz doğru şıkları seçerek hazineyi bulmak ve geri dönmek.")

choise1 = input("Yolda giderken bir yol ayrımına denk geldiniz. Hangi yoldan gideceksiniz? Sol mu sağ mı?\n ").lower()
if choise1 == "sol":
    choise2 = input("Deniz kenarında bir kayık buldunuz.Adaya gitmek için binecek misiniz yoksa bekleyecek misiniz?Binmek için bin,beklemek için bekle yazınız.\n").lower()
    if choise2 == "bekle":
        choise3 = input("Beklemeniz meyvesini verdi ve bir gemiyle adaya vardınız.Adada yerin zemininde bulunan kırmızı,sarı,siyah ve mavi kapılardan hangisini seçeceksiniz?\n").lower()
        if choise3 == "sarı":
            choise4 = input("Tebrikler! Hazineyi buldunuz. Çıktığınızda geldiğiniz gemi ve sahilde bir kayık sizi bekliyor. Hangisini kullanacaksınız? Gemi yada kayık yazın.\n").lower()
            if choise4 == "kayık":
                print("KAZANDINIZ!")
            elif choise4 == "gemi":
                print("Gemideki mürettebat korsan çıktı ve her şeyinizi aldılar.Kaybettiniz.")
        elif choise3 == "kırmızı":
            print("Ateş dolu bir odaya düştünüz.Kaybettiniz.")
        elif choise3 == "siyah":
            print("Adımınızı attığınız an bir uçuruma düştünüz.Kaybettiniz.")    
        elif choise3 == "mavi":
            print("Canavarlarla dolu bir odaya girdiniz.Kaybettiniz.")  
        else:
            print("Olmayan bir kapıyı açtınız.Kaybettiniz.")
    else:
        print("Bindiğiniz kayık denizde açıldıktan bir süre sonra su almaya başladı ve battı.Kaybettiniz.")
else:
    print("Seçtiğiniz yolda kötü adamlara denk geldiniz ve elinizdeki haritaya el koydular.Kaybettiniz.")                              

 
           
