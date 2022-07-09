#pragma once
#include<iostream>
#include<fstream>
#include<stack>
#include<utility>
#include<map>
#include<string>
#include<sstream>
using namespace std;

char G[20][20];             //存放输入的文法 用@表示空 产生式以$结尾
int  length[20];            // 每条产生式的长度
int  number = 0;            // 产生式的个数
bool tempofinput[150];      //记录在文法中的字符
char str_vn[20];            //非终结符
int  size_vn = 0;           //非终结符的个数
char str_vt[150];           //终结符
int  size_vt = 0;           //终结符的个数
bool first_vn[30][150];     //记录每个非终结符的first集
char buffer[50];            //缓冲区 用来存放生成CLOSURE(I)时需要的first_set 也用来读入用户的输入串^_^
int  bsize = 0;             //buffer字符串的有效长度

struct thri {               //定义状态转换数组中的元素格式
    int beg;
    int nex;
    char ch;
};
thri trans[200];            //用来在GO（）函数中记录状态间的转换
int  size_trans = 0;        //trans数组的大小

struct proj {               //定义项目的形式
    int formula_numb;       //产生式的编号
    int part;               //原点的位置
    char expc;              //展望
};
//项目集
proj    items[100][100];    //项目集族
int     Ccount = 0;         //项目集的个数
int     size_item[100];     //单个项目集的大小

//状态转换表
struct action {
    char    ch;
    int     nxt_sta;
};

action    action_table[100][100];   //状态转换表
int       size_act_table[100];      //状态转换表的大小

ifstream  G_ifile;                  //输入文法的文件指针
ifstream  input_ifile;              //输入句子的文件指针
ofstream  items_ofile;              //输出项目集族的文件指针
ofstream  act_ofile;                //输出转换表的文件指针


//
string int_to_string(int a) {
    ostringstream temp;
    temp << a;
    return temp.str();
}
//读入文法
void Read_G()
{ 
    //读入文法
    G_ifile >> number;
    for (int i = 1; i <= number; i++) {
        char temp;
        int j = 0;
        G_ifile >> temp;
        while (temp != '$') {
            tempofinput[temp] = true;
            G[i][j++] = temp;
            G_ifile >> temp;
        }
        length[i] = j;
    }
    //生成拓广文法
    G[0][0] = 'S';
    tempofinput[G[0][0]] = true;
    G[0][1] = G[1][0];
    length[0] = 2;
    //统计文法中的终结符和非终结符
    for (int i = 0; i < 64; i++)
        if (tempofinput[i])
            str_vt[size_vt++] = i;
    for (int i = 91; i < 128; i++)
        if (tempofinput[i])
            str_vt[size_vt++] = i;
    for (int i = 65; i < 91; i++)
        if (tempofinput[i])
            str_vn[size_vn++] = i;
}

//计算每个非终结符的first集
void get_first() {
    bool flag1;
    do {
        flag1 = false;
        for (int i = 1; i <= number; i++) {
            int t = 1;
            bool flag2;
            do {
                flag2 = false;
                //该符号是非终结符
                if (G[i][t] >= 'A' && G[i][t] <= 'Z') {
                    for (int k = 0; k < 64; k++)
                        if (first_vn[G[i][t] - 'A'][k] == true && !first_vn[G[i][0] - 'A'][k]) {
                            first_vn[G[i][0] - 'A'][k] = true;
                            flag1 = true;
                        }
                    for (int k = 91; k < 128; k++)
                        if (first_vn[G[i][t] - 'A'][k] == true && !first_vn[G[i][0] - 'A'][k]) {
                            first_vn[G[i][0] - 'A'][k] = true;
                            flag1 = true;
                        }
                    if (first_vn[G[i][t] - 'A'][64] == true) { //若该非终结符的first集有空则继续向后找。
                        t++;
                        flag2 = true;
                    }
                }
                else if (!first_vn[G[i][0] - 'A'][G[i][t]]) {
                    first_vn[G[i][0] - 'A'][G[i][t]] = true;
                    flag1 = true;
                }
            } while (flag2 && t < length[i]);
            if (t == length[i])
                first_vn[G[i][0] - 'A'][26] = true;
        }
    } while (flag1);
}

