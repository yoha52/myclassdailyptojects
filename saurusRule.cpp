#include <iostream>
using namespace std;
struct matrixStruct
{
    int matrix[3][3];
};

int det(matrixStruct matPara)

{
    int matrix[3][3];
    //assing each matrix index
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            matrix[i][j] = matPara.matrix[i][j];
        }
    }

    int posetive = matrix[0][0] * matrix[1][1] * matrix[2][2] +
                   matrix[0][1] * matrix[1][2] * matrix[2][0] +
                   matrix[0][2] * matrix[1][0] * matrix[2][1];
    int negetive = matrix[0][2] * matrix[1][1] * matrix[2][0] +
                   matrix[0][0] * matrix[1][2] * matrix[2][1] +
                   matrix[0][1] * matrix[1][0] * matrix[2][2];
    int det = posetive - negetive;
    return det;
}
int main()
{
    matrixStruct mat = {{{1, 1, 1}, {2, 2, 2}, {7, 2, 9}}};
    cout << det(mat);
}