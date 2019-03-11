pkg load image
a=imread('./martin-brechtl-1423370-unsplash.jpg');
b=rgb2gray(a);
imwrite(b,'gray.bmp');
x=rows(b);
y=columns(b);
%threshold
t=input('Enter threshold: ');
for i=1:x
  for j=1:y
    disp(b(i,j));
    if b(i,j)>=t
      d(i,j)=255;
     else
      d(i,j)=0;
    end
  end;
end;

imwrite(d,'threshold.bmp');
imshow(d);