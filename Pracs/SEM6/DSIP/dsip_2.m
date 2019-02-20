x = -10:10;
y = [zeros(1,10) 1 zeros(1,10)];
subplot(3,2,1);
stem(x,y);
title('impulse');
xlabel('n');
ylabel('f(n)');

x = -10:10;
y = [zeros(1,10) ones(1,11)];
subplot(3,2,2);
stem(x,y);
title('unit');
xlabel('n');
ylabel('f(n)');

x = -10:10;
y = [zeros(1,10) 0:10];
subplot(3,2,3);
stem(x,y);
title('ramp');
xlabel('n');
ylabel('f(n)');

x = -10:10;
a = 1.5;
y = [zeros(1,10) a.^(0:10) ];
subplot(3,2,4);
stem(x,y);
title('expo increasing');
xlabel('n');
ylabel('f(n)');

x = -10:10;
a = 0.5;
y = [zeros(1,10) a.^(0:10) ];
subplot(3,2,5);
stem(x,y);
title('expo decreasing');
xlabel('n');
ylabel('f(n)');

figure;

x = -6:0.2:6;
a = 2;
w = 1.3;
theta = pi;
y = a.*cos(w.*x+theta);
subplot(2,2,1);
stem(x,y);
title('Cos Discrete');
xlabel('n');
ylabel('f(n)');

x = -6:0.2:6;
a = 3;
w = 1.3;
theta = pi;
y = a.*cos(w.*x+theta);
subplot(2,2,2);
stem(x,y);
title('Cos Discrete a change');
xlabel('n');
ylabel('f(n)');

x = -6:0.2:6;
a = 2;
w = 2.4;
theta = pi;
y = a.*cos(w.*x+theta);
subplot(2,2,3);
stem(x,y);
title('Cos Discrete w change');
xlabel('n');
ylabel('f(n)');

x = -6:0.2:6;
a = 2;
w = 1.3;
theta = pi/2;
y = a.*cos(w.*x+theta);
subplot(2,2,4);
stem(x,y);
title('Cos Discrete theta change');
xlabel('n');
ylabel('f(n)');

figure;

x = -6:0.2:6;
a = 2;
w = 1.3;
theta = pi;
y = a.*sin(w.*x+theta);
subplot(2,2,1);
stem(x,y);
title('Sine Discrete');
xlabel('n');
ylabel('f(n)');

x = -6:0.2:6;
a = 3;
w = 1.3;
theta = pi;
y = a.*sin(w.*x+theta);
subplot(2,2,2);
stem(x,y);
title('Sine Discrete a change');
xlabel('n');
ylabel('f(n)');

x = -6:0.2:6;
a = 2;
w = 2.4;
theta = pi;
y = a.*sin(w.*x+theta);
subplot(2,2,3);
stem(x,y);
title('Sine Discrete w change');
xlabel('n');
ylabel('f(n)');

x = -6:0.2:6;
a = 2;
w = 1.3;
theta = pi/2;
y = a.*sin(w.*x+theta);
subplot(2,2,4);
stem(x,y);
title('Sine Discrete theta change');
xlabel('n');
ylabel('f(n)');

