import zipfile
import os
import sys
import shutil


def main():
    image = sys.argv[1]

    if not os.path.isfile(image):
        print('O arquivo informado não existe')
        sys.exit()

    check_format = (str(image[len(str(image)) - 4:len(str(image))]))
    if check_format.lower() not in ['.bmp', '.png', '.jpg', 'jpeg']:
        print('O arquivo não é uma imagem válida')
        sys.exit()
   
    file_to_hide = sys.argv[2]

    if not os.path.isfile(file_to_hide):
        print('O arquivo informado para esconder não existe')
        sys.exit()

    # Caminho completo para o arquivo
    path_image = os.path.realpath(image)
    path_file_to_hide = os.path.relpath(file_to_hide)
    
    # Zipa o arquivo a ser escondido
    stegzip = zipfile.ZipFile('steg.zip', 'w')
    stegzip.write(path_file_to_hide,
    compress_type=zipfile.ZIP_DEFLATED,
    compresslevel=9)
    stegzip.close()
    nc_stegzip = os.path.realpath('steg.zip')

    if check_format == 'jpeg':
        nomefinal = str(image)[0:len(str(image))-5] + '_modificado.' + str(check_format)
    else:
        nomefinal = str(image)[0:len(str(image))-4] + '_modificado' + str(check_format)

    with open(nc_stegzip, 'rb') as zf:
        conteudostegzip = zf.read()

    shutil.copyfile(path_image, nomefinal)
    
    with open(nomefinal, 'ab') as f:
        f.write(conteudostegzip)
    
    # O processo está concluído!
    print('O arquivo foi salvo como '
    + str(nomefinal))

    print('Tamanho do arquivo original '
    + str(os.path.getsize(image)))
    
    print('Tamanho do arquivo final '
    + str(os.path.getsize(nomefinal)))

if __name__ == '__main__':
    main()    