//判断项目temp是否在项目集T里
bool is_in(proj temp, int T) {
    for (int i = 0; i < size_item[T]; i++)
        if (temp.formula_numb == items[T][i].formula_numb && temp.part == items[T][i].part && temp.expc == items[T][i].expc)
            return true;
    return false;
}

//计算在生成CLOSURE(I)时用到的FIRST(ba);
void  gete_expc(proj temp) {
    bsize = 0;
    bool flag;
    int tt = temp.part;
    do {
        flag = false;
        if (tt + 1 >= length[temp.formula_numb]) {
            buffer[bsize++] = temp.expc;
            return;
        }
        else if (G[temp.formula_numb][tt + 1] < 'A' || G[temp.formula_numb][tt + 1] > 'Z') {
            buffer[bsize++] = G[temp.formula_numb][tt + 1];
            return;
        }
        else if (G[temp.formula_numb][tt + 1] >= 'A' && G[temp.formula_numb][tt + 1] <= 'Z') {
            for (int i = 0; i < 64; i++) {
                if (first_vn[G[temp.formula_numb][tt + 1] - 'A'][i])
                    buffer[bsize++] = i;
            }
            for (int i = 91; i < 128; i++) {
                if (first_vn[G[temp.formula_numb][tt + 1] - 'A'][i])
                    buffer[bsize++] = i;
            }
            if (first_vn[G[temp.formula_numb][tt + 1] - 'A'][64]) {
                tt++;
                flag = true;
            }
        }
    } while (flag);
}

//计算items[T]的closure闭包
void e_closure(int T) {
    for (int i = 0; i < size_item[T]; i++) {
        proj temp;
        if (G[items[T][i].formula_numb][items[T][i].part] >= 'A' && G[items[T][i].formula_numb][items[T][i].part] <= 'Z') {
            for (int j = 0; j < 20; j++)
                if (G[j][0] == G[items[T][i].formula_numb][items[T][i].part]) {
                    gete_expc(items[T][i]);
                    for (int k = 0; k < bsize; k++) {
                        temp.formula_numb = j;
                        temp.part = 1;
                        temp.expc = buffer[k];
                        if (!is_in(temp, T))
                            items[T][size_item[T]++] = temp;
                    }
                    bsize = 0;
                }
        }
    }
    return;
}

//判断新生成的项目集是否已经在项目集族中了
int is_contained()
{
    for (int i = 0; i < Ccount; i++) {
        int s = 0;        //记录有多少是匹配的
        if (size_item[i] == size_item[Ccount])
            for (int j = 0; j < size_item[Ccount]; j++) {
                for (int k = 0; k < size_item[i]; k++)
                    if ((items[Ccount][j].formula_numb == items[i][k].formula_numb) && (items[Ccount][j].part == items[i][k].part) && (items[Ccount][j].expc == items[i][k].expc)) {
                        s++;
                        break;
                    }
            }
        if (s == size_item[Ccount])
            return i;
    }
    return 0;
}

//打印项目集
void print_projs(int T) {
    cout << C_YELLOW << "I" << T << ";" << C_CLOSE << endl;
    items_ofile << "I" << T << ":" << endl;
    for (int i = 0; i < size_item[Ccount]; i++) {
        //格式化输出
        cout << C_RED << G[items[Ccount][i].formula_numb][0] << C_YELLOW << "->";
        for (int j = 1; j <= length[items[Ccount][i].formula_numb]; j++) {
            if (items[Ccount][i].part == j) {
                cout << C_YELLOW << "." << C_CLOSE;
            }
            cout << C_RED << G[items[Ccount][i].formula_numb][j];
        }
        cout << setiosflags(ios::right) << setw(20 - length[items[Ccount][i].formula_numb]) << "展望：" << items[Ccount][i].expc << endl;

        //cout << C_RED << items[Ccount][i].formula_numb << " , " << items[Ccount][i].part << " , " << items[Ccount][i].expc << C_CLOSE << endl;
        //items_ofile << items[Ccount][i].formula_numb << " , " << items[Ccount][i].part << " , " << items[Ccount][i].expc << endl;
    }
}

