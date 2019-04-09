clc;
clear;

x = double(rgb2gray(imread('square.jpg')));

[N,t] = size(x);

W = zeros(N,N);

for n=1:N
    for k=1:N
        W(n,k) = cos((2*pi*(n-1)*(k-1))/N)-sin((2*pi*(n-1)*(k-1))/N)*1i;
    end
end

X = W*x*W;
inv = (conj(W)*X*W);

subplot(2,2,1);
imshow(x,[]);
title("Original Image");
subplot(2,2,2);
imshow(uint8(abs(X)),[]);
title("DFT image");
subplot(2,2,3);
title("IDFT image");
imshow(abs(inv),[]);
title("IDFT image");