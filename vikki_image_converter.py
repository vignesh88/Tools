# Author : me@vikki.in
import rawpy.enhance
import rawpy
import imageio
import exifread
import sys
import piexif


class VikkiImageConverter:
    def __init__(self, s_file_name, d_file_name):
        print('starting ')
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
        print(new_dict)
        new_dictt = self.create_dic('Exif', self.list_2)
        print(new_dictt)
        final_dic = {**new_dict, **new_dictt}
        print(final_dic)
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


p1 = VikkiImageConverter('/home/vikki/Downloads/blog/test1.nef', '/home/vikki/Downloads/blog/default11.jpg')
p1.raw_jpg()
sys.exit(0)
