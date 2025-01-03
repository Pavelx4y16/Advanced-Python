# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    
    s = "This is a string"
    print(s)
    
    # Try combining them.
    # print(b + s)
    
    # Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    s_encoded = s.encode()
    print(b + s_encoded)

    b_decoded = b.decode()
    print(b_decoded + s)
    
    # encode the string as UTF-32
    print(s.encode('utf-8'))


if __name__ == "__main__":
    main()
