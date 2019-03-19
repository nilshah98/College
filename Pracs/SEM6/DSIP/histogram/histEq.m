% clear all temporary variables from other files;
clear;
% clear command line
clc;

% use imhist to verify histogram created and histeq to equalise an image

image = imread('./babyincradle.png');
grayImage = (image);
[w,h] = size(grayImage);
imshow(grayImage);
% 1 row and 256 columns =>
pixelCount = zeros(1,256);


for i=1:w
    for j=1:h
        % Since arrays are one indexed =>
        pixelCount(1,grayImage(i,j)+1) = pixelCount(1,grayImage(i,j)+1)+1;
    end
end


totalPixels = sum(pixelCount);
originalPixel = zeros(1, totalPixels);

% to calculate total pixels, unused though;
finalPixel = zeros(1, totalPixels);
pdf = pixelCount(1,:)./totalPixels;
cdf = zeros(1,256);

%initialise first value of cdf
cdf(1,1) = pdf(1,1);

%calculate cdf
for i=2:256
    cdf(1,i) = cdf(1,i-1) + pdf(1,i);
end

colorMap = round(cdf(1,:)*255);

equalisedImage = zeros(w,h);
equalisedHist = zeros(1,256);


for i=1:w
    for j=1:h
        equalisedImage(i,j) = colorMap(1, grayImage(i,j)+1);
        equalisedHist(1,equalisedImage(i,j)+1) = equalisedHist(1,equalisedImage(i,j)+1) + 1;
        finalPixel(1,(i*j)+j) = colorMap(1, grayImage(i,j)+1);
        originalPixel(1,(i*j)+j) = grayImage(i,j);
    end
end


subplot(3,2,1);
hist(double(grayImage(:)'),256);
xlabel('pixelCount')
subplot(3,2,2);
plot(imhist(grayImage));
xlabel('imhist')

subplot(3,2,3);
hist(double(equalisedImage(:)'),256);
xlabel('equalised Histogram');
subplot(3,2,4);
plot(imhist(histeq(grayImage)));
xlabel('imhist <= histeq');

% disp(equalisedImage(1,1:10));
% disp(uint8(equalisedImage(1,1:10)));

subplot(3,2,5);
imshow(uint8(equalisedImage));
xlabel('equalised Image')
subplot(3,2,6);
imshow(histeq(grayImage));
xlabel('histeq');