pkg load image
a=imread('./martin-brechtl-1423370-unsplash.jpg');
b=rgb2gray(a);
imshow(b);
imwrite(b,'gray.bmp');
x=rows(b);
y=columns(b);
c=255 .- b;
imwrite(c,'neg.bmp');
imshow(c);