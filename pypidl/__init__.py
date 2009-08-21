import os
import sys
from urlparse import urlparse
from urllib import urlretrieve
from pypidl.distmeta import __version__, VERSION
from yolk.setuptools_support import get_download_uri


def get_url(package, version=None, source=True, index=None):
    return get_download_uri(package, version, source, index)


def download_package(package, version=None, source=True, index=None,
        unlink=False, directory="."):
    uri = get_url(package, version, source, index)
    filename = download_uri(".", uri, unlink)
    if filename:
        print(filename)


def download_uri(directory, uri, unlink=False):
    filename = os.path.basename(urlparse(uri)[2])
    if os.path.exists(filename):
        if unlink:
            os.unlink(filename)
        else:
            raise Exception("ERROR: File exists: %s" % filename)

    try:
        downloaded_filename, headers = urlretrieve(uri, filename)
    except IOError, err_msg:
        sys.stderr.write("ERROR: %s: %s\n" % (uri, err_msg))

    if headers.gettype() in ["text/html"]:
        dfile = open(downloaded_filename)
        if re.search("404 Not Found", "".join(dfile.readlines())):
            dfile.close()
            sys.stderr.write("'404 Not Found' error\n")
            return None
        dfile.close()
    return filename

