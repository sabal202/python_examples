#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

class SegmentTree {
public:
    vector<int> Tree; //Основное дерево
    int len; //разм

    void BuildTree(vector<int>& a, int v, int tl, int tr) //Установка
    {
        if (tl == tr)
            Tree[v] = a[tl];
        else {
            int tm = (tl + tr) / 2;
            BuildTree(a, v * 2, tl, tm);
            BuildTree(a, v * 2 + 1, tm + 1, tr);
            Tree[v] = Tree[v * 2] + Tree[v * 2 + 1];
        }
    }

    int Summa(int Left, int Right) //S
    {
        return GetSum(1, 0, len - 1, Left, Right);
    }

    int GetSum(int v, int LPos, int RPos, int Left, int Right)
    {
        if (Left > Right)
            return 0;
        if ((Left == LPos) && (Right == RPos))
            return Tree[v];
        int Middle = (LPos + RPos) / 2;
        return GetSum(v * 2, LPos, Middle, Left, min(Right, Middle)) + GetSum(v * 2 + 1, Middle + 1, RPos, max(Left, Middle + 1), Right);
    }

    void update(int Position, int Val) //M
    {
        GetUpdt(1, 0, len - 1, Position, Val);
    }

    void GetUpdt(int v, int LPos, int RPos, int Position, int Val)
    {
        if (LPos == RPos)
            Tree[v] = Val;
        else {
            int Middle = (LPos + RPos) / 2;
            if (Position <= Middle)
                GetUpdt(v * 2, LPos, Middle, Position, Val);
            else
                GetUpdt(v * 2 + 1, Middle + 1, RPos, Position, Val);
            Tree[v] = Tree[v * 2] + Tree[v * 2 + 1];
        }
    }
    SegmentTree(vector<int>& v)
    {
        len = (int)v.size();
        Tree.resize(4 * len);
        BuildTree(v, 1, 0, len - 1);
    }
    SegmentTree(int n)
    {
        len = n;
        Tree.resize(4 * n);
    }
};

vector<int> v;

int n, q, i, j, d, f, t;

int main(void)
{
    cin >> n >> q; //Input
    v.resize(n + 1);
    for (i = 1; i <= n; i++)
        cin >> v[i];
    SegmentTree s(v);

    for (j = 0; j < q; j++) {
        char c;
        cin >> c;
        if (c == 'S') //Сумма
        {
            cin >> f >> t;
            cout << s.Summa(f + 1, t + 1) << endl;
        }
        else //Одновляем
        {
            cin >> i >> d;
            s.update(i + 1, d);
        }
    }
    return 0;
}