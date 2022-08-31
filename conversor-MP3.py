from pytube import YouTube
import os

# Link
yt = YouTube(
    input("Digite o link: \n>>"))

# Diretório
print("Onde deseja salvar?")
destino = input(">>")

# Extrair áudio
video = yt.streams.filter(only_audio=True).first()

# Download
download = video.download(output_path=destino)

# Salvando
base, ext = os.path.splitext(download)
new_file = base + '.mp3'
os.rename(download, new_file)

# Resultado
print(yt.title + "Download Completo!")