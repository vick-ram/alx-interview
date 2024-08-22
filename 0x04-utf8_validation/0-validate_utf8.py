#!/usr/bin/python3
"""0-validate_utf8 module"""


def validUTF8(data):
    """ Validate if the data set represents a valid UTF-8 encoding """

    num_bytes = 0

    for num in data:
        """Get the 8 least significant bits"""
        byte = num & 0xFF

        if num_bytes == 0:
            """Determine the number of bytes in the UTF-8 character"""
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            """For continuation bytes, they must start with '10'"""
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    """If all bytes have been processed, return True"""
    return num_bytes == 0
