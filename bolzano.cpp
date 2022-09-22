#include <bits/stdc++.h>
using namespace std;

float f(float x){
    return exp(x) + x;
}

string Center(string s, const int max){
    stringstream ss;
    int padding = (max - s.size()) / 2;
    if (padding == 1) padding++;
    for (int i = 0; i < padding; ++i) ss << ' ';
    ss << s;
    for (int i = 0; i < padding; ++i) ss << ' ';
    return ss.str();
}

string fmt(string s){
    return Center(s, 8) + '\t';
}

void header(){
    for(int i=0;i<90;i++) cout << '-'; cout << '\n';
    cout << fmt("x1") << fmt("x3") << fmt("x2") << fmt("f(x1)") << fmt("f(x3)") << fmt("f(x2)") << '\n';
    for(int i=0;i<90;i++) cout << '-'; cout << '\n';
}

float cek(float atas, float bawah, float x, float fA, float fB, float fX){
    float mn = min(abs(fA), min(abs(fB), abs(fX)));
    if (mn == abs(fA)) return atas;
    else if (mn == abs(fB)) return bawah;
    else return x;
}

void bolza(float atas, float bawah, float x, float fA, float fB, float fX){
    header();
    while(fabs(fX*10000) > 1) {
        printf("%2.6f\t%2.6f\t%2.6f\t%2.6f\t%2.6f\t%2.6f\n\n" , bawah, x, atas, fB, fX, fA);

        if(fA*fX > 0) atas = x, fA = fX; 
        else bawah = x, fB = fX; 
        
        x = (atas + bawah)/2;
        fA = f(atas), fB = f(bawah), fX = f(x); 
    }
    printf("%2.6f\t%2.6f\t%2.6f\t%2.6f\t%2.6f\t%2.6f\n\n" , bawah, x, atas, fB, fX, fA); 
    printf("x akhir = %5.6f\n", cek(atas, bawah, x, fA, fB, fX));
}

int main() {
    float atas, bawah, x, fA, fB, fX;
    printf("f(x) = exp(x) + x\nBatas atas\t: "); scanf("%f", &atas); 
    printf("Batas bawah\t: "); scanf("%f", &bawah);

    x = (atas + bawah)/2;
    fA = f(atas), fB = f(bawah), fX = f(x); 
    if(fA*fB >= 0) {
        printf("tanda sama = %3.5f %3.5f\n", fA, fB); 
        exit (0); 
    }
    bolza(atas, bawah, x, fA, fB, fX);
}