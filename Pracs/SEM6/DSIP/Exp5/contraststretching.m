% pkg load image - for octave
a=imread('./spiderman.jpg');
b=rgb2gray(a);
imwrite(b,'gray.bmp');
% x = rows(b) - for octave;
% y = columns(b) - for octave;
size(b)
[x,y]=size(b);
r1=input('Enter r1: ');
s1=input('Enter s1: ');
r2=input('Enter r2: ');
s2=input('Enter s2: ');

for i=1:x
  for j=1:y
      c(i,j)=calcu(b(i,j),r1,s1,r2,s2);
  end
end

imwrite(c,'contrast.bmp');
imshow(c);

function s = calcu(r,r1,s1,r2,s2)
    if r <= r1
        %slope1
        s = round((r-0)*(r1-0)/(s1-0)) + 0;
    elseif r <= r2
        %slope2
        s = round((r-r1)*(r2-r1)/(s2-s1)) + s1;
    else
        %slope3
        s = round((r-r2)*(255-r2)/(255-s2)) + s2;
    end
end