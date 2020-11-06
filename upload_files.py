#!/usr/bin/env python  
# -*- coding: utf-8 -*-
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AlAxfJtvmMiCNMLKod7gOmYbfZkzx87EOf8tOKovAURiOGmdqogxd-puay0hlDkMQnF1u2eNWFYUS5VCzUoFCi_mgeH2KBfXAeRbc9IVj_GyA0jlqHtv0RqwlnGtzwlwd3mhf59-UIk'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the file path to transfer: "))
    file_to = input("Enter the full path to upload to dropbox: ")


    transferData.upload_file(file_from,file_to)
    print("Your file has been moved !!!")

if __name__ == '__main__':
    main()