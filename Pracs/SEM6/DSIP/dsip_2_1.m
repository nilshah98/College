n=input('Enter number of samples: ');
for i=1:n
    y(i)=input('Enter number: ');
	yalt(i) = input('Enter number for second wave: ');
end

di=floor(n/2);
x=-di:di;
display(x)
display(y)
subplot(3,3,1);
stem(x,y);
xlabel('no of samples');
ylabel('amplitude');
title('Original Input Signal');

d=input('Enter delay value: ');
subplot(3,3,2);
x=-di+d:di+d;
stem(x,y);
xlabel('no of samples');
ylabel('amplitude');
title('Delay');

a=input('Enter advance value: ');
subplot(3,3,3);
x=-di-a:di-a;
stem(x,y);
xlabel('no of samples');
ylabel('amplitude');
title('Advance');

subplot(3,3,4);
d=floor(n/2);
x=-d:d;
y1=fliplr(y);
stem(x,y1);
xlabel('no of samples');
ylabel('amplitude');
title('Inversion');

subplot(3,3,5);
y2=y1+y/2;
stem(x,y2);
xlabel('no of samples');
ylabel('amplitude');
title('Even component');

subplot(3,3,6);
y2=y-y1/2;
stem(x,y2);
xlabel('no of samples');
ylabel('amplitude');
title('Odd component');

subplot(3,3,7);
stem(x,yalt);
xlabel('no of samples');
ylabel('amplitude');
title('Second wave');

subplot(3,3,8);
y2 = y + yalt
stem(x,y2);
xlabel('no of samples');
ylabel('amplitude');
title('Addition');

subplot(3,3,9);
y2 = y .* yalt
stem(x,y2);
xlabel('no of samples');
ylabel('amplitude');
title('Multiplication');