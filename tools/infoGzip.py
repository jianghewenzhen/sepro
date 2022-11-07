import base64
import gzip

'''gzip压缩和解压缩'''


def gzipys(data):
    data_byte = gzip.compress(data.encode("utf-8"))  # gzip压缩
    # print(data_byte)
    enbase = base64.b64encode(data_byte).decode()  # base64编码
    # print(enbase)
    return enbase


# def gzipjy(data):
#     # base64解码并解压gzip字符串
#     debase = base64.b64decode(data)
#     # print(debase)
#     decp = gzip.decompress(debase).decode()
#     # print(decp)
#     return decp

def gzipjy(name):
    with open(name, 'r') as f:
        data = f.read()
        # base64解码并解压gzip字符串
        debase = base64.b64decode(data)
        # print(debase)
        decp = gzip.decompress(debase).decode()
        # print(decp)
    return decp
