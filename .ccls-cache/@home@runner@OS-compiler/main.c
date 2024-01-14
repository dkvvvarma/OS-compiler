#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of processes: ";
    cin >> n;

    vector<int> poce(n), burst(n), wait(n), comp(n);

    cout << "Enter the processes: ";
    for (int i = 0; i < n; i++) {
        cin >> poce[i];
    }

    cout << "Enter the burst time: ";
    for (int i = 0; i < n; i++) {
        cin >> burst[i];
    }

    wait[0] = 0;
    for (int i = 1; i < n; i++) {
        wait[i] = burst[i-1] + wait[i-1];
    }
    int wt = 0;
    for (int i = 0; i < n; i++) {
        wt += wait[i];
    }
    double awt = (double) wt / n;
    cout << "Average waiting time is: " << awt << endl;

    comp[0] = burst[0];
    for (int i = 1; i < n; i++) {
        comp[i] = burst[i] + comp[i-1];
    }
    int ct = 0;
    for (int i = 0; i < n; i++) {
        ct += comp[i];
    }
    double act = (double) ct / n;
    cout << "The completion time is: " << act << endl;

    return 0;
}