//实现GO（I,X）的功能
void GO() {
    cout << C_YELLOW << "************************** 项目集族 ************************" << endl;

    //获取项目集I0
    proj init;
    init.expc = '#';
    init.formula_numb = 0;
    init.part = 1;
    items[0][0] = init;
    size_item[0]++;

    //求I0的闭包
    e_closure(0);
    //打印项目集I0
    print_projs(0);
    cout << C_YELLOW << "***************************************" << C_CLOSE << endl;

    //对每个项目集进行分析
    for (int index = 0; index <= Ccount; index++) {

        //对.后面是终结符进行分析
        for (int j = 0; j < size_vt; j++) {
            proj    buf[50];
            int     buf_size = 0;
            proj    tp;
            for (int p = 0; p < size_item[index]; p++) {
                if ((items[index][p].part < length[items[index][p].formula_numb]) && (G[items[index][p].formula_numb][items[index][p].part] == str_vt[j])) {
                    tp.formula_numb = items[index][p].formula_numb;
                    tp.expc = items[index][p].expc;
                    tp.part = items[index][p].part + 1;
                    buf[buf_size++] = tp;
                }
            }
            if (buf_size != 0) {
                Ccount++;
                for (int t = 0; t < buf_size; t++) {
                    items[Ccount][size_item[Ccount]++] = buf[t];
                }
                e_closure(Ccount);
                int  next_state = is_contained();        //看生成的项目集是否已经在项目集族中了
                if (next_state != 0) {
                    size_item[Ccount] = 0;
                    Ccount--;
                }
                else {
                    print_projs(Ccount);
                    cout << C_YELLOW << "***************************************" << C_CLOSE << endl;                    
                }
            }
        }
        //如果.后面为非终结符进行分析
        for (int j = 0; j < size_vn; j++) {
            proj    buf[50];
            int     buf_size = 0;
            proj    tp;
            for (int p = 0; p < size_item[index]; p++) {
                if ((items[index][p].part < length[items[index][p].formula_numb]) && (G[items[index][p].formula_numb][items[index][p].part] == str_vn[j])) {
                    tp.formula_numb = items[index][p].formula_numb;
                    tp.expc = items[index][p].expc;
                    tp.part = items[index][p].part + 1;
                    buf[buf_size++] = tp;
                }
            }
            if (buf_size != 0) {
                Ccount++;
                for (int t = 0; t < buf_size; t++) {
                    items[Ccount][size_item[Ccount]++] = buf[t];
                }
                e_closure(Ccount);
                int  next_state = is_contained();       //看生成的项目集是否已经在项目集族中了
                if (next_state != 0) {
                    size_item[Ccount] = 0;
                    Ccount--;                    
                }

                else {
                    print_projs(Ccount);
                    cout << C_YELLOW << "***************************************" << C_CLOSE << endl;
                }
            }
        }
    }
}

if (size_item[i] == size_item[Ccount])
            for (int j = 0; j < size_item[Ccount]; j++) {
                for (int k = 0; k < size_item[i]; k++)
                    if ((items[Ccount][j].formula_numb == items[i][k].formula_numb) && (items[Ccount][j].part == items[i][k].part) && (items[Ccount][j].expc == items[i][k].expc)) {
                        s++;
                        break;
                    }
            }
if (s == size_item[Ccount])
    return i;