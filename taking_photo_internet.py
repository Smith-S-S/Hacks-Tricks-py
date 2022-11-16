# This script downloads images from Bing search.
#ERROR: 
#urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)>

#if got error in mac
Euse this code additional

#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context)


#Bing

from bing_image_downloader import downloader
downloader.download("monkey", limit=20,  output_dir='images',adult_filter_off=True, force_replace=False, timeout=60)
downloader.download("tiger", limit=20,  output_dir='images',adult_filter_off=True, force_replace=False, timeout=60)






#for no error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context)
from bing_image_downloader import downloader
downloader.download("monkey", limit=20,  output_dir='images',adult_filter_off=True, force_replace=False, timeout=60)
downloader.download("tiger", limit=20,  output_dir='images',adult_filter_off=True, force_replace=False, timeout=60)

