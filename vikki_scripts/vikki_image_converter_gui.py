# Author : me@vikki.in
import rawpy.enhance
import rawpy
import imageio
import exifread
import sys
import piexif
import os
from tkinter import *


class VikkiImageConverter:
    def __init__(self, s_file_name, d_file_name):
        print('Processing file {}'.format(s_file_name))
        self.s_filename = s_file_name
        self.d_filename = d_file_name
        self.exif_dict = piexif.load(s_file_name)
        self.list_1 = {254, 256, 257, 258, 259, 262, 271, 272, 273, 274, 277, 278, 279, 282, 283, 249, 296, 305, 306,
                       330, 532}
        self.list_2 = {33434, 33437, 34850, 34855, 34864, 36867, 36868, 37380, 37381, 37383,
                       37384, 37385, 37386, 37520, 37521, 37522, 41495, 41985, 41986, 41987, 41988, 41989, 41990, 41991,
                       41992, 41993, 41994, 41996}

    def write_image(self):
        new_dict = self.create_dic('0th', self.list_1)
        new_dictt = self.create_dic('Exif', self.list_2)
        final_dic = {**new_dict, **new_dictt}
        exif_bytes = piexif.dump(final_dic)
        piexif.insert(exif_bytes, self.d_filename)

    def create_dic(self, ifd, id_list):
        new_dict = {}
        new_dict_2 = {}
        for i, k in self.exif_dict.items():
            if i in [ifd]:
                for x, y in k.items():
                    if x in id_list:
                        new_dict_2[x] = y
                new_dict[i] = new_dict_2
        return new_dict

    def raw_jpg(self):
        with rawpy.imread(self.s_filename) as raw:
            rgb = raw.postprocess()
            imageio.imsave(self.d_filename, rgb)
            self.write_image()


def print_tag(nef_file):
    f = open(nef_file, 'rb')
    tags = exifread.process_file(f)
    for tag in tags.keys():
        if tag in ('Exif', 'EXIF'):
            print("{}: {}".format(tag, tags[tag]))


def absolutefilepaths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if f.endswith('.nef'):
                yield os.path.abspath(os.path.join(dirpath, f))


def getfiles(file_list, destination_path):
    for i in file_list:
        source_file = i
        destination_file_name = i.split(".nef")
        destination_file_name = destination_file_name[0].split("/")
        destination_file_name = destination_file_name[-1] + ".jpg"
        destination_file_name = os.path.join(destination_path, destination_file_name)
        p1 = VikkiImageConverter(source_file, destination_file_name)
        p1.raw_jpg()


def show_entry_fields():
#    print("First Name: %s\nLast Name: %s" % (source_n.get(), destination_n.get()))
    source = source_n.get()
    destination = destination_n.get()
    if (source or destination) is None:
        sys.exit(2)
    if os.path.isfile(destination):
        print("Destination should always be a directory")
        sys.exit(2)
    if not os.path.isdir(destination):
        print("Destination doesn't exit")
        sys.exit(2)

    if not os.path.isfile(source):
        if not os.path.isdir(source):
            print("Source/destination not found or improper usage")
            sys.exit(2)

    if os.path.isdir(source):
        file_list = absolutefilepaths(source)
        getfiles(file_list, destination)
    else:
        destination_filename = source.split(".nef")
        destination_filename = destination_filename[0].split("/")
        destination_filename = os.path.join(destination, destination_filename[-1] + ".jpg")
        p1 = VikkiImageConverter(source, destination_filename)
        p1.raw_jpg()
    print("Processing completed")
    sys.exit(0)


def vikki_gui():
    global e1, e2, source_n, destination_n
    master = Tk()
    master.title("Vikki image converter")
    master.geometry('{}x{}'.format(800, 450))
    #Label(master, text="Source folder/file", font=("Courier", 32)).grid(row=0)
    s1 = Label(master, text="Source folder/file", font=("Courier", 32))
    source_n = StringVar()
    e1 = Entry(master, textvariable=source_n)
    #e1.grid(row=0, column=1, columnspan=3, sticky=W)

    d1 = Label(master, text="Destination folder/file", font=("Courier", 32))
    destination_n = StringVar()
    e2 = Entry(master, textvariable=destination_n)

    s1.pack()
    e1.pack()
    d1.pack()
    e2.pack()


    #
    #e2.grid(row=1, column=1, sticky=E)



    b1 = Button(master, text='Quit', command=master.quit)
    b1.pack(side=LEFT)
    #Button(master, text='Run', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
    b2 = Button(master, text='Run', command=show_entry_fields)
    b2.pack(side=RIGHT)
    mainloop()


vikki_gui()

sys.exit(0)
