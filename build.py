#reads in the bottom
#reads i the middle index.html
#assembles new file by combining
#writes the new file to a brand new file

top_html = open('./templates/top.html').read()
bottom_html = open('./templates/bottom.html').read()
middle_html = open('./content/index.html').read()
combined_html = top_html + middle_html + bottom_html
open ('./docs/index.html', 'w+').write(combined_html)
print (combined_html)
middle_html = open('./content/about.html').read()
combined_html = top_html + middle_html + bottom_html
open ('./docs/about.html', 'w+').write(combined_html)
print (combined_html)
middle_html = open('./content/contact.html').read()
combined_html = top_html + middle_html + bottom_html
open ('./docs/contact.html','w+').write(combined_html)

print (combined_html)
middle_html = open('./content/blog.html').read()
combined_html = top_html + middle_html + bottom_html
open ('./docs/blog.html', 'w+').write(combined_html)

print (combined_html)
middle_html = open('./content/testimonials.html').read()
combined_html = top_html + middle_html + bottom_html
open ('./docs/testimonials.html', 'w+').write(combined_html)

print (combined_html)
combined_html = top_html + middle_html + bottom_html
#./doc/  move images and css files to docs
#top and bottom do not need
#erika@erika-Inspiron-7300-2n1:~/Desktop/HW2/Erika$ python3 build.py




