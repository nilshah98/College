pkg load image
a=imread('./martin-brechtl-1423370-unsplash.jpg');
b=rgb2gray(a);
imshow(b);
imwrite(b,'gray.bmp');
x=rows(b);
y=columns(b);
r1=input('Enter r1: ');
r2=input('Enter r2: ');

for i=1:x
  for j=1:y
    if(b(i,j)>r1 && b(i,j)<=r2)
      c(i,j)=255;
     else
      c(i,j)=0;
    end
  end
end
  
      
imwrite(c,'grayswnb.bmp');
imshow(c);