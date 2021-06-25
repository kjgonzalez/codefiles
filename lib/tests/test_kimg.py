'''
test out how well kimg module is working
things to test out:
    * TODO: rename a single photo
    * TODO: resize a single photo
    * TODO: fix metadata of a single photo
    * TODO: rename a single folder to match the time range of data
    * TODO: getlist, getrange, getext, imgrename, imgreduce, renred, renSubfolder

NOTES:
    * tests are run in alphabetical order
'''
import unittest, zipfile, os, shutil
import kimg
import PIL.Image as pil
import piexif
osp = os.path

IMG_FOLDER = 'data/sample/'


class Tests_kimg(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        super(Tests_kimg, self).__init__(*args, **kwargs)
        pass
        self.ipath = osp.join(IMG_FOLDER, 'IMAG1727.jpg')

    def test__setup(self):
        ''' Need this 'test' and *cleanup test to manage files for tests '''
        print('SETUP STARTING')
        if(os.path.exists(IMG_FOLDER)): shutil.rmtree(IMG_FOLDER) # delete & remake if necessary, for dates
        zipfile.ZipFile('data/sample.zip', 'r').extractall('data/')
        self.assertEqual(14, len(os.listdir(IMG_FOLDER)))
        print('n items extracted:',len(os.listdir(IMG_FOLDER)))
        self.assertTrue(osp.exists(self.ipath))

    def test_zzcleanup(self):
        ''' Ensure that data is deleted'''
        shutil.rmtree(IMG_FOLDER)
        self.assertFalse(osp.exists(IMG_FOLDER))
        print('CLEANUP COMPLETE')

    def test_a_imgdate(self):
        ipath = osp.join(IMG_FOLDER, 'IMAG1727.jpg')
        self.assertTrue('200913_142641' == kimg.imgdate(1600000001))

    def test_b_dates(self):
        ''' Ensure that gdm, gdc, and gdt are all functioning properly. Unfortunately, date created & modified are
            relative to when the file was created locally.
         '''
        self.assertEqual(
            kimg.imgdate(kimg.gdm(self.ipath)),
            kimg.imgdate(kimg.gdc(self.ipath))
        )
        self.assertEqual('181213_080011', kimg.imgdate(kimg.gdt(self.ipath)))
        self.assertEqual(kimg.gdt(self.ipath), kimg.getdate(self.ipath))

    def test_c_getlist(self):
        # TODO: eventually move to test_klib
        x_jpg_norec = kimg.getlist(path=IMG_FOLDER,recursive=False,exts='jpg-JPG')
        self.assertEqual(12,len(x_jpg_norec))

        x_any_rec = kimg.getlist(path=IMG_FOLDER,recursive=True,exts='')
        self.assertEqual(15, len(x_any_rec))

    def test_d_getrange(self):
        self.assertEqual('180109-181231',kimg.getrange(IMG_FOLDER))
        self.assertEqual('180109_160129-181231_234056',kimg.getrange(IMG_FOLDER,date_only=False))
        self.assertEqual('180109-181215',kimg.getrange(IMG_FOLDER,recursive=False))

    def test_e_getext(self):
        dat = kimg.getlist(path=IMG_FOLDER,exts='png',incl_folders=True)
        self.assertEqual('png',kimg.getext(dat[0]))  # is a png img
        self.assertEqual('',kimg.getext(dat[1]))  # is a folder
    def test_f_imgrename(self):
        ifile = os.path.join(IMG_FOLDER,'IMAG1727.jpg')
        self.assertTrue(os.path.exists(ifile))
        kimg.imgrename(ifile)
        res2 = os.path.join(IMG_FOLDER,'181213_080011_1.jpg')
        self.assertTrue(os.path.exists(res2))

    def test_g_imgreduce(self):
        # verify that maximum dimension is 2000 and that exif data was preserved
        ifile = os.path.abspath(os.path.join(IMG_FOLDER,'IMAG2772.jpg'))
        # ifile = os.path.abspath(os.path.join(IMG_FOLDER,'17_map.png'))
        self.assertTrue(os.path.exists(ifile))
        print(os.path.getsize(ifile))
        kimg.imgreduce(ifile,overwrite=True)

        im:pil.Image = pil.open(ifile)
        self.assertTrue(2000 >= max(im.size))

        exif = None
        try:
            exif = piexif.load(im.info['exif'])
        except KeyError:
            pass # has no exif data
        im.close()
        self.assertTrue(exif is not None)

        print(os.path.getsize(ifile))






