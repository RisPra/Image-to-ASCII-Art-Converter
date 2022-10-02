import PIL.Image

class AsciiImage:
    def __init__(self, path):
        self.ASCII_CHARACTERS = ['@ ','# ','S ','% ','? ','* ','+ ', '; ', ': ', ', ', '. ']
        #self.ASCII_CHARACTERS = ['@@','##','SS','%%','??','**','++', ';;', '::', ',,', '..']
        #self.ASCII_CHARACTERS = ['@','#','S','%','?','*','+', ';', ':', ',', '.']
        self.ASCII_CHARACTERS_LENGTH = 2
        self.image = PIL.Image.open(path)
        self.givenLen = 300
        self.givenLenChar = 'w'
        self.width, self.height = self.image.size

    def resizeConfig(self, givenLen, givenLenChar):
        self.givenLen = givenLen
        self.givenLenChar = givenLenChar

    def resize(self):
        aspectRatio = self.width/self.height
        if self.givenLenChar == 'w':
            calcLen = int(self.givenLen/aspectRatio)
            self.image = self.image.resize((self.givenLen, calcLen))
        elif self.givenLenChar == 'h':
            calcLen = int(aspectRatio*self.givenLen)
            self.image = self.image.resize((calcLen, self.givenLen))
        self.width, self.height = self.image.size

    def grayscale(self):
        self.image = self.image.convert('L')

    def toAsciiText(self):
        pixels = self.image.getdata()
        return "".join([self.ASCII_CHARACTERS[pixel//25] for pixel in pixels])

    def formatAsciiText(self):
        print(self.toAsciiText())
        stringAsciiText = self.toAsciiText()
        twidth = self.width*2
        return "\n".join([stringAsciiText[i:i+twidth] for i in range(0, len(stringAsciiText)+self.ASCII_CHARACTERS_LENGTH, twidth)])

    def fileWrite(self):
        self.resize()
        self.grayscale()
        print("Returned Formated ASCII text")
        with open("Converted ASCII Art.txt", "w") as f:
            print(self.formatAsciiText())
            f.write(self.formatAsciiText())

def main():
    path = "D:/Documents/Projects/ASCII Art Image Converter/image.png"
    inst1 = AsciiImage(path)
    inst1.fileWrite()

main()