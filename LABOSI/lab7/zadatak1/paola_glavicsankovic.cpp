#include <iostream>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/vector.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/numeric/ublas/lu.hpp>
#include <cstring>

using namespace boost::numeric::ublas;
int main(){
    char jmbag[11]="0036522290";
    
    //task a) creating m1, m2 and v
    matrix<int> m1 (5, 5), m2(5, 5);
    identity_matrix<int> m (5);
    
    //filling m1 with the first 5 digits of JMBAG 
    for (unsigned i = 0; i < m1.size1 (); ++ i) {
        for (unsigned j = 0; j < m1.size2 (); ++ j){
            m1(i, j)= boost::lexical_cast<int>(jmbag[j]);
        }
    }  
    //filling m2 (sum of m1 and identity matrix)
    m2=m1 + m;
    //creating vector v and filling it with the last 5 digits of JMBAG
    vector<int> v (5);
    for (unsigned i=0 ; i < v.size(); i++) {
        v(i)=boost::lexical_cast<int>(jmbag[5 + i]);
    }
    
    //task b) multiply m2 and v 
    auto result = prod(m2, v);
    std::cout << result << std::endl;
    
    //task c) vector v * (vector v)T
    auto v2 = trans(v);
    auto productI= inner_prod(v, v2);
    std::cout << productI << std::endl;
    
    //task d) sum of m1 and m2
    auto sumMatrix=m1 + m2;
    std::cout << sumMatrix << std::endl;
   
   //task e) inverse of m2
   matrix<double> m2_copy (5,5);
   m2_copy=m2;
   permutation_matrix<double> pm(m2_copy.size1());
   
   matrix<double> inverse (5,5);
   for (int i=0; i < inverse.size1(); ++ i) {
       for (int j=0; j < inverse.size2(); ++j) {
           if (i==j) {
               inverse(i, j)=1;
           }
       }
   }
   int res=lu_factorize(m2_copy, pm);
   lu_substitute(m2_copy, pm, inverse);
   std::cout << inverse << std::endl;
    

    return 0;
}
