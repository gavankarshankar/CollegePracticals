class A{
    int a,b;
    show(){
        System.out.println("Value of a is"+a+" and value of b is "+b);

    }
}
class B extends A{
    int c;
    void show(){
        System.out.println("Value of C is "+c);
    }
void add(){
    System.out.println("Addition of all number is "+ a+b+c);
}
}
class inheritancedemo{
    public static void main(String[] args) {
        A x=new A();
        x.a=5;
        x.b=10;
        System.err.println("Content of super class A is ");
        x.show()
        B y=new B();
        y.a=12;
        y.b=34;
        System.out.println("Content of class b is ");
        void show();
    }
}