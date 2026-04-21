#include <iostream>

class Number
{
private:
    int m_Value{0};
public:
    Number(const int value) : m_Value(value) {}
    int getValue() const { return m_Value; }
    void printValue() { std::cout << "Value is: " << this->getValue(); }
};

int main(int argc, char **argv)
{
    std::cout << "Hello World" << "\n";

    Number n{420};
    
    n.printValue();
}
