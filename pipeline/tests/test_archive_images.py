import tempfile
import unittest
from pathlib import Path

from pipeline import archive


def fake_jpeg(width, height):
    """A JPEG's opening markers: SOI, an APP0 segment, then a baseline SOF0 frame header."""
    app0 = b"\xff\xe0" + (16).to_bytes(2, "big") + b"JFIF\x00" + bytes(9)
    sof = b"\xff\xc0" + (17).to_bytes(2, "big") + b"\x08" + height.to_bytes(2, "big") + width.to_bytes(2, "big") \
        + bytes(10)
    return b"\xff\xd8" + app0 + sof + b"\xff\xd9"


class JpegGeometry(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.path = Path(folder.name) / "page.jpg"
        self.path.write_bytes(fake_jpeg(1648, 2694))

    def test_size_from_frame_header(self):
        self.assertEqual(archive.jpeg_size(self.path), (1648, 2694))

    def test_box_scaled_and_clipped(self):
        # hOCR pixels are twice the image's: halved, and clipped at the right edge.
        self.assertEqual(archive._pixel_box(self.path, (3296, 5388), (100, 200, 3400, 260)), (50, 100, 1598, 30))


if __name__ == "__main__":
    unittest.main()
