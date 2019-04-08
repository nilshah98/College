% clear all temporary variables from other files;
clear;
% clear command line
clc;

img = (imread('taj.bmp'));
imgGaus = imnoise(img,'gaussian');
imgSnP = imnoise(img,'salt & pepper');
subplot(3,2,1);
imshow(img);
xlabel("original image");
subplot(3,2,3);
imshow(imgGaus);
xlabel("gaussian noice");
subplot(3,2,4);
imshow(imgSnP);
xlabel("salt & pepper");

lowpassmatrix = [1/9 1/9 1/9 ; 1/9 1/9 1/9 ; 1/9 1/9 1/9];
highpassmatrix = [-1/9 -1/9 -1/9; -1/9 8/9 -1/9; -1/9 -1/9 -1/9];
highboostmatrix = [-1/9 -1/9 -1/9; -1/9 8.9/9 -1/9; -1/9 -1/9 -1/9];

[w,h] = size(img);
disp([w,h]);
img = double(img);
imgGaus = double(imgGaus);
imgSnP = double(imgSnP);

imgLPF = double(zeros(w,h));
imgHPF = double(zeros(w,h));

for i=1:w-2
    for j=1:h-2
        % disp(c);
        imgLPF(i+1,j+1) = round(sum(sum(imgGaus(i:i+2,j:j+2).*lowpassmatrix)));
        imgHPF(i+1,j+1) = round(sum(sum(img(i:i+2,j:j+2).*highpassmatrix)));
        imgHBF(i+1,j+1) = round(sum(sum(img(i:i+2,j:j+2).*highpassmatrix)));
        temp = imgSnP(i:i+2,j:j+2);
        imgMed(i+1,j+1) = median(temp(:));
    end;
end;


subplot(3,2,5);
imshow(uint8(imgLPF));
xlabel("Low pass");
subplot(3,2,2);
imshow(uint8(imgHPF));
xlabel("High pass");
subplot(3,2,6);
imshow(uint8(imgMed));
xlabel("Median pass");
subplot(3,2,1);
imshow(uint8(imgHBF));
xlabel("High boost filter");