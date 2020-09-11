#include <iostream>
#include <iomanip>


// very simple calculator 
int add(int a, int b){
    return a+b;
}
int subtract(int a, int b){
    return a-b;
}
int divide(int a, int b){
    return a/b;
}
int multiply(int a, int b){
    return a*b;
}


int main(){
    const size_t BUFFER_SIZE = 1024;
    int result;
    int a;
    int b;
    char * op = new char[BUFFER_SIZE];
    std::cout << "Type your first term:";
    std::cin >> a;
    std::cout << "Type your operator:";
    std::cin >> std::setw(BUFFER_SIZE) >> op;
    std::cout << "Type your final term:";
    std::cin >> b;
    
    if (*op=='+'){
        result= add(a,b);
    }
    else if (*op=='-'){
        result= subtract(a,b);
    }
    else if (*op=='/'){
        result= divide(a,b);
    }
    else if (*op=='*'){
        result= multiply(a,b);
    }
    std::cout << "= " << result << "\n";
    
    delete [] op;
    
    
    
}
