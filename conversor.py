try:
    from PIL import Image
    import PIL
    import os
    import glob
except Exception as error:
    print(error)
    input('Erro ao carregar bibliotecas, notifique o administrador!')
    exit

class ConvertWebp():
    def __init__(self):
        self.folder = 'compress'
    
    def listAllImages(self):
        files = os.listdir()
        return [file for file in files if file.endswith(('jpg', 'jpeg', 'png'))]

    def __convertOnImage(self, filename_with_extension):
        extension = filename_with_extension.split('.')[-1]
        filename = filename_with_extension.replace(extension, '')
        
        image = Image.open('{}'.format(filename_with_extension))
        image = image.convert('RGB')
        image.save('{}/{}webp'.format(self.folder, filename), 'webp', optimize=True,quality=80)

    def compressImages(self):
        os.makedirs(self.folder, exist_ok=True)

        images = self.listAllImages()
        for image in images:
            self.__convertOnImage(image)

        print('                                            ')
        print(' #######   ####    ####  ####    #  ######  ')
        print(' #         #  #   #   #  #   #   #       #  ') 
        print(' #   ###   #   # #    #  #    #  #   #####  ') 
        print(' #     #   #    #     #  #   #   #   #      ')
        print(' #######   #          #  ####    #   #####  ')
        print('                                            ')
        print('Processamento realizado com sucesso, lembre-se de usar apenas as imagens comprimidas!')
        return True

try:
    conversor = ConvertWebp()
    conversor.compressImages()
except Exception as error:
    print(error)

input('Pressione Enter para fechar!')
