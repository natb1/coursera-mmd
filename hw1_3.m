function [R] = hw1_3()

M = [
   0  0  1;
  .5  0  0;
  .5  1  0
 ];

R = pagerank_no_beta(M);

end
