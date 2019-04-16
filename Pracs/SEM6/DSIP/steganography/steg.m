clc;
clear;

a=imread('./taj.bmp');
[x,y]=size(a);

message = 'State a secret message ';
secret = input(message,'s');
secString = dec2bin(secret)-'0';
l = 1;
p = 1;
[row,col] = size(secString);
c = zeros(x,y,8);

for i=1:x
  for j=1:y
    for k=1:8
      c(i,j,k)=bitget(a(i,j),k);
      if k==1
          if l <= row
            c(i,j,k)=secString(l,p);
            p = p + 1;
            if p == 8
               p = 1;
               l = l + 1;
            end
          end
      end
    end
  end
end

fin = zeros(x,y);
for i=1:x
    for j=1:y
        for k=1:8
           fin(i,j) = bitset(fin(i,j),k,c(i,j,k));
        end
    end
end

fin = uint8(fin);
imwrite(fin,'encoded.bmp')

decodedM = "";
l = 1;
p = 7;
curr = 0;


for i=1:x
    for j=1:y
        if l <= row
        curr = bitset(curr,p,bitget(fin(i,j),1));
        p = p - 1;
        if p == 0
            p = 7;
            decodedM = decodedM + char(curr);
            curr = 0;
            l = l + 1;
        end
        end
    end
end
disp("Decoded Message-");
disp(decodedM);


