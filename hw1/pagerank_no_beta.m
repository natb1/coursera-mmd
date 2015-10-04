function [R] = pagerank_no_beta(M)

n = size(M, 1);
r = ones(n, 1);
R = [];

for i = 1:5
  rprime = M * r;
  R = [R rprime];
  r = rprime;
end
