# Author: me@vikki.in
from PIL import Image
from optparse import OptionParser
import sys
import os


def compress_image():
    usage = "usage: %prog [options] arg"
    description = "compress image"
    parser = OptionParser(usage=usage, description=description)
    parser.add_option("-f", "--file", dest="file", action="store", default=sys.argv[1], help="image file")
    parser.add_option("-e", "--erase", dest="erase", default="no", action="store", help="yes/no")
    (options, args) = parser.parse_args()

    if options.file is None:
        parser.print_help()
        sys.exit(2)
    if not os.path.isfile(options.file):
        print("File '{}' not found".format(options.file))
        sys.exit(2)

    foo = Image.open(options.file)
    print(foo.size)
#    #foo = foo.resize((160,300),Image.ANTIALIAS)
    new_filename = options.file.split(".")
    new_filename = new_filename[0]
    new_filename = new_filename + "_opt" + ".jpg"
    print(new_filename)
    foo.save(new_filename, optimize=True, quality=50)
    if "yes" in options.erase:
        os.remove(options.file)


compress_image()
