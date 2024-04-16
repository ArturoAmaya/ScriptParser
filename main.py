from parse import parse_from_file
from upload import upload_script
import sys

filepath = sys.argv[1]

parsed = parse_from_file(filepath)
if parsed:
    response = upload_script(parsed)

    # TODO combine the videos
    print(response)
else:
    print(parsed)