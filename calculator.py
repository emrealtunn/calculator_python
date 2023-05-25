print(" Emre'nin hesap makinesine hoş geldiniz ")    
while True:
    try:
        a=input("Lütfen yapmak istediğiniz işlemi yazınız:")
        sonuc=eval(a)
        print("Yaptığınız işlemin sonucu:" , sonuc)
    except NameError:
        print("Lütfen sayı gir.")
    except SyntaxError:
        print(" Hata yaptınız lütfen örnekteki gibi bir işlem yapınız. Örnek: 3+5 şeklinde bir işlem giriniz !!")
