from superhero import Superhero

from yandex import YaUploader

if __name__ == '__main__':
    superhero = Superhero()
    superhero.get_superhero(['Hulk', 'Captain America', 'Thanos'])
    yandex = YaUploader(token="")
    yandex.get_upload_file("test/test.txt", 'C:\\Users\\matveev\\Desktop\\Нетология\\test.txt')
