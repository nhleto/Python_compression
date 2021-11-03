import gzip
import sys

def decompress():
    variable = ' '.join(sys.argv[1:])
    zipped = gzip.compress(variable.encode())
    decompressed = gzip.decompress(zipped)
    decoded_decompress = decompressed.decode("utf-8")
    print(decoded_decompress)

decompress()