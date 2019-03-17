"""
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

    For 1-byte character, the first bit is a 0, followed by its unicode code.
    For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.

This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.

"""
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        85ms
        """
        bin_data=[]
        for i in data:
            bin_data.append('{0:0>8}'.format(bin(i)[2:]))
        print(bin_data)
        l=len(data)
        if l<=0:
            return False
        count=0
        while count<l:
            if bin_data[count][0]=='0':
                count+=1
            else:
                count_bin=0
                while count_bin<8 and bin_data[count][count_bin]=='1':
                    count_bin+=1
                print(count_bin)
                if count_bin>4 or count_bin<=1:
                    return False
                else:
                    if count+count_bin>l:
                        print('sss')
                        return False
                    for i in range(1,count_bin):
                        if bin_data[count+i][0:2]!='10':
                            return False
                    count+=count_bin
        return True

    def validUtf8_1(self, data):
        """
        :type data: List[int]
        :rtype: bool
        42ms
        """
        count = 0
        for n in data:
            if n > 0b11110111:  # 247
                return False
            elif n >= 0b11110000:  # 240
                count += 3
            elif n >= 0b11100000:  # 224
                count += 2
            elif n >= 0b11000000:  # 192
                count += 1
            elif n >= 0b10000000:
                count -= 1
        return count == 0
print(Solution().validUtf8([145]))
print(Solution().validUtf8([197, 130, 1]))
data = [235, 140, 4]
print(Solution().validUtf8(data))
print('{0:0>8}'.format(bin(197)[2:]))