meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "NICE TRY DIDDY": "İyi denemeydi Diddy",
            "GG": "İyi oyundu",
            "EZ": "Kolaydı"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Henüz benim sözlüğümde bu kelime yok.")
