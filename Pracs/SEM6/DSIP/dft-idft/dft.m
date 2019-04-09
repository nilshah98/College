x = [1;2;3;4];

[N,t] = size(x);

W = zeros(N,N);

for n=1:N
    for k=1:N
        W(n,k) = cos((2*pi*(n-1)*(k-1))/N)-sin((2*pi*(n-1)*(k-1))/N)*1i;
    end
end

X = W*x;
inv = (conj(W)*X)/N;

disp("x");
disp(x);
disp("X");
disp(X);
disp("inverse");
disp(inv);

