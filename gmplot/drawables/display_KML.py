import json

class _DisplayKML(object):
    def __init__(self, url, **kwargs):
        '''
        Args:
            url (str): URL of KML to overlay.
        '''
        self._url = url

    def write(self, w):
        '''
        Write the kml

        Args:
            w (_Writer): Writer used to write the kml.
        '''
        w.write('new google.maps.KmlLayer(')
        w.indent()
        w.write('"%s",' % self._url)
        w.write('{suppressInfoWindows: true, preserveViewport: false, map: map}')
        w.dedent()
        w.write(');')
        w.write()
