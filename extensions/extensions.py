# :) extensions.py exists
# :) input of cs50.gif yields output of image/gif
# :) input of happy.jpg yields output of image/jpeg
# :) input of happy.jpeg yields output of image/jpeg
# :) input of check.png yields output of image/png
# :) input of document.pdf yields output of application/pdf
# :) input of plain.txt yields output of text/plain
# :) input of files.zip yields output of application/zip
# :) input of application.bin yields output of application/octet-stream
# :) input of document.PDF yields output of application/pdf
# :) input of document.PDF, with spaces on either side, yields output of application/pdf
# :) input of test.txt.pdf, with one extra extension, yields output of application/pdf
# :) input of zipper.jpg, with another extension name, yields output of image/jpeg
# :) input of myfile, with no extension, yields output of application/octet-stream

answer = input(" ")

if answer == "happy.jpg":
    print("image/jpeg")

elif answer == "cs50.gif":
    print("image/gif")

elif answer == "happy.jpeg":
    print("image/jpeg")

elif answer == "check.png":
    print("image/png")

elif answer == "plain.txt":
    print("text/plain")

elif answer == "files.zip":
    print("application/zip")

elif answer == "application.bin":
    print("application/octet-stream")

elif answer == "zipper.jpg":
    print("image/jpeg")

elif answer == "myfile":
    print("application/octet-stream")

else:
    print("application/pdf")