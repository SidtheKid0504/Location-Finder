import exiftool
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from GPSPhoto import gpsphoto
from geopy.geocoders import Nominatim


class FindLocation:

    def __init__(self):
        pass

    def get_coords(self, filename):
        if filename.lower().endswith(('jpg', 'jpeg')):
            data = gpsphoto.getGPSData(filename)
            coords = [data['Latitude'], data['Longitude']]
            return coords

        elif filename.lower().endswith(('mov', 'mp4')):
            with exiftool.ExifTool() as et:
                metadata = et.get_metadata_batch(filename)
                coords = metadata[0]['Composite:GPSPosition']

                return coords
        else:
            return ("Not Correct File")
        
   def get_location(self, filename):
        coords = self.get_coords(filename)
        locator = Nominatim(user_agent="myGeocoder")
        location = locator.reverse(coords)

        return location.raw['address']

