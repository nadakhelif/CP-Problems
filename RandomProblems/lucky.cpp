#include <iostream>
using namespace std;
int main(){
    long long a,b=0;
    cin >> a;
    string x = to_string(a);
    for(int i=0;i<x.length();i++){
        if(x[i]=='4' || x[i]=='7'){
            b++;
        }
    }
    cout << b;
    if(b==4 || b==7){
        cout << "YES";
    }else{cout << "NO";}
}
