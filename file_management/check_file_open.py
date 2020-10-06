# This snippet checks if the file is open

%%time
import os

try: 
    os.rename('file_name.csv', 'tempfile_name.csv')
    os.rename('tempfile_name.csv', 'file_name.csv')
    print('File is closed.')
except OSError:
    print('File is still open.')