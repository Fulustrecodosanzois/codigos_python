playlist=[]
musica= {}

for perc in range(2):
    nome= input("Qual o nome da música: ")
    artista= input("Qual o nome do artista: ")
    tempo= float(input("Qual a duração da música? "))
    
    musica[nome]= {"artista": artista, "duração":tempo}
    
    playlist.append(musica.copy())
    musica.clear()
    
    
print(playlist)

for linha in playlist:
    for chave, valor in linha.items():
        print(f"{chave}: Artista= {valor['artista']} duração= {valor['duração']}")
