% pkg load image
a=imread('./spiderman.jpg');
b=rgb2gray(a);
imwrite(b,'gray.bmp');
% x=rows(b);
% y=columns(b);
[x,y]=size(b);
%threshold
t=input('Enter threshold: ');
for i=1:x
  for j=1:y
    if b(i,j)>=t
      d(i,j)=255;
     else
      d(i,j)=0;
    end
  end;
end;

imwrite(d,'threshold.bmp');
imshow(d);