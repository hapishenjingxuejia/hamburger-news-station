#include <iostream>
#include <cmath>

using namespace std;

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // 交换 arr[j] 和 arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    char op;
    double num1, num2, result;

    cout << "请输入操作符(+, -, *, /, ^, r, s)：" << endl;
    cin >> op;

    if (op == '+' || op == '-' || op == '*' || op == '/' || op == '^' || op == 'r' || op == 's') {
        if (op != 's') {
            cout << "请输入两个数字：" << endl;
            cin >> num1 >> num2;
        }

        switch (op) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    cout << "错误:除数不能为0" << endl;
                    return 1;
                }
                break;
            case '^':
                result = pow(num1, num2);
                break;
            case 'r':
                result = sqrt(num1);
                break;
            case 's': {
                int arr[] = {64, 34, 25, 12, 22, 11, 90};
                int n = sizeof(arr)/sizeof(arr[0]);
                
                cout << "原始数组：";
                for (int i=0; i < n; i++) {
                    cout << arr[i] << " ";
                }
                cout << endl;

                bubbleSort(arr, n);

                cout << "排序后的数组：";
                for (int i=0; i < n; i++) {
                    cout << arr[i] << " ";
                }
                cout << endl;
                return 0;
            }
        }

        if (op != 's') {
            cout << "结果：" << result << endl;
        }
    } else {
        cout << "错误：不支持的操作符" << endl;
        return 1;
    }

    return 0;
}
