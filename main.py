from parse import parse_from_file
from upload import upload_script
import sys

filepath = sys.argv[1]

parsed = parse_from_file(filepath)
if parsed:
    upload_script(parsed)
else:
    print(parsed)