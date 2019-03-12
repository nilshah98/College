% pkg load image
a=imread('./spiderman.jpg');
b=rgb2gray(a);
imshow(b);
imwrite(b,'gray.bmp');
% x=rows(b);
% y=columns(b);
[x,y] = size(b);
c=255 - b;
imwrite(c,'neg.bmp');
imshow(c);