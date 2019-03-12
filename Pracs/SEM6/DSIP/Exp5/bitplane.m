% pkg load image
a=imread('./spiderman.jpg');
b=rgb2gray(a);
imwrite(b,'gray.bmp');
% x=rows(b);
% y=columns(b);
[x,y]=size(b);

for i=1:x
  for j=1:y
    for k=1:8
      c(i,j,k)=bitget(b(i,j),k);
    end
  end
end

for i=1:8
  d=255 .* c(:,:,i);
  imshow(d);
  imwrite(d,strcat('img',num2str(i),'.bmp'));
end
