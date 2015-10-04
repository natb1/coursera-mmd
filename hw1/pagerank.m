function [r] = pagerank(M, Beta)

epsilon = .00001;

n = size(M, 1);
r = ones(n, 1) / n;

converged = false
while not(converged)
  A = Beta * M + (1 - Beta) / n;
  rprime = A * r
  distance = norm(rprime - r)
  pause
  r = rprime;
  if distance <= epsilon
    converged = true;
  end
end
