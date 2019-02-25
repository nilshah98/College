x = input("Enter the first signal: ");
h = input("Enter the second signal: ");
lx = length(x);
lh = length(h);
d = lx - lh;
if( d>0 )
  for i=1:d;
    h(lh+i) = 0;
  end;
  n=lx;
elseif(d<0)
  d=-d;
  n=lh;
  for i=1:d;
    x(lx+i) = 0;
  end;
else
  n=lx;
end;
nn = (0:1:n-1);

subplot(3,1,1);
stem(nn,x);
xlabel("No of samples");
ylabel("Amplitude");
title("Signal X");

subplot(3,1,2);
stem(nn,h);
xlabel("No of samples");
ylabel("Amplitude");
title("Signal h");

x = x';
h = h';
for i=1:n
  for j=1:n
    k = mod((j-i+1),n);
    if(k==0)
      k=n;
    end;
    m(i,j)=h(k);
  end;
end;   
m= m';
y = m*x;
y = y';
disp(y);
subplot(3,1,3);
stem(nn,y);
xlabel("No of samples");
ylabel("Amplitude");
title("Circular Convolution y(n)");
