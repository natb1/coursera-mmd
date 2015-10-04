function [a b c] = hw1_1()

M = [
   0  0  0;
  .5  0  0;
  .5  1  1
 ];

Beta = .7;
r = pagerank(M, Beta) * 3;
a = r(1);
b = r(2);
c = r(3);

end
