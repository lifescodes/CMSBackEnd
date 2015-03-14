from lifecode import settings
from datetime import date
import os
import string
from PIL import Image

class MediaHelper:

    def getTodayPath(self):
        today = date.today()
        year = str(today.year)+'/'
        month = str(today.month)+'/'
        day = str(today.day)+'/'
        path_today = os.path.join(year, month, day)
        return path_today;

    def getPath(self, file_type):
        path = ''
        path_today = self.getTodayPath()
        if file_type == 'image':
            base_path = settings.base.UPLOAD_IMAGE_ROOT
            path = os.path.join(base_path, path_today)
        elif file_type == 'audio':
            base_path = settings.base.UPLOAD_AUDIO_ROOT
            path = os.path.join(base_path, path_today)
        elif file_type == 'video':
            base_path = settings.base.UPLOAD_VIDEO_ROOT
            path = os.path.join(base_path, path_today)
        else:
            base_path = settings.base.UPLOAD_OTHER_ROOT
            path = os.path.join(base_path, path_today)

        return path;

    def getURL(self, file_type):
        url = ''
        path_today = self.getTodayPath()
        if file_type == 'image':
            base_url = settings.base.UPLOAD_IMAGE_URL
            url = os.path.join(base_url, path_today)
        elif file_type == 'audio':
            base_url = settings.base.UPLOAD_AUDIO_URL
            url = os.path.join(base_url, path_today)
        elif file_type == 'video':
            base_url = settings.base.UPLOAD_VIDEO_URL
            url = os.path.join(base_url, path_today)
        else:
            base_url = settings.base.UPLOAD_OTHER_URL
            url = os.path.join(base_url, path_today)

        return url


    def format_filename(self, s):
        """
        https://gist.github.com/seanh/93666
        https://github.com/seanh
        http://seanh.cc/

        Take a string and return a valid filename constructed from the string.
        Uses a whitelist approach: any characters not present in valid_chars are
        removed. Also spaces are replaced with underscores.

        Note: this method may produce invalid filenames such as ``, `.` or `..`
        When I use this method I prepend a date string like '2009_01_15_19_46_32_'
        and append a file extension like '.txt', so I avoid the potential of using
        an invalid filename.

        """
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        filename = ''.join(c for c in s if c in valid_chars)
        filename = filename.replace(' ','_') # I don't like spaces in filenames.
        return filename



    def resizeAndCrop(self, img_path, modified_path, size, crop_type='top'):
        """
        Christian Felipe Alvarez
        https://github.com/sigilioso
        https://gist.github.com/sigilioso/2957026

        Resize and crop an image to fit the specified size.

        args:
            img_path: path for the image to resize.
            modified_path: path to store the modified image.
            size: `(width, height)` tuple.
            crop_type: can be 'top', 'middle' or 'bottom', depending on this
                value, the image will cropped getting the 'top/left', 'midle' or
                'bottom/rigth' of the image to fit the size.
        raises:
            Exception: if can not open the file in img_path of there is problems
                to save the image.
            ValueError: if an invalid `crop_type` is provided.
        """
        # If height is higher we resize vertically, if not we resize horizontally
        img = Image.open(img_path)
        # Get current and desired ratio for the images
        img_ratio = img.size[0] / float(img.size[1])
        ratio = size[0] / float(size[1])
        #The image is scaled/cropped vertically or horizontally depending on the ratio
        if ratio > img_ratio:
            img = img.resize((size[0], size[0] * img.size[1] / img.size[0]),
                    Image.ANTIALIAS)
            # Crop in the top, middle or bottom
            if crop_type == 'top':
                box = (0, 0, img.size[0], size[1])
            elif crop_type == 'middle':
                box = (0, (img.size[1] - size[1]) / 2, img.size[0], (img.size[1] + size[1]) / 2)
            elif crop_type == 'bottom':
                box = (0, img.size[1] - size[1], img.size[0], img.size[1])
            else :
                raise ValueError('ERROR: invalid value for crop_type')
            img = img.crop(box)
        elif ratio < img_ratio:
            img = img.resize((size[1] * img.size[0] / img.size[1], size[1]),
                    Image.ANTIALIAS)
            # Crop in the top, middle or bottom
            if crop_type == 'top':
                box = (0, 0, size[0], img.size[1])
            elif crop_type == 'middle':
                box = ((img.size[0] - size[0]) / 2, 0, (img.size[0] + size[0]) / 2, img.size[1])
            elif crop_type == 'bottom':
                box = (img.size[0] - size[0], 0, img.size[0], img.size[1])
            else :
                raise ValueError('ERROR: invalid value for crop_type')
            img = img.crop(box)
        else :
            img = img.resize((size[0], size[1]),
                    Image.ANTIALIAS)
            # If the scale is the same, we do not need to crop
        img.save(modified_path)
