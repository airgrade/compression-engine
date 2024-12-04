#import all required packages
import zlib, base64

def compress(inputfile: str, outputfile: str):
    '''takes the uncompressed file as the input and the output file is the compressed one'''
    data = open(inputfile, 'r').read()
    data_bytes = bytes(data, 'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes,9))
    decoded_data = compressed_data.decode('utf-8') 
    compressed_file = open(outputfile,'w')
    compressed_file.write(decoded_data)
    
#compress('demo.txt', 'ot.txt')

def decompress(inputfile: str, outputfile: str):
    '''Takes a compressed file as the inputfile and gives back the original size of the document as the outputfile'''
    file_content = open(inputfile, 'r').read()
    encoded_data = file_content.encode('utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
    decoded_data = decompressed_data.decode('utf-8')
    file = open(outputfile, 'w')
    file.write(decoded_data)
    file.close()
    


