function [a b c] = hw1_2()

M = [
   0  0  1;
  .5  0  0;
  .5  1  0
 ];

Beta = .85;
r = pagerank(M, Beta);
a = r(1);
b = r(2);
c = r(3);

end
