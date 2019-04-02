clc;
clear;

% pkg load image
a=imread('./taj.bmp');
% x=rows(b);
% y=columns(b);
[x,y]=size(a);

prompt = 'State a secret message ';
secret = input(prompt,'s');
binSecret = dec2bin(secret)-'0'
letter = 1;
pointer = 1;
[word,len] = size(binSecret);
c = zeros(x,y);

for i=1:x
  for j=1:y
    for k=1:8
      c(i,j,k)=bitget(a(i,j),k);
      if k==1
          if letter <= word
            c(i,j,k)=binSecret(letter,pointer);
            pointer = pointer + 1;
            if pointer == 8
                pointer = 1;
                letter = letter + 1;
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

% since character range only till 128 contained in 7 bits
decodedM = "";
letter = 1;
pointer = 7;
curr = 0;


for i=1:x
    for j=1:y
        if letter <= word
        curr = bitset(curr,pointer,bitget(fin(i,j),1));
        pointer = pointer - 1;
        if pointer == 0
            pointer = 7;
            decodedM = decodedM + char(curr);
            curr = 0;
            letter = letter + 1;
        end
        end
    end
end
disp("Decoded Message-");
disp(decodedM);
%for i=1:7
%  d=255 .* c(:,:,i);
%  imshow(d);
%  imwrite(d,strcat('img',num2str(i),'.bmp'));
%end


