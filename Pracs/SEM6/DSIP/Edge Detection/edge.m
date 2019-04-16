img = double(rgb2gray(imread('rose.jpg')));

[r,c]=size(img);

matrix = [zeros(1,c);img;zeros(1,c)];
matrix = [zeros(r+2,1) matrix zeros(r+2,1)];

matrix2 = [img;zeros(1,c)];
matrix2 = [matrix2 zeros(r+1,1)];

prewitt_x = zeros(r,c);
prewitt_y = zeros(r,c);
prewitt = zeros(r,c);

sobel_x = zeros(r,c);
sobel_y = zeros(r,c);
sobel = zeros(r,c);

robert_x = zeros(r,c);
robert_y = zeros(r,c);
robert = zeros(r,c);

second_order = zeros(r,c);

for i=1:r
    for j=1:c
        sum = 0;
        sum = (-matrix2(i,j)+0*matrix2(i,j+1)+0*matrix2(i+1,j)+matrix2(i+1,j+1));
        robert_x(i,j) = round(sum);
    end
end

for i=1:r
    for j=1:c
        sum = 0;
        sum = (0*matrix2(i,j)-matrix2(i,j+1)+matrix2(i+1,j)+0*matrix2(i+1,j+1));
        robert_y(i,j) = round(sum);
    end
end

for i=1:r
    for j=1:c
        sum = 0;
        sum = (-matrix2(i,j)-matrix2(i,j+1)+matrix2(i+1,j)+matrix2(i+1,j+1));
        robert(i,j) = round(sum);
    end
end

for i=1:r
    for j=1:c
        sum = 0;
        sum = (-matrix(i,j)-matrix(i,j+1)-matrix(i,j+2)+0*matrix(i+1,j)+0*matrix(i+1,j+1)+0*matrix(i+1,j+2)+matrix(i+2,j)+matrix(i+2,j+1)+matrix(i+2,j+2));
        prewitt_x(i,j) = round(sum);
    end
end


for i=1:r
    for j=1:c
        sum = 0;
        sum = (-matrix(i,j)+0*matrix(i,j+1)+matrix(i,j+2)-matrix(i+1,j)+0*matrix(i+1,j+1)+matrix(i+1,j+2)-matrix(i+2,j)+0*matrix(i+2,j+1)+matrix(i+2,j+2));
        prewitt_y(i,j) = round(sum);
    end
end

for i=1:r
    for j=1:c
        sum = 0;
        sum = (-2*matrix(i,j)-matrix(i,j+1)+0*matrix(i,j+2)-matrix(i+1,j)+0*matrix(i+1,j+1)+matrix(i+1,j+2)+0*matrix(i+2,j)+matrix(i+2,j+1)+2*matrix(i+2,j+2));
        prewitt(i,j) = round(sum);
    end
end

for i=1:r
    for j=1:c
        sum = 0;
        sum = (-matrix(i,j)-2*matrix(i,j+1)-matrix(i,j+2)+0*matrix(i+1,j)+0*matrix(i+1,j+1)+0*matrix(i+1,j+2)+matrix(i+2,j)+2*matrix(i+2,j+1)+matrix(i+2,j+2));
        sobel_x(i,j) = round(sum);
    end
end


for i=1:r
    for j=1:c
        sum = 0;
        sum = (-matrix(i,j)+0*matrix(i,j+1)+matrix(i,j+2)-2*matrix(i+1,j)+0*matrix(i+1,j+1)+2*matrix(i+1,j+2)-matrix(i+2,j)+0*matrix(i+2,j+1)+matrix(i+2,j+2));
        sobel_y(i,j) = round(sum);
    end
end

for i=1:r
    for j=1:c
        sum = 0;
        sum = (-2*matrix(i,j)-2*matrix(i,j+1)+0*matrix(i,j+2)-2*matrix(i+1,j)+0*matrix(i+1,j+1)+2*matrix(i+1,j+2)+0*matrix(i+2,j)+2*matrix(i+2,j+1)+2*matrix(i+2,j+2));
        sobel(i,j) = round(sum);
    end
end

for i=1:r
    for j=1:c
        sum = 0;
        sum = (0*matrix(i,j)-matrix(i,j+1)+0*matrix(i,j+2)-matrix(i+1,j)+4*matrix(i+1,j+1)-matrix(i+1,j+2)+0*matrix(i+2,j)-matrix(i+2,j+1)+0*matrix(i+2,j+2));
        second_order(i,j) = round(sum);
    end
end

subplot(2,2,1);
imshow(uint8(img));
title("original image");
subplot(2,2,2);
imshow(uint8(robert_x));
title("robert X");
subplot(2,2,3);
imshow(uint8(robert_y));
title("robert Y");
subplot(2,2,4);
imshow(uint8(robert));
title("robert");

figure;

subplot(2,2,1);
imshow(uint8(img));
title("original image");
subplot(2,2,2);
imshow(uint8(prewitt_x));
title("prewitt X");
subplot(2,2,3);
imshow(uint8(prewitt_y));
title("prewitt Y");
subplot(2,2,4);
imshow(uint8(prewitt));
title("prewitt");

figure;

subplot(2,2,1);
imshow(uint8(img));
title("original image");
subplot(2,2,2);
imshow(uint8(sobel_x));
title("sobel X");
subplot(2,2,3);
imshow(uint8(sobel_y));
title("sobel Y");
subplot(2,2,4);
imshow(uint8(sobel));
title("sobel");

figure;

subplot(2,2,1);
imshow(uint8(img));
title("original image");
subplot(2,2,2);
imshow(uint8(sobel_x));
title("Second order");

