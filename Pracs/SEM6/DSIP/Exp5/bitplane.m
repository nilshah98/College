pkg load image
a=imread('./martin-brechtl-1423370-unsplash.jpg');
b=rgb2gray(a);
imwrite(b,'gray.bmp');
x=rows(b);
y=columns(b);

for i=1:x
  for j=1:y
    for k=1:8
      c(i,j,k)=bitget(b(i,j),k);
    end
  end
end

for i=1:8
  d=255 .* c(:,:,i);
  imwrite(d,strcat("img",num2str(i),".bmp"));
end
