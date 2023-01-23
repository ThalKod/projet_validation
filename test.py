from boto.s3.connection import S3Connection
from boto.s3.key import Key

ak= "AKIATTIOBPSHYQNTSZHC"
sk = "hq2E0UCye4QRIcj89iHGSdoJQrfI5ufm9zUf7LX/"

host = 's3.eu-west-3.amazonaws.com'
conn = S3Connection(ak,sk,host=host)
b = conn.get_bucket('ensta')
k = Key(b)
k.key = 'myobject'
obj = k.get_contents_as_string()